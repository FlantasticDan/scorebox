from secrets import token_hex
from threading import Thread
from typing import Dict

import socketio
import httpx

from consoles.sports import Football

def is_string_ip(string: str) -> bool:
    octets = string.split('.')
    return len(octets) == 4

class TeamConsoleManager:
    '''Team Sports Scored by a Console Game State Manager'''
    def __init__(self, sport, home_team, home_mascot, home_color, visitor_team, visitor_mascot, visitor_color, com_port) -> None:
        self.nonce = token_hex(6)

        self.home_name = home_team
        self.home_mascot = home_mascot
        self.home_color = home_color
        self.visitor_name = visitor_team
        self.visitor_mascot = visitor_mascot
        self.visitor_color = visitor_color

        self.game_state = None # type: Dict

        self.alert_mode = 'neutral'
        self.alert_visibility = 'off'
        self.alert_text = ''
        self.display_mode = 'live'

        self.remote = is_string_ip(com_port)
        self.source = com_port

        if not self.remote:
            self.client = socketio.Client()
            self.client_thread = Thread(target=self.socket_client)
            self.client_thread.start()

            self.console = Football(com_port)
            self.console.on_update = self.updater
        else:
            httpx.get(f'http://{self.source}:9876/init/{sport}')

    
    def updater(self, game_state):
        if self.client.connected:
            self.client.emit('update', game_state)
            self.game_state = game_state
        
    def socket_client(self):
        self.client.connect('http://localhost:5000')
        self.client.wait()

    def overlay_export(self) -> Dict:
        return {
            'home_name': self.home_name,
            'home_mascot': self.home_mascot,
            'home_color': self.home_color,
            'visitor_name': self.visitor_name,
            'visitor_mascot': self.visitor_mascot,
            'visitor_color': self.visitor_color,
        }
    
    def status_export(self) -> Dict:
        return {
            'flag': self.flag_status,
            'alert_mode': self.alert_mode,
            'alert_visibility': self.alert_visibility,
            'alert_text': self.alert_text,
            'display_mode': self.display_mode,
            'play_visibility': self.play_visibility
        }
    
    def set_flag_status(self, new_status) -> None:
        self.flag_status = new_status
    
    def set_alert_mode(self, new_status) -> None:
        self.alert_mode = new_status
    
    def set_alert_visibility(self, new_status) -> None:
        self.alert_visibility = new_status
    
    def set_alert_text(self, new_status) -> None:
        self.alert_text = new_status
        self.alert_visibility = 'on'
    
    def set_display_mode(self, new_mode) -> None:
        self.display_mode = new_mode
    
    def set_play_visibility(self, new_status) -> None:
        self.play_visibility = new_status
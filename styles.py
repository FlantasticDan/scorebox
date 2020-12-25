'''Stylesheets for Qt Widgets'''
# pylint: skip-file

bg_grey = '#1f1f1f'
header_grey = '#3d3d3d'
light_blue = '#0095ff'
dark_blue = '#0062ff'

header_font = 'italic 42px "League Gothic"'

main = f'''\
    background-color: {bg_grey};
'''

header = f'''\
    background-color: {header_grey};
'''

instructions = f'''\
    font-family: "Roboto";
    font-size: 20pt;
    color: white;
'''
buttons = f'''\
    QPushButton{{
        font-family: "Staatliches";
        font-size: 18pt;
        color: white;
        background-color: {light_blue};
        border: 3px solid {light_blue};
    }}

    QPushButton:hover{{
        background-color: {dark_blue};
        border-color: {dark_blue};
    }}

    QPushButton:pressed{{
        background-color: {light_blue};
        border-color: {dark_blue};
    }}
'''

header_label = f'''\
    font: {header_font};
    color: white;
'''
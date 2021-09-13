VERSION = 'v0.0.1 (091221)'

sport = None

def init():
    global sport
    sport = None

def displayable_sport():
    global sport
    if sport == 'waterpolo':
        return 'Water Polo'
    return sport.capitalize()
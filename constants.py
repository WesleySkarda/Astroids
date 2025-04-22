class screen_varables:
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900
    BACKGROUND = 'black'

class astroid_variables:
    ASTEROID_MIN_RADIUS = 20
    ASTEROID_KINDS = 3
    ASTEROID_SPAWN_RATE = 0.8  # seconds
    ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
    ASTEROID_COLOR = 'white'

class menu_variables:
    GAME_FONT = "HyperspaceBold-GM0g.ttf"
    NOT_HOVERING = 'white'
    HOVERING = 'red'

class player_variables:
    PLAYER_RADIUS = 20
    PLAYER_COLOR = 'white'
    LINE_WIDTH = 2
    PLAYER_TURN_SPEED = 300
    PLAYER_SPEED = 200
    PLAYER_SHOOT_SPEED = 500
    PLAYER_SHOOT_COOLDOWN = 0.3

class shooting_contsants:    
    SHOT_RADIUS = 5
    SHOT_COLOR = 'white'

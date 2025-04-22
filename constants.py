class screen_varables:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
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
    high_scores = [('', 940), ('', 900), ('', 760), ('wesley', 700), ('wesley skarda', 480), ('wesley', 380), ('wesley', 280), ('wesley', 260), ('wesley', 220), ('wesley', 160)]
    large_text = int(screen_varables.SCREEN_HEIGHT/10)
    small_text = int(screen_varables.SCREEN_HEIGHT/20)

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
    


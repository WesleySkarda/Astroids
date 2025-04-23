class screen_varables:
    SCREEN_WIDTH = 2560
    SCREEN_HEIGHT = 1440
    BACKGROUND = 'black'
    FPS = 60

class astroid_variables:
    ASTEROID_MIN_RADIUS = int(screen_varables.SCREEN_WIDTH/80)
    ASTEROID_KINDS = 3
    ASTEROID_SPAWN_RATE = 1.0  # seconds
    ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
    ASTEROID_COLOR = 'white'

class menu_variables:
    GAME_FONT = "HyperspaceBold-GM0g.ttf"
    NOT_HOVERING = 'white'
    HOVERING = 'red'
    high_scores = [('est', 24864), ('', 7120), ('wesley', 6440), ('wes', 3920), ('wes', 3420), ('wesley', 3140), ('            ', 1729), ('', 1404), ('wesley', 1180), ('wesley', 1120)]
    large_text = int(screen_varables.SCREEN_HEIGHT/10)
    small_text = int(screen_varables.SCREEN_HEIGHT/20)

class player_variables:
    PLAYER_RADIUS = astroid_variables.ASTEROID_MIN_RADIUS
    PLAYER_COLOR = 'white'
    LINE_WIDTH = int(PLAYER_RADIUS/10)
    PLAYER_TURN_SPEED = 300
    PLAYER_SPEED = 200
    PLAYER_SHOOT_SPEED = 500
    PLAYER_SHOOT_COOLDOWN = 0.3
    PLAYER_LIVES = 2

class shooting_contsants:    
    SHOT_RADIUS = int(player_variables.PLAYER_RADIUS/4)
    SHOT_COLOR = 'white'
    


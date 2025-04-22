from menu import menu, Name_input
import constants
import pygame 
from file_updater import update_file

def Game_over(screen, score):
    game_over = menu(f"game over",screen)
    final_score = menu(f"final score: {score}",screen)
    enter_name = Name_input("Enter your name", screen)
    next_screen = menu("press enter to get to next screen",screen)

    game_over.set_position(constants.screen_varables.SCREEN_HEIGHT/2 - game_over.render().get_height()*4)
    final_score.set_position(game_over.position[1])
    enter_name.set_position(final_score.position[1])
    next_screen.set_position(enter_name.position[1])
    

    pygame_clock = pygame.time.Clock()
    
    cool_down = 5
    cool_down_timer = 1


    while True:
        screen.fill(constants.screen_varables.BACKGROUND)
        dt = pygame_clock.tick(60)/ 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if cool_down <= 0 and event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_RETURN:
                    constants.menu_variables.high_scores.append((enter_name.name, score))
                    constants.menu_variables.high_scores.sort(key=lambda x: x[1], reverse = True)
                    constants.menu_variables.high_scores = constants.menu_variables.high_scores[0:10]
                    update_file("constants.py", {"high_scores": constants.menu_variables.high_scores[0:10]})
                    return "high score"
                
                elif event.type == pygame.K_BACKSPACE or event.unicode == "\x08":
                    enter_name.name = enter_name.name[:-1]
                    cool_down = cool_down_timer

                else:
                    enter_name.name += event.unicode
                    cool_down = cool_down_timer
            else: 
                cool_down -= 1

        game_over.draw()
        final_score.draw()
        enter_name.draw()
        next_screen.draw()
        pygame.display.update()

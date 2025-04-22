import pygame
from menu import menu
import constants
import importlib

def main_menu(screen):
    importlib.reload(constants)

    screen.fill(constants.screen_varables.BACKGROUND)
    title = menu("astroids", screen, 100)
    start_button = menu("Start", screen)
    settings = menu("Settings", screen)
    quit = menu('quit', screen)
    high_score = menu("High Score", screen)

    drawables = [title, start_button, settings, quit, high_score]

    title.set_position((constants.screen_varables.SCREEN_HEIGHT/2-title.render().get_height()*2))
    start_button.set_position((title.position[1]+ title.render().get_height()))
    settings.set_position(start_button.position[1])
    high_score.set_position(settings.position[1])
    quit.set_position(high_score.position[1])

    hovering_list = [start_button, settings, high_score, quit]
    cool_down = 50
    cool_down_timer = 20
    start_button.hover()
    pygame_clock = pygame.time.Clock()
    for item in drawables:
        item.draw()
        
    while True:
        keys = pygame.key.get_pressed()
        dt = pygame_clock.tick(60)/ 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

        if cool_down <= 0:    
            if keys[pygame.K_w]:
                for button in hovering_list:
                    if button.hovering:
                        hovering_list[hovering_list.index(button)-1].hover()
                        button.hover()
                        cool_down = cool_down_timer
                        break
            
            elif keys[pygame.K_s]:
                for button in hovering_list:
                    if button.hovering:
                        if hovering_list.index(button) == len(hovering_list) - 1:
                            button.hover()
                            hovering_list[0].hover()
                            cool_down = cool_down_timer
                            break
                        else:
                            button.hover()
                            hovering_list[hovering_list.index(button)+1].hover()
                            cool_down = cool_down_timer
                            break
            
            if keys[pygame.K_SPACE]:
                for button in hovering_list:
                    if button.hovering:
                        if button.text == "Start":
                            return "game"
                        elif button.text == "Settings":
                            return "settings"
                        elif button.text == "High Score":
                            return "high score"
                        elif button.text == "quit":
                            return "quit"
        else: 
            cool_down -= 1
        pygame.display.update()
from menu import *
import pygame
import constants

def settings(screen):
    screen.fill(constants.screen_varables.BACKGROUND)
    title = menu("Settings", screen, constants.menu_variables.large_text)
    resolution = settings_resolution("resolution", screen)
    Background_color = background_color("backgound color", screen)
    player_color = Player_color('player color', screen)
    astroiod_color = Astroid_color("astroid color", screen)
    text_color = Text_color("text color", screen)
    text_highlight_color = Text_highlight_color("highlight color", screen)
    back = menu("back", screen)
    
    drawables = [title, resolution, Background_color, player_color, astroiod_color, text_color, text_highlight_color, back]

    title.set_position((constants.screen_varables.SCREEN_HEIGHT/2-title.render().get_height()*3))
    resolution.set_position((title.position[1]+ title.render().get_height()))
    Background_color.set_position((resolution.position[1]))
    player_color.set_position(Background_color.position[1])
    astroiod_color.set_position(player_color.position[1])
    text_color.set_position(astroiod_color.position[1])
    text_highlight_color.set_position(text_color.position[1])
    back.set_position(text_highlight_color.position[1])

    hovering_list = [resolution, Background_color, player_color, astroiod_color, text_color, text_highlight_color, back]
    switching_list = [resolution, Background_color, player_color, astroiod_color, text_color, text_highlight_color]
    cool_down = 50
    cool_down_timer = 20
    resolution.hover()
    pygame_clock = pygame.time.Clock()
        
    while True:
        screen.fill(constants.screen_varables.BACKGROUND)
        for item in drawables:
            item.draw()
        keys = pygame.key.get_pressed()
        dt = pygame_clock.tick(60)/ 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for item in switching_list:
                    item.update_variable()
                return 'quit'

        if cool_down <= 0:    
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                for button in hovering_list:
                    if button.hovering:
                        hovering_list[hovering_list.index(button)-1].hover()
                        button.hover()
                        cool_down = cool_down_timer
                        break
            
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
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
            
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                for button in switching_list:
                    if button.hovering:
                        button.back()
                        cool_down = cool_down_timer
                        break
            
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                for button in switching_list:
                    if button.hovering:
                        button.next()
                        cool_down = cool_down_timer
                        break
            if keys[pygame.K_RETURN]:
                for button in hovering_list:
                    if button.hovering and button.text == "back":
                        for item in switching_list:
                            item.update_variable()
                        return 'main_menu'
              
        else: 
            cool_down -= 1
        pygame.display.update()


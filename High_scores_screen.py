import constants
from menu import menu
import pygame

def high_scores(screen):
    title = menu(f"High scores",screen, constants.menu_variables.large_text)
    scores_list = []
    next_screen = menu("press enter to return to menu",screen)
    for i in range(len(constants.menu_variables.high_scores)):
        scores_list.append(menu(f"{i + 1}: {constants.menu_variables.high_scores[i][0]} : {constants.menu_variables.high_scores[i][1]}",screen))
    
    title.set_position()
    scores_list.append(next_screen)
    for Menu in scores_list:
        if scores_list.index(Menu) == 0:
            Menu.set_position(title.position[1]+ title.render().get_height())
        else:
            Menu.set_position(scores_list[scores_list.index(Menu)-1].position[1])
    scores_list.insert(0, title)

    pygame_clock = pygame.time.Clock()
    
    cool_down = 20
    cool_down_timer = 1

    while True:
        screen.fill(constants.screen_varables.BACKGROUND)
        dt = pygame_clock.tick(60)/ 1000
        keys = pygame.key.get_pressed()
        for item in scores_list:
            item.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
        if cool_down <= 0:
                
            if cool_down <= 0:                
                if keys[pygame.K_RETURN]:
                    return "main menu"
            
        else: 
            cool_down -= 1
        pygame.display.update()

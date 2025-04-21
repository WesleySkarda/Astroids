import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot
from menu import menu

def main(screen):
    pygame_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, Shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroidfield = AsteroidField()

    dt = 0
    game_loop_bool = True

    while game_loop_bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,"black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                return
            for bullet in Shots:
                if bullet.is_colliding(asteroid):
                    bullet.kill()
                    asteroid.split()

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = pygame_clock.tick(60)/ 1000
        
def settings(screen):
    pass

def main_menu(screen):
    screen.fill((0, 0, 0))
    pygame_clock = pygame.time.Clock()
    title = menu("astroids", screen, 100)
    start_button = menu("Start", screen)
    settings = menu("Settings", screen)
    quit = menu('quit', screen)
    title.set_position((SCREEN_HEIGHT/2-title.render().get_height()*2))
    start_button.set_position((title.position[1]+ title.render().get_height()))
    settings.set_position(start_button.position[1])
    quit.set_position(settings.position[1])
    hovering_list = [start_button, settings, quit]
    start_button.hover()

    while True:
        keys = pygame.key.get_pressed()
        dt = pygame_clock.tick(10)/ 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            
        if keys[pygame.K_w]:
            for button in hovering_list:
                if button.hovering:
                    hovering_list[hovering_list.index(button)-1].hover()
                    button.hover()
                    break
        
        elif keys[pygame.K_s]:
            for button in hovering_list:
                if button.hovering:
                    if hovering_list.index(button) == len(hovering_list) - 1:
                        button.hover()
                        hovering_list[0].hover()
                        break
                    else:
                        button.hover()
                        hovering_list[hovering_list.index(button)+1].hover()
                        break
        title.draw()
        start_button.draw()
        settings.draw()
        quit.draw()
        pygame.display.update()


        if keys[pygame.K_SPACE]:
            pass
            

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = "main_menu"
    while True:

        if game_state == "main_menu":
            game_state = main_menu(screen)

        if game_state == "game":
            main(screen)
            break

        if game_state == "quit":
            break
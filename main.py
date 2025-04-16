import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
                return print("Game over!")
            for bullet in Shots:
                if bullet.is_colliding(asteroid):
                    bullet.kill()
                    asteroid.split()

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = pygame_clock.tick(60)/ 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
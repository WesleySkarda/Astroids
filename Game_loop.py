import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot
from menu import in_game_text

def game_loop(screen):
    pygame_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shots = pygame.sprite.Group()
    score_counter = in_game_text("Score", screen)
    score_counter.set_position()
    player_lives = in_game_text("extra Lives", screen)
    player_lives.set_position(constants.screen_varables.SCREEN_HEIGHT - player_lives.render().get_height()*3)

    Shot.containers = (updatable, drawable, Shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player((constants.screen_varables.SCREEN_WIDTH/2), (constants.screen_varables.SCREEN_HEIGHT/2))
    asteroidfield = AsteroidField()

    dt = 0
    game_loop_bool = True

    while game_loop_bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return player.Score
        pygame.Surface.fill(screen, constants.screen_varables.BACKGROUND)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                if player.lives == 0:
                    return player.Score
                else:
                    for asteroid in asteroids:
                        asteroid.kill()
                    player.position = pygame.Vector2((constants.screen_varables.SCREEN_WIDTH/2), (constants.screen_varables.SCREEN_HEIGHT/2))
                    player.lives -= 1
            for bullet in Shots:
                if bullet.is_colliding(asteroid):
                    bullet.kill()
                    player.Score += asteroid.split()

        for object in drawable:
            object.draw(screen)
        score_counter.draw(player.Score)
        player_lives.draw(player.lives)
        pygame.display.flip()
        dt = pygame_clock.tick(60)/ 1000
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop_bool = True
    while game_loop_bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        pygame.Surface.fill(screen,"black")
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
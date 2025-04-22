import pygame
import constants
from main_menu import main_menu
from Game_loop import game_loop
from settings import settings
import os
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.screen_varables.SCREEN_WIDTH, constants.screen_varables.SCREEN_HEIGHT))
    game_state = "main menu"
    while True:

        if game_state == "main menu":
            game_state = main_menu(screen)

        if game_state == "game":
            game_loop(screen)
            break

        if game_state == "settings":
            game_state = settings(screen)
            python = sys.executable
            os.execl(python, python, * sys.argv)

        if game_state == "high score":
            break

        if game_state == "quit":
            break
            

if __name__ == "__main__":
    main()

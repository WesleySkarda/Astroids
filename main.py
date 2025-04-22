import pygame
import constants
from main_menu import main_menu
from Game_loop import game_loop
from settings import settings
import os
import sys
from Game_over_screen import Game_over
from High_scores_screen import high_scores

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.screen_varables.SCREEN_WIDTH, constants.screen_varables.SCREEN_HEIGHT))
    game_state = "main menu"
    while True:

        if game_state == "main menu":
            game_state = main_menu(screen)

        if game_state == "game":
            score = game_loop(screen)
            game_state = Game_over(screen, score)
            

        if game_state == "settings":
            game_state = settings(screen)
            python = sys.executable
            os.execl(python, python, * sys.argv)

        if game_state == "high score":
            game_state = high_scores(screen)
            python = sys.executable
            os.execl(python, python, * sys.argv)

        if game_state == "quit":
            break
            

if __name__ == "__main__":
    main()

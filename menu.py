from constants import *
import pygame
class menu():

    def __init__(self, text:str, surface, size = 40):
        self.text = text
        self.size = size
        self.State = NOT_HOVERING
        self.position = (0,0)
        self.surface = surface
        self.hovering = False
    
    def render(self):
        return pygame.font.Font(GAME_FONT, self.size).render(self.text, True, self.State)
    
    def set_position(self, Position:int = 0):
        self.position = (SCREEN_WIDTH/2 - self.render().get_width()/2, self.render().get_height() + Position)

    def draw(self):
        self.surface.blit(self.render(), self.position)

    def hover(self):
        if self.hovering:
            self.hovering = False
            self.State = NOT_HOVERING
        else:
            self.hovering = True
            self.State = HOVERING
        self.draw()


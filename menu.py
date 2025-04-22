import constants
import pygame
from file_updater import update_file


class menu():

    def __init__(self, text:str, surface, size = 40):
        self.text = text
        self.size = size
        self.State = constants.menu_variables.NOT_HOVERING
        self.position = (0,0)
        self.surface = surface
        self.hovering = False
    
    def render(self):
        return pygame.font.Font(constants.menu_variables.GAME_FONT, self.size).render(self.text, True, self.State)
    
    def set_position(self, Position:int = 0):
        self.position = (constants.screen_varables.SCREEN_WIDTH/2 - (self.render().get_width()/2), self.render().get_height() + Position)

    def draw(self):
        self.surface.blit(self.render(), self.position)

    def hover(self):
        if self.hovering:
            self.hovering = False
            self.State = constants.menu_variables.NOT_HOVERING
        else:
            self.hovering = True
            self.State = constants.menu_variables.HOVERING
        self.draw()

class settings_resolution(menu):

    def __init__(self, text, surface, size=40):
        super().__init__(text, surface, size)
        self.resolutions = [(1920, 1080),
                            (1366, 768),
                            (1440, 900),
                            (2560, 1440),
                            (3840, 2160),
                            (1536, 864),
                            (1280, 720),
                            (1600, 900)
                            ]
        self.resolution = (constants.screen_varables.SCREEN_WIDTH, constants.screen_varables.SCREEN_HEIGHT)
        
    def render(self):
        return pygame.font.Font(constants.menu_variables.GAME_FONT, self.size).render(self.text + f": {self.resolution[0]} x {self.resolution[1]}", True, self.State)
    
    def next(self):
        if self.resolutions.index(self.resolution) == len(self.resolutions) - 1:
            self.resolution = self.resolutions[0]
        else:
            self.resolution = self.resolutions[self.resolutions.index(self.resolution) + 1]
    
    def back(self):
        self.resolution = self.resolutions[self.resolutions.index(self.resolution) - 1]

    def update_variable(self):
        update_file("constants.py", {"SCREEN_WIDTH": self.resolution[0],
                                     "SCREEN_HEIGHT": self.resolution[1]})

class settings_color_parent(menu):
    color = None
    update_variable_name:str = ''
    color_list = ["white", "black", "red", "green", "blue", "orange", "purple", "brown", "pink", "grey", "olive", "cyan"]

    def render(self):
        return pygame.font.Font(constants.menu_variables.GAME_FONT, self.size).render(self.text + f":{self.color}", True, self.State)
    
    def update_variable(self):
        update_file("constants.py", {self.update_variable_name: f"'{self.color}'"})
    
    def next(self):
        if self.color_list.index(self.color) == len(self.color_list) - 1:
            self.color = self.color_list[0]
        else:
            self.color = self.color_list[self.color_list.index(self.color) + 1]
    
    def back(self):
        self.color = self.color_list[self.color_list.index(self.color) - 1]


class background_color(settings_color_parent):
    update_variable_name:str = 'BACKGROUND'
    color = constants.screen_varables.BACKGROUND

class Player_color(settings_color_parent):
    update_variable_name:str = 'PLAYER_COLOR'
    color = constants.player_variables.PLAYER_COLOR

class Astroid_color(settings_color_parent):
    update_variable_name:str = 'ASTEROID_COLOR'
    color = constants.astroid_variables.ASTEROID_COLOR

class Text_color(settings_color_parent):
    update_variable_name:str = 'NOT_HOVERING'
    color = constants.menu_variables.NOT_HOVERING

class Text_highlight_color(settings_color_parent):
    update_variable_name:str = 'HOVERING'
    color = constants.menu_variables.HOVERING
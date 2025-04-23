import pygame
import constants

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, CircleShape):
        return (self.radius + CircleShape.radius) >= self.position.distance_to(CircleShape.position)
    
    def bounderies(self):
        if self.position.x > (self.radius + constants.screen_varables.SCREEN_WIDTH):
            self.position.x = 0
        elif self.position.x < (0 - self.radius):
            self.position.x = constants.screen_varables.SCREEN_WIDTH
        
        if self.position.y > (self.radius + constants.screen_varables.SCREEN_HEIGHT):
            self.position.y = 0
        elif self.position.y < (0 - self.radius):
            self.position.y = constants.screen_varables.SCREEN_HEIGHT
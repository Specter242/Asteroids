import pygame

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        surface_size = int(self.radius * 2)  # Make it a bit bigger than needed
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)

    def draw(self, screen): 
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):

        self.position += self.velocity * dt 

        self.rect.center = self.position
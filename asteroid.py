import pygame
import random

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

    def split(self):
        
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            r = random.uniform(20, 50)
            #a = pygame.Vector2(0, 1).rotate(r)
            #b = pygame.Vector2(0, 1).rotate(-r)
            c = self.radius - ASTEROID_MIN_RADIUS
            x = self.position.x
            y = self.position.y
            
            ast1 = Asteroid(x, y, c)
            ast1.velocity = pygame.Vector2(self.velocity * 1.2, self.velocity * 1.2).rotate(r)

            ast2 = Asteroid(x, y, c)
            ast2.velocity = pygame.Vector2(self.velocity * 1.2, self.velocity * 1.2).rotate(-r)


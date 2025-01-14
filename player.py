import pygame

from circleshape import *
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        surface_size = int(self.radius * 4)  # Make it a bit bigger than needed
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.update_image()

    

    # in the player class
    def triangle(self):
        center = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): 
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = self.position

    def update_image(self):
        # Clear the previous drawing
        self.image.fill((0, 0, 0, 0))
        # Get triangle points and draw them
        points = self.triangle()
        pygame.draw.polygon(self.image, "white", points, 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt) 

        self.update_image()   

from constants import *
from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self,x,y, radius):
        super().__init__(x,y,radius)
        self.radius = radius
        self.rotation = 0

    # dibujar circulo
    def draw(self, screen):
        pygame.draw.circle(
        screen,
        "white",
        self.position,
        self.radius,
        2)

    def update(self, dt):
        self.position += self.velocity * dt
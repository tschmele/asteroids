import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_left = self.velocity.rotate(-angle)
        new_right = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        left_ast = Asteroid(self.position[0], self.position[1], new_radius)
        right_ast = Asteroid(self.position[0], self.position[1], new_radius)
        left_ast.velocity = new_left * 1.2
        right_ast.velocity = new_right * 1.2
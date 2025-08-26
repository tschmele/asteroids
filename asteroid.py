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
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        rand_angle = random.uniform(20, 50)
        new_angles = [
            self.velocity.rotate(-rand_angle),
            self.velocity.rotate(rand_angle)
        ]
        for angle in new_angles:
            Asteroid(self.position[0], self.position[1], new_radius).velocity = angle * 1.2
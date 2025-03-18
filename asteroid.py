import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = tuple(pygame.sprite.Group())

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, screen):
        self.kill()
        random_angle = random.uniform(20, 50)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x_value, y_value = self.position
        steroid = Asteroid(x_value, y_value, new_radius)
        steroid.velocity = a * 1.2
        steroid = Asteroid(x_value, y_value, new_radius)
        steroid.velocity = b * 1.2

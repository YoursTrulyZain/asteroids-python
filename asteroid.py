import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


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
        
        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        positive_vector = self.velocity.rotate(new_angle)
        negative_vector = self.velocity.rotate(-new_angle)
        positive_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        negative_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        positive_asteroid.velocity = positive_vector * 1.2
        negative_asteroid.velocity = negative_vector * 1.2
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill("black")

        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_collision(shot):
                    asteroid.split()
                    shot.kill()

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = pygame_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
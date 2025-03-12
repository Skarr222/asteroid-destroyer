import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
)
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 1))
        player.draw(screen)
        pygame.display.flip()
        player.update(dt)
        dt = clock.tick(60) / 1000  # Now this works correctly


if __name__ == "__main__":
    main()

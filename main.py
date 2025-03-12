import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 1))

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        for sprite in updatable:
            sprite.update(dt)

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

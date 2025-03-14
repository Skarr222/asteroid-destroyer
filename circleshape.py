import pygame


class CircleShape(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(*self.containers)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

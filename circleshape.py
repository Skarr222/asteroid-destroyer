import pygame


class CircleShape(pygame.sprite.Sprite):
    containers = pygame.sprite.Group()

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
    
    def collision(self, target):
        return self.position.distance_to(target.position) <= self.radius + target.radius 
        

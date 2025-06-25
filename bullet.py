import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction="down", speed=5):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))  # Red bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = speed
        self.direction = direction

    def update(self):
        if self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

        # Kill if out of screen (tweak if needed)
               # Kill if out of screen (tweak if needed)
        if (self.rect.top > 600 or self.rect.bottom < 0 or
            self.rect.left > 800 or self.rect.right < 0):
            self.kill()

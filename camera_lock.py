import pygame

class CameraLock:
    def __init__(self, screen_width, screen_height):
        self.offset = pygame.Vector2(0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, target):
        """Center the camera on the target (player)."""
        self.offset.x = target.rect.centerx - self.screen_width // 2
        self.offset.y = target.rect.centery - self.screen_height // 2

    def apply(self, entity):
        """Adjust entity position based on camera offset."""
        return entity.rect.move(-self.offset.x, -self.offset.y)

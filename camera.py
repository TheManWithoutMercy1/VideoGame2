import pygame
pygame.init()
class Camera:
    def __init__(self, player_rect, screen, color):
        self.player_rect = player_rect
        self.screen = screen
        self.color = color
    def _draw_camera(self, rects):
        camera_width, camera_height = 600, 500  # Define camera size
        camera_x = self.player_rect.x + self.player_rect.width // 2 - camera_width // 2
        camera_y = self.player_rect.y + self.player_rect.height // 2 - camera_height // 2
        camera_rect = pygame.Rect(camera_x, camera_y, camera_width, camera_height)
        pygame.draw.rect(self.screen, self.color, camera_rect, 2)
        for rect in rects:
          return rect.move(camera_rect.topleft)
    

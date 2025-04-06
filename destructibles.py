import pygame

pygame.init()

box = pygame.image.load("images/Sprites/box_image.png")
box2 = pygame.transform.scale(box, (100,100))

class Destructible:
    def __init__(self, x_pos, y_pos, screen):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.screen = screen

    def draw(self, camera_x):
        # Adjust the rect's x position based on camera_x
         adjusted_rect = pygame.Rect(self.x_pos - camera_x, self.y_pos, 60, 60)
         pygame.draw.rect(self.screen, "Green", adjusted_rect)
         self.rect = adjusted_rect

    def check_event(self,pos):
        if self.rect.collidepoint(pos):
            print("destructible detected")

    

   
import pygame
from pygame.sprite import Sprite

class NPC(Sprite):
    def __init__(self,screen,x,y):
        super().__init__()
        self.screen = screen
        

import pygame
import random
from pygame.sprite import Sprite
class Spiderslayer(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.spider_slayer = pygame.image.load("images/Sprites/spider_slayer.png")
        self.image = pygame.transform.scale(self.spider_slayer,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vely = 0
        self.velx = 0
        self.idle = True
        center_x,center_y = self.rect.center


    def move(self):
        self.velx += 0.05
        self.rect.x += self.velx
        print("MOVING !!!")


    
     
 







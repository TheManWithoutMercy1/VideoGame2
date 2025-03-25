import pygame
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self):
        self.enemy_image = pygame.image.load("images/Sprites/enemy_soldier.png")
        self.enemy_hurt = pygame.image.load("images/Sprites/enemy_soldier_hurt.png")
        self.resized_enemy_hurt = pygame.transform.scale(self.enemy_hurt,(100,100))
        self.resized_enemy_image = pygame.transform.scale(self.enemy_image,(100,100))
        self.rect = self.resized_enemy_image.get_rect()
        self.velx = 1
        self.vely = 0
        self.rect.x = 600
        self.rect.y = 480
        self.gravity = 0.5
        self.hurt = False
        self.launched = False
        self.idle = True
        self.Enemy_rect = pygame.Rect(self.rect.x,self.rect.y,100,100)

    
    def _knockback_(self):
          if not self.hurt:
            self.hurt = True
            self.hurt_start_time = pygame.time.get_ticks()
            self.velx = 4.5
            self.rect.x += self.velx
            self.Enemy_rect.x += self.velx

    def _launched_(self):
            if not self.launched:  # Only set the launch time once
             self.launched = True
             self.launched_start_time = pygame.time.get_ticks()
             self.rect.y -= 150
             self.Enemy_rect.y -= 150
             self.gravity = 0  # Stop gravity initially

    def _update_movements(self, rects):
           if self.launched:
            if pygame.time.get_ticks() - self.launched_start_time >= 750:
              self.launched = False  # Allow gravity after 2 seconds
           if not self.launched:
              self.gravity = 1  # Resume gravity when not in launched state

           if self.hurt:
             if pygame.time.get_ticks() - self.hurt_start_time >= 250:
               self.hurt = False

           self.vely -= self.gravity
           self.rect.y -= self.vely

           for rect in rects:
            if self.rect.colliderect(rect):
                if self.vely < 0:  # Falling
                    self.rect.bottom = rect.top
                    self.Enemy_rect.bottom = rect.top
                    self.vely = 0
    
    def _update_sprites(self):
        if self.launched:
           self.resized_enemy_image = self.resized_enemy_hurt
        elif self.hurt:
            self.resized_enemy_image = self.resized_enemy_hurt
        else:  
           self.resized_enemy_image =  pygame.transform.scale(self.enemy_image,(100,100))
    

    

   





    

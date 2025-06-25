import pygame
import random
from pygame.sprite import Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.enemy_image = pygame.image.load("images/Sprites/enemy_stand.png")
        self.enemy_hurt = pygame.image.load("images/Sprites/enemy_striked.png")
        self.enemy_attack = pygame.image.load("images/Sprites/enemy_attack.png")
        self.enemy_walk = pygame.image.load("images/Sprites/enemy_walk.png")
        self.enemy_block = pygame.image.load("images/Sprites/enemy_block.png")
        self.resized_block_attack = pygame.transform.scale(self.enemy_block,((100,100)))
        self.resized_enemy_attack = pygame.transform.scale(self.enemy_attack,((100,100)))
        self.resized_enemy_hurt = pygame.transform.scale(self.enemy_hurt,(100,100))
        self.resized_enemy_image = pygame.transform.scale(self.enemy_image,(100,100))
        self.resized_enemy_walk = pygame.transform.scale(self.enemy_walk,(100,100))
        self.rect = self.resized_enemy_image.get_rect()
        self.velx = 40
        self.vely = 0
        self.rect.x = x
        self.rect.y = y
        self.gravity = 0.5
        self.hurt = False
        self.launched = False
        self.idle = True
        self.attacking = False
        self.guarding = False
        center_x,center_y = self.rect.center
        self.health = 175
        self.Enemy_rect = pygame.Rect(self.rect.x,self.rect.y,100,100)
        self.detect_player = pygame.Rect((center_x-200),center_y,450,450)

    def _yanked_left(self):
         self.rect.x -= self.velx 
         self.Enemy_rect.x -= self.velx
         self.detect_player.x -= self.velx

    def _yanked_right(self):
         self.rect.x += self.velx
         self.Enemy_rect.x += self.velx
         self.detect_player.x += self.velx

    def _yanked_left_web(self):
         self.rect.x -= self.velx 
         self.Enemy_rect.x -= self.velx
         self.detect_player.x -= self.velx

    def _yanked_right_web(self):
         self.rect.x += self.velx
         self.Enemy_rect.x += self.velx
         self.detect_player.x += self.velx
         
    def _move_mode(self):
      if not self.launched:
        if random.random() < 0.5 and not self.guarding: 
           self._yanked_left()
        else:
           self._yanked_right()

    def _attack_mode(self):
       if not self.attacking and random.random() < 0.5:  # 50% chance to attack
        self.attacking = True
        self.attack_start_time = pygame.time.get_ticks()
        self._move_mode()

    def _enemy_hurt(self):
     if random.random() < 0.3:  # 30% chance to block instead of take damage
        self._block_()
        print("Enemy blocked the attack!")
     else:
        self.health -= 1
        print("Enemy took damage!")
        self._check_health()
    
    def _check_health(self):
        if self.health <= 0:
            self.kill()

    def _block_(self):
        self.guarding = True
        self.block_start_time = pygame.time.get_ticks()
    
    def _knockback_(self):
          if not self.hurt:
            self.hurt = True
            self.hurt_start_time = pygame.time.get_ticks()
            self.rect.x += self.velx
            self.Enemy_rect.x += self.velx
            self.detect_player.x += self.velx

    def _launched_(self):
            if not self.launched:  # Only set the launch time once
             self.launched = True
             self.launched_start_time = pygame.time.get_ticks()
             self.rect.y -= 150
             self.Enemy_rect.y -= 150
             #self.detect_player.x -= 150
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

           if self.guarding:
              if pygame.time.get_ticks() - self.block_start_time >= 250:
               self.guarding = False
 

           self.vely -= self.gravity
           self.rect.y -= self.vely



           if self.attacking:
             if pygame.time.get_ticks() - self.attack_start_time > random.randint(100,2000):
                self.attacking = False
          

           for rect in rects:
            if self.rect.colliderect(rect):
                if self.vely < 0:  # Falling
                    self.rect.bottom = rect.top
                    self.Enemy_rect.bottom = rect.top
                    self.detect_player.bottom = rect.top
                    self.vely = 0

    
    def _update_sprites(self):
        if self.launched:
           self.resized_enemy_image = self.resized_enemy_hurt
        elif self.hurt:
            self.resized_enemy_image = self.resized_enemy_hurt
        elif self.attacking:
            self.resized_enemy_image = self.resized_enemy_attack
        elif self.guarding:
           self.resized_enemy_image = self.resized_block_attack
        else:  
           self.resized_enemy_image =  pygame.transform.scale(self.enemy_image,(100,100))
    

    
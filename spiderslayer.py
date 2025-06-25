import pygame
import random
from pygame.sprite import Sprite
from bullet import Bullet 
class Spiderslayer(pygame.sprite.Sprite):
    def __init__(self,x,y,  bullet_group):
        super().__init__()
        self.spider_slayer = pygame.image.load("images/Sprites/spider_slayer.png")
        self.image = pygame.transform.scale(self.spider_slayer,(100,100))
        self.rect = self.image.get_rect()
        self.bullet_group = bullet_group
        self.rect.x = x
        self.rect.y = y
        self.vely = 0
        self.velx = 0
        self.idle = True
        self.health = 75
        self.time = pygame.time.get_ticks()
        self.last_shot_time = 0
        center_x,center_y = self.rect.center
        self.time = pygame.time.get_ticks()

    def update(self):
        if self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed

    def move_right(self):
        self.velx += 0.05
        self.rect.x += self.velx
        print("MOVING RIGHT!!!")

    def move_left(self):
        self.velx -= 0.05
        self.rect.x -= self.velx
        print("MOVING LEFT!!")

    def _check_health(self):
        if self.health <= 0:
            self.kill()

    def hurt(self):
        self.health -= 1


    def moving(self):
        now = pygame.time.get_ticks()
        if now - self.time < 2500:
            self.move_right()
        elif now - self.time < 5000:
            self.move_left()
        elif now - self.time < 10000:
            self.shoot()  # idle phase → shoot bullets
        else:
            self.time = now


    def shoot(self):
     now = pygame.time.get_ticks()
     if now - self.last_shot_time > 1000:  # shoot every 1 second
        bullet_x = self.rect.centerx
        bullet_y = self.rect.bottom  # spawn at the bottom
        bullet = Bullet(bullet_x, bullet_y, direction='down', speed=5)  # custom direction
        self.bullet_group.add(bullet)
        self.last_shot_time = now

    
        



    
     
 







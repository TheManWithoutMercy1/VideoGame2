import pygame
from pygame.sprite import Sprite
GRAVITY = 3
WHITE = (255, 255, 255)
class Player(Sprite):
    #constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Sprites/player.png")
        self.attack_image = pygame.image.load("images/Sprites/punch1.png")
        self.attack2_image = pygame.image.load("images/Sprites/punch2.png")
        self.attack3_image = pygame.image.load("images/Sprites/punch3.png")
        self.uppercut_image = pygame.image.load("images/Sprites/uppercut.png")
        self.resized_uppercut = pygame.transform.scale(self.uppercut_image,(125,125))
        self.air_attack_image = pygame.image.load("images/Sprites/airattack.png")
        self.resized_airattack = pygame.transform.scale(self.air_attack_image,(100,100))

        self.web_swing_image = pygame.image.load("images/Sprites/web_swing.png")
        self.resized_swing_image = pygame.transform.scale(self.web_swing_image,(125,125))

        self.kick_image = pygame.image.load("images/Sprites/kick1.png")
        self.kick_image2 = pygame.image.load("images/Sprites/kick2.png")

        self.resized_kick_image = pygame.transform.scale(self.kick_image,(100,100))
        self.resized_kick_image2 = pygame.transform.scale(self.kick_image2,(100,100))
    
        self.run_image1 = pygame.image.load("images/Sprites/run_sprite1.png")
        self.run_image2 = pygame.image.load("images/Sprites/run_sprite2.png")
        self.run_image3 = pygame.image.load("images/Sprites/run_sprite3.png")
        self.run_image4 = pygame.image.load("images/Sprites/run_sprite4.png")
        self.run_image5 = pygame.image.load("images/Sprites/run_sprite5.png")
        self.run_image6 = pygame.image.load("images/Sprites/run_sprite6.png")
        self.run_image7 = pygame.image.load("images/Sprites/run_sprite7.png")
        self.run_image8 = pygame.image.load("images/Sprites/run_sprite8.png")
        self.run_image9 = pygame.image.load("images/Sprites/run_sprite9.png")
        self.run_image10 = pygame.image.load("images/Sprites/run_sprite10.png")
        self.run_image11 = pygame.image.load("images/Sprites/run_sprite11.png")

# Resize all run images
        self.resized_run_image4 = pygame.transform.scale(self.run_image4, (100, 100))
        self.resized_run_image5 = pygame.transform.scale(self.run_image5, (100, 100))
        self.resized_run_image6 = pygame.transform.scale(self.run_image6, (100, 100))
        self.resized_run_image7 = pygame.transform.scale(self.run_image7, (100, 100))
        self.resized_run_image8 = pygame.transform.scale(self.run_image8, (100, 100))
        self.resized_run_image9 = pygame.transform.scale(self.run_image9, (100, 100))
        self.resized_run_image10 = pygame.transform.scale(self.run_image10, (100, 100))
        self.resized_run_image11 = pygame.transform.scale(self.run_image11, (100, 100))

# Flipped versions
        self.resized_run_image4_flipped = pygame.transform.flip(self.resized_run_image4, True, False)
        self.resized_run_image5_flipped = pygame.transform.flip(self.resized_run_image5, True, False)
        self.resized_run_image6_flipped = pygame.transform.flip(self.resized_run_image6, True, False)
        self.resized_run_image7_flipped = pygame.transform.flip(self.resized_run_image7, True, False)
        self.resized_run_image8_flipped = pygame.transform.flip(self.resized_run_image8, True, False)
        self.resized_run_image9_flipped = pygame.transform.flip(self.resized_run_image9, True, False)
        self.resized_run_image10_flipped = pygame.transform.flip(self.resized_run_image10, True, False)
        self.resized_run_image11_flipped = pygame.transform.flip(self.resized_run_image11, True, False)


        self.run_image = pygame.image.load("images/Sprites/run.png")
        self.resized_run_image = pygame.transform.scale(self.run_image,(100,100))
        self.resized_run_image2 = pygame.transform.flip(self.resized_run_image,True,False)

        self.resized_image = pygame.transform.scale(self.image,(100,100))
        self.resized_image1 = pygame.transform.scale(self.image,(100,100))
        self.resized_image2 = pygame.transform.flip(self.resized_image,True,False)

        self.jump_image = pygame.image.load("images/Sprites/jump.png")

        self.resized_jump = pygame.transform.scale(self.jump_image, (100,100))
        self.resized_jump2 = pygame.transform.flip(self.resized_jump, True, False)

        self.resized_run_image1 = pygame.transform.scale(self.run_image1,(100,100))
        self.resized_run_image2 = pygame.transform.scale(self.run_image2, (100,100))
        self.resized_run_image3= pygame.transform.scale(self.run_image3, (100,100))

        self.resized_attack_image = pygame.transform.scale(self.attack_image,(100,100))
        self.resized_attack_image2 = pygame.transform.flip(self.resized_attack_image,True,False)
        self.resized_attack2_image = pygame.transform.scale(self.attack2_image,(100,100))
        self.resized_attack3_image = pygame.transform.scale(self.attack3_image,(100,100))
        self.rect = self.resized_image.get_rect()
        self.velx = 1.5
        self.vely = 0
        self.rect.x = 350
        self.rect.y = 480
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.facing_right = True
        self.facing_left = False
        self.attacking = False
        self.jumping = False
        self.falling = True
        self.running = False
        self.player_boosted = False
        self.player_rect = pygame.Rect(self.rect.x,self.rect.y,100,100)
        self.attack_count = 0
        self.run_count = 0
       # self.idle = True

    def _update_movement(self, rects):
        print(self.rect.x)
        print(self.rect.y)
        self.attacking = False
        self.uppercut = False
        self.idle = True
        self.falling = True
        self.swinging = False
        self.vely -= GRAVITY 
        self.rect.y -= self.vely
        self.player_rect.y  -= self.vely
        start_time = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if self.attack_count >= 100:
            self.attack_count = 0
        for rect in rects:
            if self.rect.colliderect(rect):
                if self.vely < 0:  # Falling
                    self.rect.bottom = rect.top
                    self.player_rect.bottom = rect.top
                    self.jumping = False
                    self.vely = 0
                    
        if key[pygame.K_w]:
            #shoot webline
            self.swinging = True
            print("shooting webline!")

        if self.swinging:
            print(f"velocity is {self.velx}")

        if key[pygame.K_s]:
            print("shooting web grapple!")

        #if self.velx >= 10.0:
         #   self.velx = 2.5

        if key[pygame.K_RIGHT]: # right key
            print(f"moving right ! {self.rect.x - self.velx}")
            self.running = True
            self.idle = False
            self.facing_left = False
            self.facing_right = True
            self.run_count +=1
            print("right key pressed!")
            self.rect.x += self.velx # move right
            self.player_rect.x += self.velx
            self.run_right_time = pygame.time.get_ticks()
            

            for rect in rects:
                if self.rect.colliderect(rect):
                    self.rect.right = rect.left
                    self.player_rect.right = rect.left
                 
        elif key[pygame.K_LEFT]: # left key 
            print(f"moving left ! {self.rect.x - self.velx}")
            self.running = True
            self.idle = False
            self.facing_right = False
            self.facing_left = True
            self.resized_image = self.resized_run_image2
            print("left key pressed!")
            self.rect.x -= self.velx # move left
            self.player_rect.x -= self.velx
            for rect in rects:
                
                if self.rect.colliderect(rect):  
                    self.player_rect.left = rect.right
                    self.rect.left = rect.right
        else:
            self.running = False
        if key[pygame.K_d] and not self.attacking:
            self.running = False
            self.attack_count += 1
            print(f"attack count is {self.attack_count}")
            print("d presssed!")
            self.attacking = True  # Start the attack
            self.attack_start_time = pygame.time.get_ticks()

        if key[pygame.K_f]:
            self.running = False
            print("uppercut attack!")
            self.uppercut = True
            self.idle = False

        if key[pygame.K_SPACE]:
            print("jump pressed!")#
            self.jumping_start_time = pygame.time.get_ticks()
            self.jumping = True   

        if self.jumping:
            if not self.swinging:
             self.rect.y += -34
             self.player_rect.y  += -34
             if pygame.time.get_ticks() - self.jumping_start_time >= 2000:
                self.jumping = False
            if self.swinging:
                self.vely = 0

        if self.uppercut:
            self.resized_image = self.resized_uppercut
            
        if self.facing_left and self.idle:
            self.resized_image = self.resized_image2
        if self.facing_right and self.idle:
            self.resized_image = self.resized_image1 
        if self.facing_right and self.jumping:
            self.resized_image = self.resized_jump
        if self.facing_left and self.jumping:
            self.resized_image = self.resized_jump2
        
        if self.swinging:
            self.resized_image = self.resized_swing_image

        if self.attacking:
            if self.jumping:
                self.resized_image = self.resized_airattack
            if self.facing_right and self.attack_count >= 0:
               self.resized_image = self.resized_attack_image  
            if self.facing_right and self.attack_count >= 20:
                self.resized_image = self.resized_attack2_image
            if self.facing_right and self.attack_count >= 40:
                self.resized_image = self.resized_attack3_image
            if self.facing_right and self.attack_count >= 60:
                self.resized_image = self.resized_kick_image
            if self.facing_right and self.attack_count >= 80:
                self.resized_image = self.resized_kick_image2
            if self.facing_left:
                self.resized_image = self.resized_attack_image2
            if pygame.time.get_ticks() - self.attack_start_time >= 2000:
               print("attack time over")
               self.attacking = False

        if self.running:
         if self.facing_right:
            if self.run_count>= 0:
                self.resized_image = self.resized_run_image4
            if self.run_count >= 10:
                self.resized_image = self.resized_run_image5
            if self.run_count >= 20:
                self.resized_image = self.resized_run_image6
            if self.run_count >= 30:
                self.resized_image = self.resized_run_image7
            if self.run_count >= 40:
                self.resized_image = self.resized_run_image8
            if self.run_count >= 50:
                self.resized_image = self.resized_run_image9
            if self.run_count >= 60:
                self.resized_image = self.resized_run_image10
            if self.run_count >= 70:
                self.resized_image = self.resized_run_image11
            if self.run_count >= 80:
                self.run_count = 0

          
        
   

      
        

        
        
  
        
       
        





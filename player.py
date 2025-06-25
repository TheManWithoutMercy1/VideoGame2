import pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.init() 
from pygame.sprite import Sprite
GRAVITY = 3
WHITE = (255, 255, 255)

#web_sound = pygame.mixer.Sound('Voicy_Spider-Man web shoot sound effect.mp3')
jump_sound = pygame.mixer.Sound('jump_05.wav')
punch_sound = pygame.mixer.Sound('hard-punch-90179.mp3')

class Player(Sprite):
    #constructor
    def __init__(self,screen,x,y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("images/Sprites/player.png")
        self.attack_image = pygame.image.load("images/Sprites/punch1.png")
        self.attack2_image = pygame.image.load("images/Sprites/punch2.png")
        self.attack3_image = pygame.image.load("images/Sprites/punch3.png")
        self.shooter_image = pygame.image.load("images/Sprites/shoot_sprite.png")
        self.spider_hurt = pygame.image.load("images/Sprites/spider_hurt.png")
        self.grab = pygame.image.load("images/Sprites/grab.png")
        self.spider_grab = pygame.transform.scale(self.grab,(100,100))
        self.spider_hurt_resized = pygame.transform.scale(self.spider_hurt,(100,100))
        self.air_kick_image = pygame.image.load("images/Sprites/airkick.png")
        health_image = pygame.image.load("images/Sprites/health_bar_img.png")
        self.swing_image1 = pygame.image.load("images/Sprites/swing_stance1.png")
        self.swing_image2 = pygame.image.load("images/Sprites/swing_stance2.png")
        self.swing_image3 = pygame.image.load("images/Sprites/swing_stance3.png")
        self.swing_image4 = pygame.image.load("images/Sprites/swing_stance4.png")
        self.swing_image5 = pygame.image.load("images/Sprites/swing_stance5.png")
        self.swing_image6 = pygame.image.load("images/Sprites/swing_stance6.png")
        self.swing_image7 = pygame.image.load("images/Sprites/swing_stance7.png")
        self.swing_image8 = pygame.image.load("images/Sprites/swing_stance8.png")
        self.swing_image9 = pygame.image.load("images/Sprites/swing_stance9.png")
        self.swing_image1 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance1.png"), (100, 100))
        self.swing_image2 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance2.png"), (100, 100))
        self.swing_image3 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance3.png"), (100, 100))
        self.swing_image4 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance4.png"), (100, 100))
        self.swing_image5 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance5.png"), (100, 100))
        self.swing_image6 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance6.png"), (100, 100))
        self.swing_image7 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance7.png"), (100, 100))
        self.swing_image8 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance8.png"), (100, 100))
        self.swing_image9 = pygame.transform.scale(pygame.image.load("images/Sprites/swing_stance9.png"), (100, 100))
        self.resized_air_kick_image = pygame.transform.scale(self.air_kick_image,(100,100))
        self.resized_shooter_image = pygame.transform.scale(self.shooter_image,(100,100))
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
        self.rect.x = x
        self.rect.y = y
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
        self.shooting = False
        self.on_ground = False
        self.web_active = False
        self.web_end = None
        self.rush = False
        self.hurt = False
        self.grab = False
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
        global key
        key = pygame.key.get_pressed()
        dx = 0
        dy = 0
    
        if self.attack_count >= 100:
            self.attack_count = 0
        for rect in rects:
            if self.rect.colliderect(rect):
                if self.vely  < 0:  # Falling downward, landing on a platform
                    self.on_ground = True
                
                    self.rect.bottom = rect.top  # Land on the platform
                    self.player_rect.bottom = rect.top  # Ensure player's feet align with the platform
                    self.jumping = False  # Stop the jumping state
                    self.vely = 0  # Reset velocity
                if self.vely < 0 and not self.on_ground:
                    self.rect.top = rect.bottom
                    self.player_rect.top = rect.bottom
                    self.vely = 0
        if key[pygame.K_z]:
            if self.web_active:
                self.web_active = False
            else:
                self.web_active = True
                
        if key[pygame.K_w]:
            #shoot webline
            self.swinging = True
            print("shooting webline!")

        if self.swinging:
            #web_sound.play()
            print(f"velocity is {self.velx}")

        if key[pygame.K_s]:
            self.shooting = True
            print("shooting web grapple!")
        else:
            self.shooting = False

        if key[pygame.K_RIGHT] and not self.swinging: # right key
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
        
                 
        elif key[pygame.K_LEFT] and not self.swinging: # left key 
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
            punch_sound.play()
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
            jump_sound.play()
            print("jump pressed!")#
            self.jumping_start_time = pygame.time.get_ticks()
            self.jumping = True  

        if key[pygame.K_g]:
            print("grab")
            self.grab = True 
            self.grab_start_time = pygame.time.get_ticks()


        if self.jumping:
            if not self.swinging:
             self.rect.y += -34
             self.player_rect.y  += -34
             if pygame.time.get_ticks() - self.jumping_start_time >= 2000:
                self.jumping = False
            if self.swinging:
                self.vely = 0

        if self.grab:
            self.resized_image = self.spider_grab
            if pygame.time.get_ticks() - self.grab_start_time > 1000:
                self.grab = False

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

        if self.shooting:
            self.resized_image = self.resized_shooter_image

        if self.attacking:
            if self.facing_right and self.attack_count >= 0:
               self.resized_image = self.resized_attack_image  
            if self.facing_right and self.attack_count >= 15:
                self.resized_image = self.resized_attack2_image
            if self.facing_right and self.attack_count >= 30:
                self.resized_image = self.resized_attack3_image
            if self.facing_right and self.attack_count >= 45:
                self.resized_image = self.resized_kick_image
            if self.facing_right and self.attack_count >= 60:
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
         elif self.facing_left:
                if self.run_count >= 0:
                    self.resized_image = self.resized_run_image4_flipped
                if self.run_count >= 10:
                    self.resized_image = self.resized_run_image5_flipped
                if self.run_count >= 20:
                    self.resized_image = self.resized_run_image6_flipped
                if self.run_count >= 30:
                    self.resized_image = self.resized_run_image7_flipped
                if self.run_count >= 40:
                    self.resized_image = self.resized_run_image8_flipped
                if self.run_count >= 50:
                    self.resized_image = self.resized_run_image9_flipped
                if self.run_count >= 60:
                    self.resized_image = self.resized_run_image10_flipped
                if self.run_count >= 70:
                    self.resized_image = self.resized_run_image11_flipped
                if self.run_count >= 80:
                    self.run_count = 0

        # Only show hurt sprite if not attacking, jumping, running, swinging, etc.
        if self.hurt and not (self.attacking or self.jumping or self.running or self.swinging or self.shooting or self.uppercut):
          self.resized_image = self.spider_hurt_resized
          if pygame.time.get_ticks() - self.hurt_start_time > 1000:
             self.hurt = False


            
    def _web_zip(self,event,rects,camera_x,d=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse click detected")
            print(pygame.mouse.get_pos())
            x,y = (pygame.mouse.get_pos())
            world_pos = (x + camera_x, y)
            self.check_event(world_pos,rects)
            d.check_event(world_pos)

    def check_event(self, pos, rects):
     if self.rect.collidepoint(pos):
        print("player detected") 

     for rect in rects:
        if rect.collidepoint(pos):  
            print("infrastructure detected at:")
            self.web_line(pos,self.screen)
            web_x,web_y = pos
            if self.web_active:
                self.web_rush(web_x,web_y)
    
         
    def web_rush(self,web_x,web_y):
              print("TESTING!")
              self.rect.x = web_x
              self.player_rect.x = web_x
              self.player_rect.y = web_y
              self.rect.y = web_y 
            
    def web_line(self, web_end, screen):
            self.web_end = web_end
            self.web_active = True
            print(f"Shooting webline from {self.rect.center} to {web_end}")

    def player_hurt(self):
     if not self.hurt:  # Only set hurt once per collision cycle
        self.hurt = True
        self.hurt_start_time = pygame.time.get_ticks()

   

        

    
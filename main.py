import pygame
from player import Player
import random
from camera import Camera
from NewYork import create_map
from Enemies import Enemy
from destructibles import Destructible
from camera_lock import CameraLock  # Import camera system

tile_image = pygame.image.load("images/Sprites/Level Design/Ground.png")
health_image = pygame.image.load("images/Sprites/health_bar_img.png")
health_image_r = pygame.transform.scale(health_image,(140,75))

tile_size = 10
WHITE = (255, 255, 255)
tile_map = [
    [0]*100 for _ in range(10)
] + [
    [0]*20 + [1]*5 + [0]*75,               # small left platform
    [0]*50 + [1]*10 + [0]*40,              # middle platform
    [0]*80 + [1]*5 + [0]*15,               # right floating platform
    [0]*10 + [1] + [0]*88 + [1],           # two vertical pillars
    [0]*10 + [1] + [0]*88 + [1],
    [0]*10 + [1] + [0]*88 + [1],
    [0]*10 + [1] + [0]*88 + [1],
    [0]*10 + [1]*10 + [0]*80,              # lower platform
    [0]*30 + [1]*5 + [0]*65,               # jumpable block
    [0]*60 + [1]*5 + [0]*35,               # jumpable block
    [0]*90 + [1]*10,                       # far right wall ledge
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,

    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,

    [0]*100,
    [0]*100,
    [0]*100,
    [0]*100,

    
    [0]*100,
    [0]*100,

    [0]*100,
    [0]*100,

    [1]*1000                                 # solid ground
]

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
color = (255,0,0)
player = Player(screen)
enemy = Enemy(500,600)
enemy2 = Enemy(800,600)
enemy3 = Enemy(1200,600)
enemies = pygame.sprite.Group()
enemies.add(enemy)
enemies.add(enemy2)
enemies.add(enemy3)
d = Destructible(100,50,screen)
destructibles = [d]

# Drawing Rectangle

camera = Camera( player.player_rect, screen ,color)
rects = []  # Initialize the list once
camera_lock = CameraLock(400, 800)
camera_x = 0
camera_y = 0

BLACK = (0,0,0)

def _draw_health_bar():
   screen.blit(health_image_r, (10,9))
   pygame.draw.rect(screen, color, pygame.Rect(60, 30, 75, 15))
   pygame.draw.rect(screen, BLACK, pygame.Rect(60, 30, 75, 15),2)
  
def _enemies_defeated():
    if enemies == 0:
       print("ENEMIES DEFEATED")



def _draw_collisions(tile_map):
    global rects  
    rects.clear()  # Clear previous rects to avoid duplication
    for row_index, row in enumerate(tile_map):
        for col_index, tile in enumerate(row):
            if tile == 1:  # If tile is solid (collision)
                x = col_index * tile_size  # Store world position (no camera offset)
                y = row_index * tile_size
                rect = pygame.Rect(x, y, 40, 40)  # Store world position in rects
                rects.append(rect)  # Store for collision detection
                # Apply camera offset when drawing
                pygame.draw.rect(screen, color, 
                                 (rect.x - camera_x, rect.y - camera_y, rect.width, rect.height), 2)
def _enemy_collisions():
    for enemy in enemies:
     if player.player_rect.colliderect(enemy.detect_player): 
          enemy._attack_mode()    
     if player.player_rect.colliderect(enemy.rect):
        if player.attacking:
          print("collision detected!!!!!!!")
          enemy._knockback_()
          enemy._enemy_hurt()
        if player.uppercut:
          print("enemy uppercutted!!!")
          enemy._launched_()
          enemy._enemy_hurt()

          
def _web_swing():
    if player.swinging and player.jumping:
        pygame.draw.line(screen, WHITE, (player.rect.x - camera_x, player.rect.y - camera_y), (player.rect.x - camera_x + 3,50), 3)
        #player.vely += 1.5  # Apply gravity while swinging 
        # 
def grapple():
    if player.shooting and enemies:
        closest_enemy = min(enemies, key=lambda enemy: abs(player.rect.x - enemy.rect.x))
        distance = abs(player.rect.x - enemy.rect.x)  # Correct distance calculation

        web_length = 600  # Length of the web
        # Start from the player's right side
        start_x = player.rect.right - camera_x
        start_y = player.rect.centery - camera_y
        end_x = closest_enemy.rect.centerx - camera_x
        end_y = closest_enemy.rect.centery - camera_y

        if closest_enemy.rect.x > player.rect.x:  # Enemy is to the right
            closest_enemy._yanked_left()
        else:
           closest_enemy._yanked_right()
        
        #else:  # Enemy is to the left
        #    end_x = start_x - distance  # Move web left
        #    end_y = start_y
        #    enemy._yanked_right()
        
        # Draw the web
        pygame.draw.line(screen, WHITE, (start_x, start_y), (end_x, end_y), 3)

def _camera_scroll():
    global camera_x
    camera_x = player.rect.x - (800 // 2) + (player.rect.width // 2)  # Center the player
    #elif player.idle:
    #camera_x = camera_x
while running:
    # Handle events first
    for event in pygame.event.get():
        player._web_zip(event,rects,camera_x,d)
        if event.type == pygame.QUIT:
            running = False
    # Move the camera BEFORE updating player movement
    _camera_scroll()
    _enemy_collisions()
  
    # Move the player after camera has updated
    player._update_movement(rects)
    
 
    for enemy in enemies:
      enemy._update_movements(rects)
      enemy._update_sprites()

    
    screen.fill("lightblue")  # Clear screen

    create_map(screen, tile_map, tile_image, tile_size)  # Draw world

    screen.blit(player.resized_image, (player.rect.x - camera_x, player.rect.y))
    for enemy in enemies:
      screen.blit(enemy.resized_enemy_image, (enemy.rect.x - camera_x, enemy.rect.y))

    d.draw(camera_x)

   # camera._draw_camera(rects)  # Draw any camera-related effects
    _draw_collisions(tile_map)
    # Draw the enemy rect with the camera offset
    #for enemy in enemies:
      #pygame.draw.rect(screen, (0, 0, 0), (enemy.Enemy_rect.x - camera_x, enemy.Enemy_rect.y, enemy.Enemy_rect.width, enemy.Enemy_rect.height), 2)
      #pygame.draw.rect(screen , (0,0,0) , (enemy.detect_player.x - camera_x,enemy.detect_player.y, enemy.detect_player.width , enemy.detect_player.height), 2)
     

    pygame.draw.rect(screen, (0, 0, 0), (player.player_rect.x - camera_x, player.player_rect.y, player.player_rect.width, player.player_rect.height), 2)
    _web_swing()
    grapple()
    if player.web_active:
        pygame.draw.line(screen,"white",(player.player_rect.centerx - camera_x, player.player_rect.centery - camera_y),(player.web_end[0] - camera_x, player.web_end[1]),3)


    for enemy in enemies:
      enemy._check_health()
      
    if len(enemies) < 1:
       print("ALL ENEMIES DEFEATED!!!")

    _draw_health_bar()
    # Refresh the screen
    pygame.display.flip()
    clock.tick(60)  # Keep frame rate at 60 FPS

pygame.quit()

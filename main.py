import pygame
from player import Player
from camera import Camera
from NewYork import create_map
from Enemies import Enemy
from camera_lock import CameraLock  # Import camera system
tile_image = pygame.image.load("images/Sprites/Level Design/Ground.png")
tile_size = 10
WHITE = (255, 255, 255)
tile_map = [
    [0] * 200, [1] * 150, 
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 1],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 1],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 1],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 1],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 ,0 , 0],
    [1] * 200
]
#pygame setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
color = (255,0,0)
player = Player()
enemy = Enemy()
camera = Camera( player.player_rect, screen ,color)
rects = []  # Initialize the list once
camera_lock = CameraLock(600, 800)
camera_x = 0
camera_y = 0
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
    if player.player_rect.colliderect(enemy.Enemy_rect):
        if player.attacking:
          print("collision detected!!!!!!!")
          enemy._knockback_()
        if player.uppercut:
          print("enemy uppercutted!!!")
          enemy._launched_()
def _web_swing():
    if player.swinging and player.jumping:
        pygame.draw.line(screen, WHITE, (player.rect.x - camera_x, player.rect.y - camera_y), (player.rect.x - camera_x + 3,50), 3)
        #player.vely += 1.5  # Apply gravity while swinging 
        # 
def grapple():
     pygame.draw.line(screen, WHITE ())

def _camera_scroll():
    global camera_x
    camera_x = player.rect.x - (800 // 2) + (player.rect.width // 2)  # Center the player
    #elif player.idle:
    #camera_x = camera_x
while running:
    # Handle events first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Move the camera BEFORE updating player movement
    _camera_scroll()
    _enemy_collisions()
    # Move the player after camera has updated
    player._update_movement(rects)
    enemy._update_movements(rects)
    enemy._update_sprites()
    # Draw everything AFTER updates
    screen.fill("lightblue")  # Clear screen
    create_map(screen, tile_map, tile_image, tile_size)  # Draw world
    screen.blit(player.resized_image, (player.rect.x - camera_x, player.rect.y))
    screen.blit(enemy.resized_enemy_image, (enemy.rect.x - camera_x, enemy.rect.y))    
   # camera._draw_camera(rects)  # Draw any camera-related effects
    _draw_collisions(tile_map)
    # Draw the enemy rect with the camera offset
    pygame.draw.rect(screen, (0, 0, 0), (enemy.Enemy_rect.x - camera_x, enemy.Enemy_rect.y, enemy.Enemy_rect.width, enemy.Enemy_rect.height), 2)
    pygame.draw.rect(screen, (0, 0, 0), (player.player_rect.x - camera_x, player.player_rect.y, player.player_rect.width, player.player_rect.height), 2)
    _web_swing()
   
    # Refresh the screen
    pygame.display.flip()
    clock.tick(60)  # Keep frame rate at 60 FPS

pygame.quit()

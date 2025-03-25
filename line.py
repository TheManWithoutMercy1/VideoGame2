import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Line Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(WHITE)
    
    # Draw a red line from (50, 50) to (450, 450) with a width of 5 pixels
    pygame.draw.line(screen, RED, (50, 50), (450, 450), 5)
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

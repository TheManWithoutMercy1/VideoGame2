import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH,HEIGHT])

fps = 60

timer = pygame.time.Clock()
wall_thickness = 10
gravity = 0.5
bounce_stop = 0.3
mouse_trajectory = []




class Ball:
    def __init__(self, x_pos, y_pos, radius , color, mass , retention, y_speed, x_speed, id):
           self.x_pos = x_pos
           self.y_pos = y_pos
           self.radius = radius
           self.color = color
           self.mass = mass
           self.retention = retention
           self.y_speed = y_speed
           self.x_speed = x_speed
           self.id = id
           self.selected = False


    def draw(self):
         self.circle = pygame.draw.circle(screen,self.color, [self.x_pos, self.y_pos ], self.radius)

    def check_gravity(self):
        if not self.selected:
          if self.y_pos < HEIGHT - self.radius - (wall_thickness/2):
              self.y_speed += gravity
          else:
            if self.y_speed > bounce_stop:
             self.y_speed = self.y_speed *-1 * self.retention
            else:
               if abs(self.y_speed) <= bounce_stop:
                   self.y_speed = 0
        else:
            self.x_speed = 0
            self.y_speed = 0
        return self.y_speed
    
    def update_pos(self,mouse):
        if not self.selected:
         self.y_pos += self.y_speed
         self.x_pos += self.x_speed
        else:
          self.x_pos = mouse[0]
          self.y_pos = mouse[1]

    def check_select(self, pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True

        return self.selected

#game variables
def draw_walls():
    left = pygame.draw.line(screen, 'white', (0,0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (WIDTH,0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0,0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0,HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left,right,top,bottom]
    return wall_list
    
ball1 = Ball(50,50,30,'blue',100,0.9,0,0,1)
ball2 = Ball(500,500,50,'green',300,.8,0,0,2)
balls = [ball1,ball2]

#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    mouse_coords = pygame.mouse.get_pos()
    mouse_trajectory.append(mouse_coords)
    if len(mouse_trajectory) > 20:
        mouse_trajectory.pop(0)
    x_push,y_push = calc_motion_vector()

    walls = draw_walls()
    ball1.draw()
    ball2.draw()
    ball1.update_pos(mouse_coords)
    ball2.update_pos(mouse_coords)
    ball1.y_speed = ball1.check_gravity()
    ball2.y_speed =ball2.check_gravity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
              if ball1.check_select(event.pos) or ball2.check_select(event.pos):
                  active_select = True
        if event.type == pygame.MOUSEBUTTONUP:
              if event.button == 1:
                  active_select = False
                  for i in range(len(balls)):
                      balls[i].check_select((-1000,-1000))

    

    pygame.display.flip()
pygame.quit()
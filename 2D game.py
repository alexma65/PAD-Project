# import pygame
import pygame

# initialize game engine
pygame.init()

window_width=1600
window_height=1159

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Hello World")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("dims.jpg").convert()

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)

    keys = pygame.key.get_pressed()

    #Keys
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_width:
        x += speed
    if keys[pygame.K_UP] and y > speed:
        y -= speed
    if keys[pygame.K_DOWN] and y < window_height:
        y += speed
    screen.fill((0,0,0))
    
    
    """
    # import pygame
import pygame

# initialize game engine
pygame.init()

window_width=800
window_height=600

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("2D_Game")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("dims.jpg").convert()

x = 10
y = 10
width = 20
height = 30
speed = 10

#Creat a player
class Player:
    x = 10
    y = 10
    width = 20
    height = 30
    speed = 10

while(dead==False):
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)
    pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    pygame.display.update()

    #keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_width:
        x += speed
    if keys[pygame.K_UP] and y > speed:
        y -= speed
    if keys[pygame.K_DOWN] and y < window_height:
        y += speed
    screen.fill((0,0,0))

pygame.quit()
    """
    

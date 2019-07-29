
# import pygame
import pygame

# initialize game engine
pygame.init()

window_width=800
window_height=600

ALPHA=(0,0,0)

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("2D_Game")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("C:/users/zsb20/PycharmProjects/projecto/images/dims.jpg").convert()


class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.movex = 0
            self.movey = 0
            self.frame = 0
            self.images = []
            img = pygame.image.load('C:/Users/zsb20/PycharmProjects/projecto/images/astro1.png').convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)

while(not dead):
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)
    player_list.draw(screen)



    pygame.display.update()
    #keys
    keys = pygame.key.get_pressed()
    #
    if keys[pygame.K_LEFT]: player.rect.x -= 10
    if keys[pygame.K_RIGHT]: player.rect.x += 10
    if keys[pygame.K_UP]: player.rect.y -=10
    if keys[pygame.K_DOWN]: player.rect.y +=10
    screen.fill((0,0,0))

pygame.quit()

    

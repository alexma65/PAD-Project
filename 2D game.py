
# import pygame
import pygame
import random
import os
import sys

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
            self.health = 10
            self.images = []
            img = pygame.image.load('C:/Users/zsb20/PycharmProjects/projecto/images/astro1.png').convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:/Users/zsb20/PycharmProjects/projecto/images/enemy1.png').convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        distance = 80
        speed = random.randint(-10,20)

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0
        self.counter += 1

player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)

enemy_list = pygame.sprite.Group()
for i in range(5):
    enemy   = Enemy(20,100*(i+1))

    enemy_list.add(enemy)


def checkCollision(player, enemy):
    col = pygame.sprite.collide_rect(player, enemy)
    if col == True:
        sys.exit()

while(not dead):
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)
    player_list.draw(screen)
    enemy_list.draw(screen)
    for e in enemy_list:
        e.move()
        checkCollision(player,e)




    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.rect.x -= 5
    if keys[pygame.K_RIGHT]: player.rect.x += 5
    if keys[pygame.K_UP]: player.rect.y -= 5
    if keys[pygame.K_DOWN]: player.rect.y += 5
    screen.fill((0,0,0))

pygame.quit()

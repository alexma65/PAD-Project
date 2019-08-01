
# import pygame
import pygame
import random
import os
import sys
import time
from pygame.locals import *
# initialize game engine
pygame.init()

window_width=800
window_height=600

ALPHA=(0,0,0)



animation_increment=10
clock_tick_rate=60

clock = pygame.time.Clock()
seconds = 0
milliseconds = 0

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("2D_Game")

dead=False


background_image = pygame.image.load("C:/users/zsb20/PycharmProjects/projecto/images/dims.jpg").convert()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

#Start Screen
def game_intro():
    intro = True
    while intro:

        screen.fill((0,0,0))
        message_display("GLACTIC SURVIVOR")
        message_display2("Press Any Key To Start")
        message_display3("Press ESC To Exit")
        message_display4("Press P To Stop")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                intro = False
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window_width/2),(window_height/2))
    screen.blit(TextSurf,TextRect)

def message_display2(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window_width/2),(window_height/1.7))
    screen.blit(TextSurf,TextRect)

def message_display3(text):
    largeText = pygame.font.Font('freesansbold.ttf', 15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window_width/2),(window_height/1.2))
    screen.blit(TextSurf,TextRect)
def message_display4(text):
    largeText = pygame.font.Font('freesansbold.ttf', 15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window_width/2),(window_height/1.05))
    screen.blit(TextSurf,TextRect)


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

class Gold(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:/Users/zsb20/PycharmProjects/projecto/images/gold.png').convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)

gold = Gold(50,50)
gold_list = pygame.sprite.Group()
gold_list.add(gold)

enemy_list = pygame.sprite.Group()
for i in range(10):
    enemy   = Enemy(20,55*(i+1))

    enemy_list.add(enemy)
score = 0
def checkCollision1(player, gold):
    col1 = pygame.sprite.collide_rect(player, gold)
    if col1 == True:
        score += 1
        a= random.randint(0,700)
        b= random.randint(0,500)
        gold_list.pop()
        for i in range(1):

            gold = Gold(a,b)
            gold_list.add(gold)



def checkCollision(player, enemy):
    col = pygame.sprite.collide_rect(player, enemy)
    if col == True:
        sys.exit()

font = pygame.font.SysFont("comicsansms", 28)

game_intro()
start_time = pygame.time.get_ticks()
pause = True
while(not dead):

    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        if event.type == KEYUP:
            if event.key == K_p:
                pause = False
        while pause == False:
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_p:
                        pause = True
    screen.blit(background_image, [0, 0])


    pygame.display.flip()
    clock.tick(clock_tick_rate)
    gold_list.draw(screen)
    player_list.draw(screen)
    enemy_list.draw(screen)

    if pygame.sprite.collide_rect(player, gold):
        a = random.randint(0, 700)
        b = random.randint(0, 500)
        gold_list.remove(gold)
        gold = Gold(a, b)
        gold_list.add(gold)
        score += 1
    text = font.render("Score: " + str(score), True, (255, 255, 255))


    screen.blit(text, (600, 0))
    for e in enemy_list:
        e.move()
        checkCollision(player,e)

    current_time = pygame.time.get_ticks()
    time_elapsed = (current_time - start_time) / 1000
    timer = font.render("Time " + str(time_elapsed), True, (255, 255, 255))

    screen.blit(timer, (4, 550))

    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5

    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    if keys[pygame.K_UP]: player.rect.y -= 5
    if keys[pygame.K_DOWN]: player.rect.y += 5
    screen.fill((0,0,0))





pygame.quit()

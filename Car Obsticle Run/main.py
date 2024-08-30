import pygame # In command prompt type "pip install pygame" before executing
import random # In command prompt type "pip install random" before executing
import math # In command prompt type "pip install math" before executing

# Initialize Pygame
pygame.init()
# dodged
dodged_val = 0
font = pygame.font.Font('freesansbold.ttf',23)
textX = 10
textY = 10

# Creating Screen
screen = pygame.display.set_mode((300, 650))
# Title and Icon
pygame.display.set_caption("Car obstacle run")
icon = pygame.image.load("D:\Pranav\class python\Car Obsticle Run\sports-car.png")
pygame.display.set_icon(icon)
# Lane
Lane = pygame.image.load("D:\Pranav\class python\Car Obsticle Run\lane.png")
# Player
playerImg = pygame.image.load("D:\Pranav\class python\Car Obsticle Run\ourcar.png")
playerX = 118
playerX_change = 0
# Enemy
enemyImg = pygame.image.load('D:\Pranav\class python\Car Obsticle Run\opcar.png')
enemyX = random.randint(-25, 200)
enemyY = -32
enemyY_change = 3
# Over text
over_font = pygame.font.Font('freesansbold.ttf',43)
def player(x):
    screen.blit(playerImg, (x, 500))
def opcar(x,y):
    screen.blit(enemyImg, (x,y))
def isCollision(EX,EY,PX,PY):
    distance = math.sqrt((math.pow(EX-PX, 2)) + (math.pow(EY-PY, 2)))
    if distance < 65:
        return True
    else:
        return False
def gameover():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text, (20, 250))
def show_score(x,y):
    score = font.render("Score : "+ str(dodged_val),True,(0,255,0))
    screen.blit(score, (x, y))
collision = isCollision(enemyX, enemyY, playerX, 500)
# Game loop
running = True
while running:
# RGB - Red, Green, Blue
    screen.fill((64, 64, 64))
# Lane on screen
    screen.blit(Lane, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= -25:
        playerX = -25
    elif playerX >= 200:
        playerX = 200
    if collision == True:
         gameover()
    else:
        enemyY += enemyY_change
        opcar(enemyX,enemyY)
        if enemyY >= 682:
            enemyX = random.randint(-25, 200)
            enemyY = -32
            opcar(enemyX, enemyY)
            dodged_val += 1
        collision = isCollision(enemyX, enemyY, playerX, 500)
    player(playerX)
    show_score(textX,textY)
    pygame.display.update()

# cargame.py
import pygame
import random

# get image
background = pygame.image.load("background.jpg")


tileandparent = {(0, 0): None}


def findpath(target_tile):
    path = []  # tracks the tiles we need to follow
    current_tile = target_tile
    while current_tile is not None:
        path.append(current_tile)
        current_tile = tileandparent[current_tile]  # what is your parent
    return path


screenwidth = 600
screenheight = 600
# creating game screen
gamescreen = pygame.display.set_mode((screenwidth, screenheight))

# car details
carwidth = 300
carheight = 300
carpositionx = screenwidth / 2
carpositiony = 700
# enemy details
enemy1_positionx = screenwidth / 2  # center
enemy1_positiony = 10  # near the top
enemy_speed = 0.09


# forever block
while True:
    # move enemies
    enemy1_positiony += 0.3
    if enemy1_positiony > 800:
        enemy1_positiony = 0
        chosen_number = random.randint(0, screenwidth)  # new
        enemy1_positionx = chosen_number  # new

    # LETS DETECT WHEN WE HIT THE ENEMY
    # STEP 1: GET THE PLAYER AND ENEMY RECTANGLES
    enemy_rectangle = pygame.Rect(enemy1_positionx, enemy1_positiony, 50, 50)
    player_rectangle = pygame.Rect(carpositionx, carpositiony, carwidth, carheight)
    # STEP2: CHECK IF PLAYER TOUCHES ENEMY
    if player_rectangle.colliderect(enemy_rectangle):
        exit()  # stop the game

    gamescreen.fill((0, 200, 0))
    gamescreen.blit(background, (0, 0))
    # draw enemies
    pygame.draw.rect(
        gamescreen,
        (50, 50, 50),
        pygame.Rect(enemy1_positionx, enemy1_positiony, 50, 50),
    )

    pygame.draw.rect(
        gamescreen,
        (100, 0, 0),
        pygame.Rect(carpositionx, carpositiony, carwidth, carheight),
    )

    pygame.display.flip()  # tells pygame we are done drawing
    buttons = pygame.event.get()  # ask for all buttons
    for button in buttons:
        if button.type == pygame.QUIT:
            exit()  # stop game

    buttons = pygame.key.get_pressed()
    if buttons[pygame.K_a] and carpositionx > 0:
        # move the vehicle left
        carpositionx -= 2

    if buttons[pygame.K_d] and carpositionx + carwidth < screenwidth:
        # move the vehicle left
        carpositionx += 2

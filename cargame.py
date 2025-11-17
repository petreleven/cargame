# cargame.py
import pygame
import random

# get image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (600, 600))
background_y = 0  # keep track of where the bg is at
background2_y = -600  # keep track of where the bg is at


# get our car image
mycar = pygame.image.load("car.png")  # new


tileandparent = {(0, 0): None}


screenwidth = 600
screenheight = 600
# creating game screen
gamescreen = pygame.display.set_mode((screenwidth, screenheight))

# car details
carwidth = 50
carheight = 50
carpositionx = screenwidth / 2
carpositiony = 500
# enemy details
enemy1_positionx = screenwidth / 2  # center
enemy1_positiony = 10  # near the top
enemy_speed = 0.09


# adding sounds
pygame.mixer.init()  # prepares our game to load some sounds
#background_music = pygame.mixer.music.load("the sound we will download")
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play()


# forever block
while True:
    background_y += 0.7
    background2_y += 0.7

    if background_y > 600:
        background_y = -600
    if background2_y > 600:
        background2_y = -600

    # move enemies
    enemy1_positiony += 0.7
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
    gamescreen.blit(background, (0, background_y))
    gamescreen.blit(background, (0, background2_y))
    gamescreen.blit(mycar, (carpositionx, carpositiony))
    gamescreen.blit(mycar, (0, enemy1_positiony))
    pygame.draw.rect(
        gamescreen,
        (100, 0, 0),
        pygame.Rect(carpositionx, carpositiony, carwidth, carheight),
    )
    # draw enemies
    pygame.draw.rect(
        gamescreen,
        (50, 50, 50),
        pygame.Rect(enemy1_positionx, enemy1_positiony, 50, 50),
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

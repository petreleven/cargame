# space.py
import pygame

width = 600
height = 400

gamescreen = pygame.display.set_mode((width, height))

# ship details
ship_positionx = 300
ship_rectangle = pygame.Rect(300, 380, 50, 150)


# forever block  using(while loop)
while True:
    #move ship
    buttons = pygame.key.get_pressed()
    #have we pressed letter A for left?
    if buttons[pygame.K_a]:
        ship_rectangle.centerx -= 2
    # have we pressed letter D for right?
    if buttons[pygame.K_d]:
        ship_rectangle.centerx += 2


    #draw items
    gamescreen.fill((20, 20, 20))  # grey for space
    pygame.draw.rect(gamescreen, (200,0,0), ship_rectangle)


    buttons = pygame.event.get()
    for button in buttons:
        if button.type == pygame.QUIT:  # is that button the quit          #new
            exit()  # exit the game                    #new



    # tell pygame we are done drawing
    pygame.display.flip()

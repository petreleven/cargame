#space.py
import pygame

width = 600
height = 400

gamescreen =pygame.display.set_mode((width,height))

#forever block  using(while loop)
while True:
    buttons = pygame.event.get()
    for button in buttons:
        if button.type == pygame.KEYDOWN:



    gamescreen.fill((20,20,20)) #grey for space

    #tell pygame we are done drawing
    pygame.display.flip()





#space.py
import pygame

width = 600
height = 400

gamescreen =pygame.display.set_mode((width,height))

#ship details
ship_positionx =  300
ship_rectangle = pygame.Rect(300, 380, width=50, height=50)




#forever block  using(while loop)
while True:
    buttons = pygame.event.get()
    for button in buttons:
        if button.key == pygame.QUIT: #is that button the quit          #new
            exit()                    #exit the game                    #new



    gamescreen.fill((20,20,20)) #grey for space

    #tell pygame we are done drawing
    pygame.display.flip()





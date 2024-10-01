import pygame 
from sys import exit

# starts the pygame module 

#pygame.init is the opposite for pygame.quit

pygame.init()
# display surface - window the play will see in the end 
# set mode needs at least one arg - width and height
screen = pygame.display.set_mode((800, 400))

#creating a new surface 
# test_surface = pygame.Surface((100,200))


#creating a font (fonttype, fontsize)
test_font = pygame.font.Font(None, 50)


# adding color to surface 
# test_surface.fill('Red')

new_surface = pygame.image.load('background.jpg').convert_alpha()
# render takes 3 bits of information text, quality of text, color
text_surface = test_font.render('my game', False, "Green")

snail_surface = pygame.image.load("snail.png").convert_alpha()

#update pygame windo titltle 
pygame.display.set_caption("Runner")
# create a clock object - helps with time and frame rate 



clock  = pygame.time.Clock()

# going to run forever

#snail_xposition
snail_position_x = 600

while True:
    # draw all element and update all element

    # checking for all possible player input

    for event in pygame.event.get():
        #indidcating to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            #stops the while loop
            exit()
    #blit stands for block image transfer, we want to get the left,top position 
    screen.blit(new_surface,(200,100))

    screen.blit(text_surface,(300,50))
    # -1 moves to the left +1 moves to the right
    snail_position_x-= 4
    if snail_position_x < -100: snail_position_x = 800

    screen.blit(snail_surface,(snail_position_x,250))


    
    #updates the display surface
    pygame.display.update()
    # the clock tells the while loop not to run more than 60 seconds 
    clock.tick(60)
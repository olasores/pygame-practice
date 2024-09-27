import pygame 
from sys import exit

# starts the pygame module 

#pygame.init is the opposite for pygame.quit

pygame.init()
# display surface - window the play will see in the end 
# set mode needs at least one arg - width and height
screen = pygame.display.set_mode((800, 400))


#update pygame windo titltle 
pygame.display.set_caption("Runner")
# create a clock object - helps with time and frame rate 
clock  = pygame.time.Clock()

# going to run forever

while True:
    # draw all element and update all element

    # checking for all possible player input

    for event in pygame.event.get():
        #indidcating to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            #stops the while loop
            exit()
    #updates the display surface
    pygame.display.update()
    # the clock tells the while loop not to run more than 60 seconds 
    clock.tick(60)
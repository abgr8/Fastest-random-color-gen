import pygame
import random


WIDTH = 800
HEIGHT = 600
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Abbas Application")
clock = pygame.time.Clock()     ## For syncing the FPS


## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_6:
                randbg = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                screen.fill(randbg)
                print(randbg)
                


    #2 Update
    all_sprites.update()


    #3 Draw/render
    

    

    all_sprites.draw(screen)
    ########################

    

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()

import pygame
pygame.init()

window = pygame.display.set_mode ((600,400))

running  = True
while running :

    window.fill((100, 145, 255))
    pygame.draw.rect(window,(240, 140, 50), [100, 100, 400, 100 ], 2 )
    pygame.draw.rect(window,(0, 0,255), [270, 100, 60, 300 ], 0 )
    pygame.draw.circle(window, (150, 0, 0), [300, 50], 40, 0)
    for event in pygame.event.get() :
        if event.type  ==pygame.QUIT:
            running = False 
    pygame.display.update()   
pygame.quit()         

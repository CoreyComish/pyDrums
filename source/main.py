import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1024, 884))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load(os.path.join("img", "drums.png"))
print(bg)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(bg, (0,0)) # display drum set bg
    pygame.display.flip()
    clock.tick(60) # 60 fps
    
    

pygame.quit()
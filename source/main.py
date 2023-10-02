import pygame
import os
import drums

# Initialize, set display area, load bg
pygame.init()
screen = pygame.display.set_mode((1024, 884))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load(os.path.join("img", "drums.jpg"))

# Create drum object
drums = drums.Drums()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key down events, playing the correct drum
        if event.type == pygame.KEYDOWN:
            drums.playDrum(event.key)

    screen.blit(bg, (0,0)) # display drum set bg
    pygame.display.flip()
    clock.tick(60) # 60 fps

pygame.quit()
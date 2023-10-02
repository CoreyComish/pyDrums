import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1024, 884))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load(os.path.join("img", "drums.png"))
print(bg)

# Audio
hi_hat = pygame.mixer.Sound("./audio/Standard/hi-hat.wav")
kick = pygame.mixer.Sound("./audio/Standard/kick.wav")
snare = pygame.mixer.Sound("./audio/Standard/snare.wav")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_h]:
        pygame.mixer.Sound.play(hi_hat)
    if keys[pygame.K_s]:
        pygame.mixer.Sound.play(snare)
    if keys[pygame.K_SPACE]:
        pygame.mixer.Sound.play(kick)

    screen.blit(bg, (0,0)) # display drum set bg
    pygame.display.flip()
    clock.tick(60) # 60 fps
    
    

pygame.quit()
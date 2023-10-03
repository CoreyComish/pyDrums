import pygame
import os
import Drums
import MusicPlayer

# Initialize, set display area, load bg
pygame.init()
screen = pygame.display.set_mode((1024, 884))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load(os.path.join("img", "drums.jpg"))

# Create drum object
drums = Drums.Drums(screen)

# Create Music Player position and object
musicplayer_rect = pygame.Rect(650, 20, 200, 20)
musicplayer = MusicPlayer.MusicPlayer(screen, musicplayer_rect, 1)

# Position of last drum hit
drum_hit_pos = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key down events, playing the correct drum
        if event.type == pygame.KEYDOWN:
            drum_hit = drums.playDrum(event.key)
            if drum_hit != None:
                drum_hit_pos.append(drums.drumHitPos(drum_hit))
        

        # Check if we are clicking down on a menu item
        # If we are, handle the proper event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if musicplayer.getMusicPlayerRect().collidepoint(event.pos):
                musicplayer.loadMusic()
            if musicplayer.getPlayPauseButtonRect().collidepoint(event.pos):
                musicplayer.playPause()
            if musicplayer.getRestartButtonRect().collidepoint(event.pos):
                musicplayer.restart()

    screen.blit(bg, (0,0)) # display drum set bg
    musicplayer.drawMusicPlayerUI(screen) # display music player on screen
    
    # draw light indicator of last drum hit
    if len(drum_hit_pos) != 0:
        for hit in drum_hit_pos:
            pygame.draw.circle(screen, (0,255,0), drum_hit_pos[0], 30)
            drum_hit_pos.pop(0)
    
    pygame.display.flip()
    clock.tick(60) # 60 fps

pygame.quit()
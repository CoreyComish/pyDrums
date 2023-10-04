import pygame
import pygame_widgets
import os
import Drums
import MusicPlayer
import DrumSelector

# Initialize, set display area, load bg
pygame.init()
screen = pygame.display.set_mode((1024, 884))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load(os.path.join("img", "drums.jpg"))

# Create drum object
drums = Drums.Drums(screen)
# Draw drums volume slider UI. Using a library for this, so pygame_widgets.update gets called in the loop
drums.drawVolumeSlider(screen)

# Create Music Player position and object
musicplayer_rect = pygame.Rect(650, 20, 200, 20)
musicplayer = MusicPlayer.MusicPlayer(screen, musicplayer_rect, 1)
# Draw music volume slider UI. Using a library for this, so pygame_widgets.update gets called in the loop
musicplayer.drawVolumeSlider(screen)

# Create Drum Selector position and object
drum_selector_rect = pygame.Rect(750, 850, 225, 20)
drum_selector = DrumSelector.DrumSelector(screen, drum_selector_rect, 1)

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
            if drum_selector.getDrumSelectorRect().collidepoint(event.pos):
                new_drum_list = drum_selector.getDrums()
                if new_drum_list != None:
                    drums.loadDrums(new_drum_list)

    screen.blit(bg, (0,0)) # display drum set bg
    musicplayer.drawMusicPlayerUI(screen) # display music player on screen
    drum_selector.drawDrumSelectorUI(screen) # display drum selector on screen
    
    # draw light indicator of last drum hit
    if len(drum_hit_pos) != 0:
        for hit in drum_hit_pos:
            pygame.draw.circle(screen, (0,255,0), drum_hit_pos[0], 30)
            drum_hit_pos.pop(0)

    # Check if moved sliders for volume changes
    musicplayer.updateVolume()
    drums.updateVolume()

    pygame_widgets.update(event)
    pygame.display.flip()
    clock.tick(60) # 60 fps

pygame.quit()
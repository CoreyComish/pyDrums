import pygame
import pygame_widgets
import Drums
import MusicPlayer
import DrumSelector
import utils

# Initialize, set display area, load bg
pygame.init()
screen = pygame.display.set_mode((1024, 884))
clock = pygame.time.Clock()
running = True
root = utils.getProjectRoot()
bg = pygame.image.load(root + "/img/drums.jpg")

# Create drum UI and object
drums = Drums.Drums(screen)
drums.drawDrumUI()

# Create Music Player UI and object
musicplayer = MusicPlayer.MusicPlayer(screen)
musicplayer.drawMusicPlayerUI()

# Create Drum Selector UI and object
drum_selector = DrumSelector.DrumSelector(screen, drums)
drum_selector.drawDrumSelectorUI()

# Position of last drum hit
drum_hit_pos = []

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key down events, playing the correct drum
        if event.type == pygame.KEYDOWN:
            drum_hit = drums.playDrum(event.key)
            if drum_hit != None:
                drum_hit_pos.append(drums.drumHitPos(drum_hit))

    screen.blit(bg, (0,0)) # display drum set bg
    
    # draw light indicator of last drum hit
    if len(drum_hit_pos) != 0:
        for hit in drum_hit_pos:
            pygame.draw.circle(screen, (0,255,0), drum_hit_pos[0], 30)
            drum_hit_pos.pop(0)

    # Check if moved sliders for volume changes
    musicplayer.updateVolume()
    drums.updateVolume()

    pygame_widgets.update(event) # update UI
    pygame.display.flip()
    clock.tick(60) # 60 fps

pygame.quit()
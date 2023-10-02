# Drum Class

import pygame

pygame.mixer.init()

defaultDrums = [pygame.mixer.Sound("./audio/Standard/hi_hat.wav"), 
                pygame.mixer.Sound("./audio/Standard/kick.wav"), 
                pygame.mixer.Sound("./audio/Standard/snare.wav"), 
                pygame.mixer.Sound("./audio/Standard/hi_tom.wav"),
                pygame.mixer.Sound("./audio/Standard/md_tom.wav"), 
                pygame.mixer.Sound("./audio/Standard/fl_tom.wav"),
                pygame.mixer.Sound("./audio/Standard/ride.wav"), 
                pygame.mixer.Sound("./audio/Standard/crash.wav")]

defaultKeys = [pygame.K_h, pygame.K_SPACE, pygame.K_s, 
               pygame.K_q, pygame.K_w, pygame.K_e,
               pygame.K_y, pygame.K_u]

class Drums:

    def __init__(self):
        self.sounds = defaultDrums
        self.drumsToKeys = defaultKeys
        self.hi_hat = self.sounds[0]
        self.kick = self.sounds[1]
        self.snare = self.sounds[2]
        self.hi_tom = self.sounds[3]
        self.md_tom = self.sounds[4]
        self.fl_tom = self.sounds[5]
        self.ride = self.sounds[6]
        self.crash = self.sounds[7]

    # Plays the drum sound, given the key press
    # This has a dependency on the fact the drum sounds are loaded in the correct order (see init)
    def playDrum(self, keypress):
        try:
            idx = self.drumsToKeys.index(keypress)
            pygame.mixer.Channel(idx).play(pygame.mixer.Sound(self.sounds[idx]))
        except:
            pass

    # Used to load different sounds into the drum kit
    def loadDrum(self, drumList):
        if len(drumList) == len(self.sounds):
            self.sounds = drumList
        else:
            quit
            
        
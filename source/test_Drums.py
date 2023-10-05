from Drums import Drums
import pygame

screen = 1 # dummy screen
drums = Drums(screen)

correct_drum_list = ["./audio/Standard/hi_hat.wav", 
                "./audio/Standard/kick.wav", 
                "./audio/Standard/snare.wav", 
                "./audio/Standard/hi_tom.wav",
                "./audio/Standard/md_tom.wav", 
                "./audio/Standard/fl_tom.wav",
                "./audio/Standard/ride.wav", 
                "./audio/Standard/crash.wav"]

missing_drum_list = ["./audio/Standard/hi_hat.wav", 
                "./audio/Standard/kick.wav", 
                None, 
                "./audio/Standard/hi_tom.wav",
                "./audio/Standard/md_tom.wav", 
                "./audio/Standard/fl_tom.wav",
                "./audio/Standard/ride.wav", 
                "./audio/Standard/crash.wav"]

duplicate_drum_list = ["./audio/Standard/hi_hat.wav", 
                "./audio/Standard/kick.wav", 
                "./audio/Standard/hi_hat.wav", 
                "./audio/Standard/hi_tom.wav",
                "./audio/Standard/md_tom.wav", 
                "./audio/Standard/fl_tom.wav",
                "./audio/Standard/ride.wav", 
                "./audio/Standard/crash.wav"]

def test_load_drums():
    drums.loadDrums(['hi_hat.wav']) == None # only one drum
    drums.loadDrums(['hi_hat.wav' * 7]) == None # one to few drums
    drums.loadDrums(['hi_hat.wav' * 9]) == None # one to many drums
    drums.loadDrums(missing_drum_list) == None # one missing drum
    drums.loadDrums(duplicate_drum_list) == None # duplicate drum in drum list
    drums.loadDrums(correct_drum_list) == correct_drum_list # valid test

def test_play_drum():
    drums.playDrum(pygame.K_m) == None # invalid key
    drums.playDrum(pygame.K_h) != None # valid key
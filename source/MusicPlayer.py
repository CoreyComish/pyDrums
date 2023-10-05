# Music Player UI and Class

# todo: build clean UI

import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import tkinter
from tkinter import filedialog

class MusicPlayer:

    def __init__(self, display):
        self.display = display
        self.music_file_path = None
        self.slider = None

    def getAudioFilePath(self):
        file_path = filedialog.askopenfile()
        if file_path != None and file_path.name[-4:] == ".mp3":
            return file_path
        else:
            return None
    
    def getVolumeSliderVal(self):
        return self.slider.getValue()
    
    def loadMusic(self):
        self.music_file_path = self.getAudioFilePath()
        if self.music_file_path != None:
            pygame.mixer.music.load(self.music_file_path)
            pygame.mixer.music.play(loops=-1)
        else:
            exit

    def playPause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def restart(self):
        if self.music_file_path != None:
            pygame.mixer.music.rewind()
        else:
            exit
        
    def drawMusicPlayerUI(self):
        load_song_button = Button(self.display, 650, 20, 100, 20, hoverColor=(150,0,0), radius=6, 
                                  text="Load .mp3", onClick=lambda: self.loadMusic())
        playpause_button = Button(self.display, load_song_button._x + 115, load_song_button._y,
                                  load_song_button._width, load_song_button._height,
                                  hoverColor=load_song_button.hoverColour, radius=load_song_button.radius, 
                                  text="Play/Pause", onClick=lambda: self.playPause())
        restart_button = Button(self.display, load_song_button._x + 230, load_song_button._y,
                                  load_song_button._width, load_song_button._height,
                                  hoverColor=load_song_button.hoverColour, radius=load_song_button.radius, 
                                  text="Restart", onClick=lambda: self.restart())
        self.drawVolumeSlider()

    def drawVolumeSlider(self):
        sliderLabel = TextBox(self.display, 100, 810, 20, 20, colour=(255,255,255), 
                              borderColour=(255,255,255))
        sliderLabel.setText("Music Volume")
        sliderLabel.disable()
        slider = Slider(self.display, 50, 825, 200, 10, min=0.0, max=1.0, step=0.05)
        self.slider = slider
    
    def updateVolume(self):
        if (pygame.mixer.music.get_volume() != self.getVolumeSliderVal()):
            pygame.mixer.music.set_volume(self.getVolumeSliderVal())
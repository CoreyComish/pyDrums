# Music Player UI and Class

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
        self.load_song_button = None
        self.playpause_button = None
        self.restart_button = None

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
            self.song_status_text.setText("Playing: " + str(self.music_file_path.name))
        else:
            exit

    def playPause(self):
        if self.music_file_path != None:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                self.drawPlayPauseButton(False)
                self.song_status_text.setText("Paused: " + str(self.music_file_path.name))
            else:
                pygame.mixer.music.unpause()
                self.drawPlayPauseButton(True)
                self.song_status_text.setText("Playing: " + str(self.music_file_path.name))

    def restart(self):
        if self.music_file_path != None:
            pygame.mixer.music.rewind()
        else:
            exit

    def drawLoadSongButton(self):
        self.load_song_button = Button(self.display, 650, 20, 100, 20, hoverColor=(150,0,0), radius=6, 
                                  text="Load .mp3", onClick=lambda: self.loadMusic())

    def drawPlayPauseButton(self, isPlaying):
        if isPlaying:
            buttonText = "Pause"
        else:
            buttonText = "Play"
        self.playpause_button = Button(self.display, self.load_song_button._x + 115, self.load_song_button._y,
                                  self.load_song_button._width, self.load_song_button._height,
                                  hoverColor=self.load_song_button.hoverColour, radius=self.load_song_button.radius, 
                                  text=buttonText, onClick=lambda: self.playPause())
    
    def drawRestartButton(self):
        self.restart_button = Button(self.display, self.load_song_button._x + 230, self.load_song_button._y,
                                  self.load_song_button._width, self.load_song_button._height,
                                  hoverColor=self.load_song_button.hoverColour, radius=self.load_song_button.radius, 
                                  text="Restart", onClick=lambda: self.restart())
        
    def drawSongPlaying(self):
        self.song_status_text = TextBox(self.display, 20, 20, 625, 20, colour=(255,255,255), 
                              borderColour=(255,255,255), fontSize=25)
        self.song_status_text.disable()

    def drawMusicPlayerUI(self):
        self.drawLoadSongButton()
        self.drawRestartButton()
        self.drawPlayPauseButton(True)
        self.drawVolumeSlider()
        self.drawSongPlaying()

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
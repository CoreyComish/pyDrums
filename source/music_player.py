# Music Player UI and Class

# todo: build clean UI

import pygame
import tkinter
from tkinter import filedialog

class MusicPlayer:

    def __init__(self, display, rect, color):
        self.display = display
        self.music_player_rect = rect
        self.color = color

        self.play_pause_button_rect = None
        self.restart_button_rect = None

        self.music_file_path = None

    def getAudioFilePath(self):
        file_path = filedialog.askopenfile()
        if file_path.name[-4:] == ".mp3":
            return file_path
        else:
            return None
    
    def getMusicPlayerRect(self):
        return self.music_player_rect
    
    def getPlayPauseButtonRect(self):
        return self.play_pause_button_rect
    
    def getRestartButtonRect(self):
        return self.restart_button_rect
    
    def loadMusic(self):
        self.music_file_path = self.getAudioFilePath()
        if self.music_file_path != None:
            pygame.mixer.music.load(self.music_file_path)
            pygame.mixer.music.play()
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
    
    def drawMusicPlayer(self):
        self.music_player_rect = pygame.draw.rect(self.display, self.color, self.music_player_rect)

    def drawPlayPauseButton(self):
        rect = (self.music_player_rect.left + self.music_player_rect.width + 10, 
                self.music_player_rect.top, 20, 20)
        self.play_pause_button_rect = pygame.draw.rect(self.display, self.color, rect)

    def drawRestartButton(self):
        rect = (self.music_player_rect.left + self.music_player_rect.width + 40, 
                self.music_player_rect.top, 20, 20)
        self.restart_button_rect = pygame.draw.rect(self.display, self.color, rect)
    
    # temp ui
    def drawMusicPlayerUI(self, display):
        self.drawMusicPlayer()
        self.drawPlayPauseButton()
        self.drawRestartButton()
        

    
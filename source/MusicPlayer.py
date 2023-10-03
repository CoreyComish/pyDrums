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

        self.font = pygame.font.SysFont('Arial', 15)

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
    
    def drawMusicPlayer(self, display):
        self.music_player_rect = pygame.draw.rect(self.display, self.color, self.music_player_rect)
        if self.music_file_path != None:
            if pygame.mixer.music.get_busy():
                status_string = "Playing: "
            else:
                status_string = "Paused: "
            display.blit(self.font.render(status_string + str(self.music_file_path.name), True, (255,0,0)), 
                         (10, 10))
        display.blit(self.font.render("Click to load a .mp3 file", True, (255,0,0)), 
                (self.music_player_rect.left + 5, self.music_player_rect.top + 2))

    def drawPlayPauseButton(self, display):
        rect = (self.music_player_rect.left + self.music_player_rect.width + 10, 
                self.music_player_rect.top, 60, 30)
        self.play_pause_button_rect = pygame.draw.rect(self.display, self.color, rect)
        if pygame.mixer.music.get_busy():
            action_string = "Pause"
        else:
            action_string = "Play"
        display.blit(self.font.render(action_string, True, (255,0,0)), 
                (self.play_pause_button_rect.left + 5, self.play_pause_button_rect.top + 5))

    def drawRestartButton(self, display):
        rect = (self.music_player_rect.left + self.music_player_rect.width + 80, 
                self.music_player_rect.top, 60, 30)
        self.restart_button_rect = pygame.draw.rect(self.display, self.color, rect)
        display.blit(self.font.render("Restart", True, (255,0,0)), 
                (self.restart_button_rect.left + 5, self.restart_button_rect.top + 5))
    
    # temp ui
    def drawMusicPlayerUI(self, display):
        self.drawMusicPlayer(display)
        self.drawPlayPauseButton(display)
        self.drawRestartButton(display)
        

    
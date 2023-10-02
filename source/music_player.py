# Music Player UI and Class

# todo: play/pause button, restart button, rewind/ff button, cleaner ui

import pygame
import tkinter
from tkinter import filedialog

class MusicPlayer:

    def __init__(self, rect, color):
        self.rect = rect
        self.color = color
    
    # todo: file checking/validation and proper handling
    def getAudioFilePath(self):
        file_path = filedialog.askopenfile()
        return file_path
    
    def getButtonRect(self):
        return self.rect
    
    # temp ui
    def drawMusicPlayerUI(self, display):
        self.rect = pygame.draw.rect(display, self.color, self.rect)
# Drum Selector Class
# Handles user selecting different drum kits and UI

import pygame
import tkinter
from tkinter import filedialog
import os

class DrumSelector:

    def __init__(self, display, rect, color):
        self.display = display
        self.drum_select_rect = rect
        self.color = color
        self.folder_path = None

        self.font = pygame.font.SysFont('Arial', 15)

    def getDrumSelectorRect(self):
        return self.drum_select_rect

    def getDrumFolderPath(self):
        self.folder_path = filedialog.askdirectory()
        return self.folder_path
    
    def getDrums(self):
        new_drum_list = []
        folder_path = self.getDrumFolderPath()
        for filename in os.listdir(folder_path):
            file = os.path.join(folder_path, filename)
            new_drum_list.append(file)
        if len(new_drum_list) == 8:
            return new_drum_list
        else:
            return None
    
    def drawDrumSelector(self, display):
        pygame.draw.rect(self.display, self.color, self.drum_select_rect)
        display.blit(self.font.render("Click to load another drum set", True, (255,0,0)), 
                (self.drum_select_rect.left + 5, self.drum_select_rect.top + 2))

    def drawDrumSelectorUI(self, display):
        self.drawDrumSelector(display)
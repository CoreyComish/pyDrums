# Drum Selector Class
# Handles user selecting different drum kits and UI

import pygame
import pygame_widgets
from pygame_widgets.button import Button
import tkinter
from tkinter import filedialog
import os

class DrumSelector:

    def __init__(self, display, drums):
        self.display = display
        self.folder_path = None
        self.drums = drums

    def getDrumFolderPath(self):
        self.folder_path = filedialog.askdirectory()
        return self.folder_path
    
    def getDrums(self):
        new_drum_list = []
        folder_path = self.getDrumFolderPath()
        if len(folder_path) != 0:
            for filename in os.listdir(folder_path):
                file = os.path.join(folder_path, filename)
                new_drum_list.append(file)
        if len(new_drum_list) == 8:
            self.drums.loadDrums(new_drum_list)
        else:
            return None

    def drawDrumSelectorUI(self):
        drum_select_button = Button(self.display, 725, 850, 250, 20, hoverColor=(150,0,0), radius=6, 
                                  text="Change drum kits", onClick=lambda: self.getDrums())
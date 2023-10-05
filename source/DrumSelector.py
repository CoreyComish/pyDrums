# Drum Selector Class
# Handles user selecting different drum kits and UI

import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import tkinter
from tkinter import filedialog
import os

class DrumSelector:

    def __init__(self, display, drums):
        self.display = display
        self.folder_path = None
        self.drums = drums
        self.drum_select_button = None
        self.drum_kit_name_text = None

    def getDrumFolderPath(self):
        self.folder_path = filedialog.askdirectory(initialdir=os.path.join("audio"))
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
            self.drum_kit_name_text.setText("Drum Kit: " + os.path.basename(os.path.normpath(folder_path)))
        else:
            return None
        
    def drawDrumSelectButton(self):
        self.drum_select_button = Button(self.display, 725, 850, 250, 20, hoverColor=(150,0,0), radius=6, 
                                  text="Change drum kits", onClick=lambda: self.getDrums())
        self.drum_kit_name_text = TextBox(self.display, 785, 830, 250, 20, colour=(255,255,255), 
                              borderColour=(255,255,255), fontSize=20)
        self.drum_kit_name_text.setText("Drum Kit: Standard")
        self.drum_kit_name_text.disable()

    def drawDrumSelectorUI(self):
        self.drawDrumSelectButton()
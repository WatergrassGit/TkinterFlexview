import tkinter as tk
from tkinter import ttk
from . models import DataModel
from . import views as v
from . styles import StyleSheet


class Application(tk.Tk):
    """Controller for model and view."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.wm_title("Flex View")
        self.geometry("800x600")

        self.callbacks = {
            'get_text': self.get_text,
            'update_title_fontsize': self.update_title_fontsize,
        }

        self.datamodel = DataModel()

        self.stylesheet = StyleSheet()

        self.mainview = v.MainView(self, self.callbacks)
        self.mainview.grid(row=0, column=0, sticky='nsew')

        # configure columns to allow horizontal expanding and contracting of widgets in the view
        self.grid_columnconfigure(0, weight=1)

    def get_text(self):
        """Used to request text data from the model."""

        return self.datamodel.long_text
    
    def update_title_fontsize(self, width):
        """
        Used to update title font size when window changes.
        
        :arguments
        ----------
        width: int
            width of screen in pixels
        """

        self.stylesheet.update_title_fontsize(width)

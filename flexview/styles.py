import tkinter as tk
from tkinter import ttk


class StyleSheet(ttk.Style):
    """The StyleSheet class holds the styles for the application."""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Styles for mainview title widget
        self.configure('title.TLabel', font=('Helvetica', 20), background='red')

        # Styles for mainview text widget
        self.configure('text.TLabel', font=("Helvetica", 11), background='green')

        # Styles for mainview media_frame widget
        self.configure('media.TFrame', background='black')

        # Styles for widgets contained in media_frame
        self.configure('initial.TFrame', background='silver')
        self.configure('final.TFrame', background='gold')

import tkinter as tk
from tkinter import ttk


class MainView(ttk.Frame):
    """Main view for application."""

    def __init__(self, master, callbacks, *args, **kwargs):
        """
        Initialize MainView

        :arguments
        ----------
        master : tkinter object
            parent widget for MainView
        callbacks : dictionary
            contains references to callable methods in `master`
        """

        super().__init__(master, *args, **kwargs)

        self.callbacks = callbacks

        # View title
        self.title = ttk.Label(self, text="Responsive Window Design", style='title.TLabel')

        # View text
        example_text = self.callbacks['get_text']()
        self.text = ttk.Label(self, text=example_text, wraplength=300, justify='left', style='text.TLabel')

        # View frame - holds two separate frames
        self.media_frame = ttk.Frame(self, style='media.TFrame')

        # Allow horizontal expansion and contraction of objects in MainView widget
        self.grid_columnconfigure(0, weight=1)

        # Set up grid for mainview content
        self.title.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.text.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.media_frame.grid(row=2, column=0, sticky='nsew')

        # Add items to media_frame widget
        self.initial_frame = ttk.Frame(self.media_frame, style='initial.TFrame', height=200)
        self.initial_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.final_frame = ttk.Frame(self.media_frame, style='final.TFrame', height=200)
        self.final_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        # set of relative widths for media_frame contents
        self.media_frame.grid_columnconfigure(0, weight=1)
        self.media_frame.grid_columnconfigure(1, weight=2)

        # Set up events
        self.bind("<Configure>", self.responsive_page)
        self.title.bind("<Configure>", self.update_fontsize)
        self.text.bind("<Configure>", self.update_wraplength)

    def responsive_page(self, event):
        # Regular / Wide view
        if self.winfo_width() >= 600:
            self.initial_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
            self.final_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
            
            # set of relative widths for media_frame contents
            self.media_frame.grid_columnconfigure(0, weight=1)
            self.media_frame.grid_columnconfigure(1, weight=2)

        # Mobile / Thin view
        else:
            self.initial_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
            self.final_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

            # set of relative widths for media_frame contents
            self.media_frame.grid_columnconfigure(0, weight=1)
            self.media_frame.grid_columnconfigure(1, weight=0)

    def update_fontsize(self, event):
        """Update title font size based on widget width."""

        self.callbacks['update_title_fontsize'](self.winfo_width())

    def update_wraplength(self, event):
        """Update wraplength based on widget width."""

        self.text.config(wraplength=self.winfo_width()-20)

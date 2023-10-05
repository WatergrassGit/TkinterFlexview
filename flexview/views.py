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

        # ---------- Scrollable Frame Setup ---------- #
        # Create scrollable frame using canvas with adjacent vertical scrollbar
        # This requires seting up a canvas widget with the interior frame
        # attached using the .create_window method (cannot grid onto a canvas)

        # Canvas setup
        # highlightthickness = 0 is important to ensure canvas start appears at (0, 0)
        self.canvas = tk.Canvas(self, bg='red', bd=0, highlightthickness=0)
        self.v_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)

        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.v_scrollbar.grid(row=0, column=1, sticky='ns')

        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        # Interior scrollable frame setup
        self.scrollable_frame = ttk.Frame(self.canvas, style='scrollframe.TFrame')
        self.canvas_window = self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")

        # Grid configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

        # ---------- Scrollable Frame Content ---------- #
        self.title = ttk.Label(self.scrollable_frame, text="Responsive Window Design", style='title.TLabel')
        example_text = self.callbacks['get_text']()
        self.text = ttk.Label(self.scrollable_frame, text=example_text, justify='left', style='text.TLabel')
        self.media_frame = ttk.Frame(self.scrollable_frame, style='media.TFrame')

        self.title.grid(row=0, column=0, sticky='nsew')
        self.text.grid(row=1, column=0, sticky='nsew')
        self.media_frame.grid(row=2, column=0, sticky='nsew')

        self.media_frame.grid_columnconfigure(0, weight=1)
        self.media_frame.grid_columnconfigure(1, weight=2)        

        # ---------- Media Frame Content ---------- #
        self.initial_frame = ttk.Frame(self.media_frame, style='initial.TFrame', height=200)
        self.final_frame = ttk.Frame(self.media_frame, style='final.TFrame', height=200)

        self.initial_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.final_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        # ---------- Event Bindings ---------- #
        self.canvas.bind("<Configure>", self.responsive_page)

    def responsive_page(self, event):
        """
        Utilize canvas width to add responsive behavior to view.

        This includes
        * Responsive grid
        * Responsive font size
        * Responsive Label widget wraplength

        :arguments
        ----------
        event : tkinter.Event
            Collects information from a triggered event. In this case it
            includes information about canvas width.
        """

        canvas_width = event.width  # can also use self.canvas.winfo_width()

        # Adjust canvas_window width to allow scrollable frame width
        # to expand to width of canvas
        self.canvas.itemconfigure(self.canvas_window, width=canvas_width)

        # DO NOT DELETE: Required to ensure scrollbars update properly
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Adjust Grid as needed.
        if canvas_width >= 600:  # Regular / Wide view
            self.final_frame.grid(row=0, column=1)
            self.media_frame.grid_columnconfigure(1, weight=2)
        else:  # Mobile / Thin view
            self.final_frame.grid(row=1, column=0)
            self.media_frame.grid_columnconfigure(1, weight=0)

        # Update title font size based on widget width.
        self.callbacks['update_title_fontsize'](canvas_width)

        # Update wraplength based on widget width.
        self.text.config(wraplength=canvas_width)

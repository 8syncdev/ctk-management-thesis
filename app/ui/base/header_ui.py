from app.setting.setting import *
import customtkinter



class HeaderUI:
    def __init__(self, parent):
        self.parent = parent
        self.init_ui()


    def init_ui(self):
        self.wrapper = CTkFrame(self.parent.header, height=50)
        self.wrapper.pack(fill='x')
        # Left Frame
        self.left_frame = CTkFrame(self.wrapper, height=50)
        self.left_frame.pack(side='left')

        # Center Frame
        self.center_frame = CTkFrame(self.wrapper, height=50)
        self.center_frame.pack(side='left', fill='x')

        # Right Frame
        self.right_frame = CTkFrame(self.wrapper, height=50)
        self.right_frame.pack(side='right')
        self.init_right_ui()


    def init_right_ui(self):
        themes = ['system', 'light', 'dark']
        self.theme = CTkOptionMenu(self.right_frame, values=themes, command=lambda event: self.set_theme())
        self.theme.pack(side='right')
    
    def set_theme(self):
        customtkinter.set_appearance_mode(self.theme.get())



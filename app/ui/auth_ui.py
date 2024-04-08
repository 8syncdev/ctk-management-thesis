from app.setting.setting import *
from app.ui.base.base_ui import BaseUI
from app.ui.layouts.auth_ui.auth_ui import AuthUI as AuthUIScreen



class AuthUI(BaseUI):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("Auth")
        self.geometry("500x900+100+100")

        self.init_ui()

    def init_ui(self):
        super().init_ui()
        AuthUIScreen(self.body)


    

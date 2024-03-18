from app.setting.setting import *
from app.ui.base.base_ui import BaseUI



class AuthUI(BaseUI):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("Auth")
        self.geometry("500x900+100+100")

        self.init_ui()


    

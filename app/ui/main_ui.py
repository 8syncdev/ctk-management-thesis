from app.setting.setting import *
from app.ui.base.base_top_ui import BaseTopUI
from app.ui.layouts.main_ui.body_main_ui import BodyMain
from app.db.main import AccountDAO


class MainUI(BaseTopUI):

    def __init__(self, account, **kwargs):
        super().__init__(**kwargs)
        self.title("Main")
        self.geometry("1400x900+100+100")

        self.account = account

        self.init_ui()
        '''
            self.init_ui() có:
            self.header
            self.body
            self.footer
        '''
        BodyMain(self, account=self.account, role=self.account.role)




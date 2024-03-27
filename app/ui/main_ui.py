from app.setting.setting import *
from app.ui.base.base_ui import BaseUI
from app.ui.layouts.main_ui.body_main_ui import BodyMain
from app.db.main import AccountDAO


class MainUI(BaseUI):

    def __init__(self, account, role='student', **kwargs):
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
        BodyMain(self, account=self.account, role=role)




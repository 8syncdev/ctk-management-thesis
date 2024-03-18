from app.setting.setting import *
from app.ui.base.base_ui import BaseUI
from app.ui.layouts.main_ui.body_student_main import BodyMain as BodyMainStudent


class MainUI(BaseUI):

    def __init__(self, role='student', **kwargs):
        super().__init__(**kwargs)
        self.title("Main")
        self.geometry("1400x900+100+100")

        self.init_ui()
        '''
            self.init_ui() có:
            self.header
            self.body
            self.footer
        '''
        if role == 'student':
            BodyMainStudent(self)




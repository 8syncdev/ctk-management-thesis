from app.setting.setting import *


class BaseUI(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



    def init_ui(self):
        # Header 
        self.header = CTkFrame(self, height=50)
        self.header.pack(fill ='x')
        # Body
        self.body = CTkFrame(self)
        self.body.pack(fill = 'both', expand = True)

        # Footer
        self.footer = CTkFrame(self, height=50)
        self.footer.pack(fill ='x')

    def run_ui(self):
        self.mainloop()
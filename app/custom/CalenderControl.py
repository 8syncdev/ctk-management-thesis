from app.setting.setting import *
from datetime import datetime
from calendar import monthrange


class CalenderControl(CTkFrame):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.master = master
        self.pack()
        self.init_ui()


    def init_ui(self):
        self.menu_option_day = CTkOptionMenu(self, values=[str(i) for i in range(1, monthrange(2021, 1)[1] + 1)], width=10)
        self.menu_option_day.pack(side='left', padx=5)

        self.menu_option_month = CTkOptionMenu(self, values=[str(i) for i in range(1, 13)], command=lambda e : self.update_day(self.get_day_of_month(self.menu_option_month.get())), width=10)
        self.menu_option_month.pack(side='left', padx=5)

        self.menu_option_year = CTkOptionMenu(self, values=[str(i) for i in range(2021, 2031)], command=lambda e : self.update_day(self.get_day_of_month(self.menu_option_month.get())), width=10)
        self.menu_option_year.pack(side='left', padx=5)


    
    def get_day_of_month(self, month):
        return monthrange(int(self.menu_option_year.get()), int(month))[1]
    
    def update_day(self, day):
        self.menu_option_day.configure(values=[str(i) for i in range(1, day + 1)])


    def get_value(self):
        return datetime.strptime(f'{self.menu_option_day.get()}/{self.menu_option_month.get()}/{self.menu_option_year.get()}', '%d/%m/%Y')
from app.setting.setting import *
from app.db.main import *
from app.ui.main_ui import MainUI


class AuthUI(CTkFrame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill='both', expand=True)
        self.master = master
        # Dao
        self.account_dao = AccountDAO()

        self.init_ui()

    def init_ui(self):

        self.main_frame = CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.tab_auth = CTkTabview(self.main_frame)
        self.tab_auth.pack(fill='both', expand=True)

        self.frame_login = self.tab_auth.add('Login')
        self.frame_register = self.tab_auth.add('Register')

        # ----------------- Login -----------------
        self.label_email = CTkLabel(self.frame_login, text='Email')
        self.label_email.pack(pady=5)

        self.entry_email = CTkEntry(self.frame_login)
        self.entry_email.pack(pady=5)

        self.label_password = CTkLabel(self.frame_login, text='Password')
        self.label_password.pack(pady=5)

        self.entry_password = CTkEntry(self.frame_login, show='*')
        self.entry_password.pack(pady=5)

        self.btn_login = CTkButton(self.frame_login, text='Login', command=self.on_login)
        self.btn_login.pack(pady=5)

        # ----------------- Register -----------------
        self.label_name = CTkLabel(self.frame_register, text='Name')
        self.label_name.pack(pady=5)

        self.entry_name = CTkEntry(self.frame_register)
        self.entry_name.pack(pady=5)

        self.label_email_register = CTkLabel(self.frame_register, text='Email')
        self.label_email_register.pack(pady=5)

        self.entry_email_register = CTkEntry(self.frame_register)
        self.entry_email_register.pack(pady=5)

        self.label_password_register = CTkLabel(self.frame_register, text='Password')
        self.label_password_register.pack(pady=5)

        self.entry_password_register = CTkEntry(self.frame_register, show='*')
        self.entry_password_register.pack(pady=5)

        self.btn_register = CTkButton(self.frame_register, text='Register', command=self.on_register)
        self.btn_register.pack(pady=5)

    def on_login(self):
        try:
            email = self.entry_email.get()
            password = self.entry_password.get()

            all_account = self.account_dao.get_all()
            for account in all_account:
                if account.email == email and account.password == password:
                    print('Login success')
                    # self.destroy()
                    MainUI(account=account).run_ui()
                    return
        except Exception as e:
            print(f'Error: {e}')

    def on_register(self):
        try:
            name = self.entry_name.get()
            email = self.entry_email_register.get()
            password = self.entry_password_register.get()

            all_account = self.account_dao.get_all()
            account = Account(name=name, email=email, password=password)
            if account not in all_account:
                self.account_dao.create(account)
                print('Register success')
            else:
                print('Account already exists')
        except Exception as e:
            print(f'Error: {e}')



    def run_ui(self):
        self.mainloop()


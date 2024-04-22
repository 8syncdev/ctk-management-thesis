from app.setting.setting import *
from app.custom.TableView import TableView
from app.db.main import *
from app.utils.main import *
from app.asset.styles.style import *
from app.custom.SlideControl import SlideControl
from app.custom.CalenderControl import CalenderControl

class TabGradeUI(CTkFrame):

    def __init__(self, master=None, loggin_account=None, base_master=None, **kw):
        super().__init__(master=master, **kw)
        self.master = master
        self.loggin_account = loggin_account
        self.base_master = base_master
        self.pack(fill='both', expand=True)
        # Select group
        self.selected_group = None
        if self.loggin_account.role == 'lecturer':
            self.selected_group = AccountUtil.get_all_group_of_thesis(self.loggin_account)[0] if AccountUtil.get_all_group_of_thesis(self.loggin_account) != [] else None
        self.init_ui()

    def init_ui(self):
        # ----------------- Header -----------------
        if hasattr(self, 'header_section'):
            self.header_section.destroy()
        self.header_section = CTkFrame(self, height=50,)
        self.header_section.pack(fill='x', expand=False, side='top', pady=5, padx=5)

        self.implement_header()

        # ----------------- Body -----------------
        if hasattr(self, 'body_section'):
            self.body_section.destroy()
        self.body_section = CTkFrame(self,)
        self.body_section.pack(fill='both', expand=True, padx=5, pady=(0, 5))
        self.implement_body()


    def implement_header(self):
        # ----------------- Left Header -----------------
        self.left_header = CTkFrame(self.header_section, width=300, height=50)
        self.left_header.pack(side='left', fill='x', pady=5, padx=5)

        if self.loggin_account.role=='lecturer':
            name_group = self.selected_group.name if self.selected_group != None else "No Group"
        else:
            name_group = AccountUtil.get_joined_group(self.loggin_account).name if AccountUtil.get_joined_group(self.loggin_account) != None else "No Group"
        self.label_name_group = CTkLabel(self.left_header, 
                                         text=f'Group: {AccountUtil.get_joined_group(self.loggin_account).name if AccountUtil.get_joined_group(self.loggin_account) != None and self.loggin_account.role=="student" else name_group}', 
                                         width=300)
        self.label_name_group.pack(pady=5, padx=5)

        # ----------------- Right Header -----------------
        self.right_header = CTkFrame(self.header_section, width=300, height=50)
        self.right_header.pack(side='right', fill='x', pady=5, padx=5)

        if self.loggin_account.role=='lecturer':
            self.menu_option_groups_of_lecturer = CTkOptionMenu(self.right_header, values=[group.name for group in AccountUtil.get_all_group_of_thesis(self.loggin_account)], command=self.on_change_group)
            self.menu_option_groups_of_lecturer.pack(side='right', padx=5)

    def on_change_group(self, e):
        try:
            get_all_group = AccountUtil.get_all_group_of_thesis(self.loggin_account)
            for group in get_all_group:
                if group.name == self.menu_option_groups_of_lecturer.get():
                    self.selected_group = group
                    self.init_ui()
        except Exception as e:
            print(f'Error: {e}')
            pass

    def implement_body(self):
        # ----------------- Left Body -----------------
        self.left_body = CTkFrame(self.body_section, width=300)
        self.left_body.pack(side='left', fill='y', padx=5)

        # ----------------- Right Body -----------------
        self.right_body = CTkFrame(self.body_section)
        self.right_body.pack(side='right', fill='both', expand=True, padx=5)

        # ----------------- Left Body -----------------
        self.implement_left_body()

        # ----------------- Right Body -----------------
        self.implement_right_body()

    def implement_left_body(self):
        self.button_open_eval_grade = CTkButton(self.left_body, text='Evaluate Grade', command=self.open_eval_grade)
        self.button_open_eval_grade.pack(pady=5, padx=5, fill='x')

    def implement_right_body(self, selected_group=None):
        if hasattr(self, 'wrapped_view_right_body'):
            self.wrapped_view_right_body.destroy()
        self.wrapped_view_right_body = CTkFrame(self.right_body)
        self.wrapped_view_right_body.pack(fill='both', expand=True)

        get_all_group = AccountUtil.get_all_group_of_thesis(self.loggin_account)

        self.scroll_view_member_group = CTkScrollableFrame(self.wrapped_view_right_body,)
        self.scroll_view_member_group.pack(fill='both', expand=True)

        if selected_group != None:
            for account in selected_group.account_list:
                row = CTkFrame(self.scroll_view_member_group)
                row.pack(fill='x', padx=5, pady=2)
                self.init_ui_member_group(row, account)
        else:
            for group in get_all_group:
                for account in group.account_list:
                    row = CTkFrame(self.scroll_view_member_group)
                    row.pack(fill='x', padx=5, pady=2)
                    self.init_ui_member_group(row, account)

    def init_ui_member_group(self, row, account):
        self.label_name_member = CTkLabel(row, text=f'{account.name}', width=200)
        self.label_name_member.pack(side='left', padx=5, pady=5)

        self.label_role_member = CTkLabel(row, text=f'Group: {AccountUtil.get_joined_group(account).name if AccountUtil.get_joined_group(account) != None else "No Group"}, Thesis: {AccountUtil.get_thesis_of_account(self.loggin_account).name}', width=100)
        self.label_role_member.pack(side='left', padx=5, pady=5)

        self.button_view_detail = CTkButton(row, text='View Detail', command=lambda: self.view_detail_member(account))
        self.button_view_detail.pack(side='right', padx=5, pady=5)

        


    def open_eval_grade(self):
        ...

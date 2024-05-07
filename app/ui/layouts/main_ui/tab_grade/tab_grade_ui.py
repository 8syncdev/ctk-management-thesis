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
        # DAO
        self.grade_dao = GradeDAO()
        self.init_ui()

    def init_ui(self):
        # Selected Group
        self.selected_group = AccountUtil.get_joined_group(self.loggin_account) if AccountUtil.get_joined_group(self.loggin_account) != None else None
        if self.loggin_account.role == 'lecturer':
            self.selected_group = AccountUtil.get_all_group_of_thesis(self.loggin_account)[0] if AccountUtil.get_all_group_of_thesis(self.loggin_account) != [] else None
        self.selected_theis = AccountUtil.get_thesis_of_selected_group(self.selected_group)
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

        self.label_name_thesis = CTkLabel(self.left_header, text=f'''Thesis: {AccountUtil.get_thesis_of_selected_group(self.selected_group).name if self.selected_group != None else 'No thesis'} ''', width=200, font=get_style('font_lg_bold'), text_color=get_style('dark_active'))
        self.label_name_thesis.pack(pady=5, padx=5, side='left')

        # ----------------- Right Header -----------------
        self.right_header = CTkFrame(self.header_section, width=300, height=50)
        self.right_header.pack(side='right', fill='x', pady=5, padx=5)

        if self.loggin_account.role=='lecturer':
            self.menu_option_groups_of_lecturer = CTkOptionMenu(self.right_header, values=[group.name for group in AccountUtil.get_all_group_of_thesis(self.loggin_account) if self.selected_group != None], command=self.on_change_group)
            self.menu_option_groups_of_lecturer.pack(side='right', padx=5)
            self.menu_option_groups_of_lecturer.set(self.menu_option_groups_of_lecturer._values[0])

            self.menu_option_thesis_of_lecturer = CTkOptionMenu(self.right_header, values=[thesis.name for thesis in AccountUtil.get_all_thesis_of_account(self.loggin_account)], command=self.on_change_thesis)
            self.menu_option_thesis_of_lecturer.pack(side='right', padx=5)
    
    
    def on_change_thesis(self, e):
        try:
            get_all_thesis = AccountUtil.get_all_thesis_of_account(self.loggin_account)
            for thesis in get_all_thesis:
                if thesis.name == self.menu_option_thesis_of_lecturer.get():
                    self.menu_option_groups_of_lecturer.configure(values=[group.name for group in thesis.group_list])
                    self.menu_option_thesis_of_lecturer.set(thesis.name)
                    self.menu_option_groups_of_lecturer.set(thesis.group_list[0].name)
                    self.label_name_group.configure(text=f'Group: {thesis.group_list[0].name}')
                    self.label_name_thesis.configure(text=f'Thesis: {thesis.name}')
                    self.selected_theis = thesis
                    # Re-Implement body
                    self.selected_group = thesis.group_list[0]
            self.implement_body()
            self.on_change_group()
        except Exception as e:
            print(f'Error: {e}')
            pass

    def on_change_group(self, e=None):
        try:
            self.slide_control_evel_grade.animate_backwards()
            get_all_group = AccountUtil.get_all_group_of_thesis(self.loggin_account, self.selected_theis)
            print([group.name for group in get_all_group])
            print(self.menu_option_groups_of_lecturer.get())
            for group in get_all_group:
                if group.name == self.menu_option_groups_of_lecturer.get():
                    self.selected_group = group
                    self.menu_option_groups_of_lecturer.set(group.name)
                    self.label_name_group.configure(text=f'Group: {group.name}')
            self.implement_body()
        except Exception as e:
            print(f'Error: {e}')
            pass

    def implement_body(self):
        # ----------------- Left Body -----------------
        if hasattr(self, 'left_body'):
            self.left_body.destroy()
        self.left_body = CTkFrame(self.body_section, width=300)
        self.left_body.pack(side='left', fill='y', padx=5)

        # ----------------- Right Body -----------------
        if hasattr(self, 'right_body'):
            self.right_body.destroy()
        self.right_body = CTkFrame(self.body_section)
        self.right_body.pack(side='right', fill='both', expand=True, padx=5)

        # ----------------- Left Body -----------------
        self.implement_left_body()

        # ----------------- Right Body -----------------
        self.implement_right_body()

    def implement_left_body(self):
        if self.loggin_account.role == 'lecturer':
            self.button_open_eval_grade = CTkButton(self.left_body, text='Evaluate Grade', command=lambda: self.slide_control_evel_grade.animate())
            self.button_open_eval_grade.pack(pady=5, padx=5, fill='x')

            self.init_ui_slide_control_evel_grade()
        else:
            self.left_body.destroy()
        

    def init_ui_slide_control_evel_grade(self):
        self.slide_control_evel_grade = SlideControl(self.base_master, -0.5, 0, options={
            'rely': 0.05,
            'relheight': 0.95,
        }, time_duration=0.01)

        self.frame_detail_left = CTkFrame(self.slide_control_evel_grade, border_width=5)
        self.frame_detail_left.pack(fill='both', expand=True)

        # Intro Detail Left Frame
        self.intro_detail_left_frame = CTkFrame(self.frame_detail_left, height=500)
        self.intro_detail_left_frame.pack(fill='both', pady=5, padx=5, expand=True)

        # Inner Header Frame
        self.inner_header_frame_detail = CTkFrame(self.intro_detail_left_frame)
        self.inner_header_frame_detail.pack(fill='x', pady=5, padx=5)

        self.label_inner_header = CTkLabel(self.inner_header_frame_detail, text='Evaluate Grade')
        self.label_inner_header.pack(side='left', padx=5, pady=5, fill='x')

        self.button_back = CTkButton(self.inner_header_frame_detail, text='', command=lambda: self.slide_control_evel_grade.animate(), image=AssetUtil.get_icon('x-circle'))
        self.button_back.pack(side='right', padx=5, pady=5)

        
        


    def implement_right_body(self, selected_group=None):
        if self.loggin_account.role == 'lecturer':
            if hasattr(self, 'wrapped_view_right_body'):
                self.wrapped_view_right_body.destroy()
            self.wrapped_view_right_body = CTkFrame(self.right_body)
            self.wrapped_view_right_body.pack(fill='both', expand=True)

            if not hasattr(self, 'selected_theis'):
                self.selected_theis = AccountUtil.get_thesis_of_selected_group(self.selected_group)
            get_all_group = AccountUtil.get_all_group_of_thesis(self.loggin_account, self.selected_theis)

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
        else:
            if hasattr(self, 'wrapped_view_right_body'):
                self.wrapped_view_right_body.destroy()
            self.wrapped_view_right_body = CTkFrame(self.right_body)
            self.wrapped_view_right_body.pack(fill='both', expand=True)

            get_join_group = AccountUtil.get_joined_group(self.loggin_account)
            if get_join_group != None:
                for account in get_join_group.account_list:
                    row = CTkFrame(self.wrapped_view_right_body)
                    row.pack(fill='x', padx=5, pady=2)
                    self.init_ui_member_group(row, account)
            else:
                self.label_no_group = CTkLabel(self.wrapped_view_right_body, text='You have not joined any group', font=get_style('font_bold_italic'))
                self.label_no_group.pack(pady=5, padx=5)


    def init_ui_member_group(self, row, account):
        self.label_name_member = CTkLabel(row, text=f'{account.name}', width=200)
        self.label_name_member.pack(side='left', padx=5, pady=5)

        self.label_role_member = CTkLabel(row, text=f'Group: {AccountUtil.get_joined_group(account).name if AccountUtil.get_joined_group(account) != None else "No Group"}, Thesis: {self.selected_theis.name}', width=100)
        self.label_role_member.pack(side='left', padx=5, pady=5)

        self.label_progress = CTkLabel(row, text=f'Progress: {AccountUtil.get_total_progress_of_account(account)}%', width=100, font=get_style('font_bold_italic'), text_color=get_style('info_active'))
        self.label_progress.pack(side='left', padx=5, pady=5)
        if self.loggin_account.role == 'lecturer':
            self.button_open_eval_grade = CTkButton(row, text='Evaluate', image=AssetUtil.get_icon('edit-2', resize=(20, 20)), fg_color=get_style('info_active'), text_color=get_style('white'), command=lambda account=account: self.open_eval_grade(account))
            self.button_open_eval_grade.pack(side='right', padx=5, pady=5)
        else:
            self.label_grade = CTkLabel(row, text=f'Grade: {AccountUtil.get_grade_of_account(account)}%', width=100, font=get_style('font_bold_italic'), text_color=get_style('info_active'))
            self.label_grade.pack(side='right', padx=5, pady=5)
        

    def open_eval_grade(self, account):
        self.slide_control_evel_grade.animate_backwards()

        # Data to submit
        get_thesis_of_account = AccountUtil.get_thesis_of_account(self.loggin_account)

        # Inner Body Frame from func init_ui_slide_control_evel_grade
        if hasattr(self, 'inner_body_frame_detail'):
            self.inner_body_frame_detail.destroy()
        self.inner_body_frame_detail = CTkFrame(self.intro_detail_left_frame)
        self.inner_body_frame_detail.pack(fill='both', expand=True)

        # Inner Body Frame
        self.inner_body_frame = CTkFrame(self.inner_body_frame_detail)
        self.inner_body_frame.pack(fill='both', expand=True)

        row = CTkFrame(self.inner_body_frame)
        row.pack(fill='x', padx=5, pady=5)
        self.label_score = CTkLabel(row, text='Score:', width=100)
        self.label_score.pack(side='left', padx=5, pady=5)
        self.score_of_account = CTkSlider(row, from_=0, to=100, orientation='horizontal', width=300)
        self.score_of_account.pack(pady=5, padx=5, fill='x', side='right')

        row = CTkFrame(self.inner_body_frame)
        row.pack(fill='x', padx=5, pady=5)
        self.label_info = CTkLabel(row, text='Info:', width=100)
        self.label_info.pack(side='left', padx=5, pady=5)
        self.label_info_account = CTkLabel(row, text=f'Full Name: {account.name}\nEmail: {account.email}\nRole: {account.role}\nGroup: {AccountUtil.get_joined_group(account).name if AccountUtil.get_joined_group(account) != None else "No Group"}\nThesis: {get_thesis_of_account.name if get_thesis_of_account != None else "No Thesis"}', width=300, font=get_style('font_bold_italic'))
        self.label_info_account.pack(pady=5, padx=5, fill='x', side='right')


        row_action = CTkFrame(self.inner_body_frame)
        row_action.pack(fill='x', padx=5, pady=5)

        self.button_grade = CTkButton(row_action, text='Grade', command=lambda _account=account: self.grade_account(_account))
        self.button_grade.pack(side='right', padx=5, pady=5)



        self.after(1000, self.slide_control_evel_grade.animate)

    def grade_account(self, account):
        try:
            for grade in self.grade_dao.get_all():
                if grade.account == account and grade.thesis == self.selected_theis:
                    grade.score = self.score_of_account.get() if self.score_of_account.get() != grade.score else grade.score
                    self.grade_dao.update(grade)
                    self.slide_control_evel_grade.animate()
                    print('Update Grade Success')
                    return
            grade = Grade(
                account=account,
                score=self.score_of_account.get(),
                thesis=self.selected_theis,
            )
            self.grade_dao.create(grade)
            self.slide_control_evel_grade.animate()
            print('Grade Success')
        except Exception as e:
            print(f'Error: {e}')
            pass


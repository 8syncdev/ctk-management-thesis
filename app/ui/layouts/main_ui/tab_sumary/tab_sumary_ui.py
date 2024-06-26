from app.setting.setting import *
from app.custom.TableView import TableView
from app.db.main import *
from app.utils.main import *
from app.asset.styles.style import *
from app.custom.SlideControl import SlideControl
from app.custom.CalenderControl import CalenderControl



class TabSumaryUI(CTkFrame):

    def __init__(self, master=None, loggin_account = None, base_master = None, **kw):
        super().__init__(master=master, **kw)
        self.master = master
        self.base_master = base_master
        self.loggin_account = loggin_account
        self.pack(fill='both', expand=True)
        # ------------ DAO ----------------
        self.thesis_dao = ThesisDAO()
        self.account_dao = AccountDAO()
        self.gradebycouncil = GradeByCouncilDAO()
        self.grade_dao = GradeDAO()
        # ------------ UI ----------------
        self.init_ui()

    def init_ui(self):
        # Slide Component:
        self.slide_grade_council = SlideControl(self.base_master, -0.5, 0, options={
                'rely': 0.1,
                'relheight': 0.8,
            }, time_duration=0.01)
        self.init_slide_grade_council_ui()
        # Header Frame
        self.init_header_ui()

        # Slide Show Group Task
        self.slide_grade_account = SlideControl(self.base_master, -0.5, 0, options={
                'rely': 0.1,
                'relheight': 0.8,
            }, time_duration=0.01)



        # Body Frame
        self.body_frame= CTkScrollableFrame(self)
        self.body_frame.pack(fill='both', expand=True, padx=3, pady=(0, 3))
        self.init_body_ui()

    def init_slide_grade_council_ui(self):
        header_frame = CTkFrame(self.slide_grade_council, height=50)
        header_frame.pack(fill='x', padx=3, pady=3)

        CTkLabel(header_frame, text='Grade By Council', font=get_style('font_lg_bold')).pack(side='left', padx=10)

        button_close = CTkButton(header_frame, text='', fg_color=get_style('danger'), text_color=get_style('white'), command=lambda: self.slide_grade_council.animate(), width=30, height=30, image=AssetUtil.get_icon('x'))
        button_close.pack(side='right', padx=10)


        body_frame = CTkFrame(self.slide_grade_council)
        body_frame.pack(fill='both', expand=True, padx=3, pady=3)

        row = CTkFrame(body_frame)
        row.pack(fill='x', padx=3, pady=1)

        CTkLabel(row, text='Thesis:', font=get_style('font_bold'), width=200).pack(side='left', padx=10)

        get_all_thesis = [
            f'{thesis.id} - {thesis.name} - {thesis.account.name}'
            for thesis in self.thesis_dao.get_all()
        ]

        menu_option_thesis = CTkOptionMenu(row, values=get_all_thesis, width=50)
        menu_option_thesis.pack(side='left', padx=10)

        row = CTkFrame(body_frame)
        row.pack(fill='x', padx=3, pady=1)

        CTkLabel(row, text='Council:', font=get_style('font_bold'), width=200).pack(side='left', padx=10)

        get_all_council = [
            council.name
            for council in self.account_dao.get_all() if council != self.loggin_account and council.role == 'lecturer'
        ]

        scroll_show_council = CTkScrollableFrame(row, width=200, height=100)
        scroll_show_council.pack(side='left', padx=10, fill='both')
        

        self.selected_council = []
        for council in get_all_council:
            check_item = CTkCheckBox(scroll_show_council, text=council, font=get_style('font_bold'), onvalue=(True, council), offvalue=(False, council), command=lambda e=council, *args: self.handle_selected_council(e, *args))
            check_item.pack(fill='x', padx=10, pady=5)

        row = CTkFrame(body_frame)
        row.pack(fill='x', padx=3, pady=1)

        button_submit = CTkButton(row, text='Submit', fg_color=get_style('success'), text_color=get_style('white'), command=lambda thesis=menu_option_thesis.get(): self.submit_grade_by_council(thesis, scroll_show_council))
        button_submit.pack(side='right', padx=10)

    def handle_selected_council(self, council, *args):
        if council in self.selected_council:
            self.selected_council.remove(council)
        else:
            self.selected_council.append(council)

    def submit_grade_by_council(self, thesis, council_list):
        if self.selected_council.__len__() == 0:
            print('Please select council')
            return
        
        get_council = [
            council
            for council in self.account_dao.get_all() if council.name in self.selected_council and council != self.loggin_account and council.role == 'lecturer'
        ]

        grade_by_council = GradeByCouncil(
            id=self.gradebycouncil.get_all()[self.gradebycouncil.count()-1].id + 1 if self.gradebycouncil.count() > 0 else 1,
            thesis=self.thesis_dao.get(int(thesis.split(' - ')[0])),
            account_list=get_council
        )
        self.gradebycouncil.create(grade_by_council)

        self.slide_grade_council.animate()


    def init_header_ui(self):
        self.header_frame = CTkFrame(self, height=50)
        self.header_frame.pack(fill='x', padx=3, pady=3)
        
        options_menu = [
            'Teacher No Task',
            'Most Registered Teacher',
            'Grade By Council'
        ]

        self.button_grade_by_council = CTkButton(self.header_frame, text='Grade By Council', fg_color=get_style('success'), text_color=get_style('white'), command=lambda: self.slide_grade_council.animate())
        self.button_grade_by_council.pack(side='left', padx=10)
        if self.loggin_account.role == 'lecturer':
            self.menu_options = CTkOptionMenu(self.header_frame, values=options_menu, width=20, command= lambda e: self.init_body_ui())
            self.menu_options.pack(side='left', padx=10)


    def handle_teacher_no_task(self, container = None):
        if hasattr(self, 'inner_frame_show'):
            self.inner_frame_show.destroy()
        
        self.inner_frame_show = CTkFrame(container)
        self.inner_frame_show.pack(fill='both', expand=True)

        get_data_teacher_no_task = self.get_data_teacher_no_task()
        print(get_data_teacher_no_task)

        for data in get_data_teacher_no_task:
            row = CTkFrame(self.inner_frame_show)
            row.pack(fill='x', padx=3, pady=1)

            align_content = CTkFrame(row, fg_color='transparent')
            align_content.pack(fill='x', padx=10 , pady=5)

            name_thesis = CTkLabel(align_content, text=data['name_thesis'], width=400, font=get_style('font_lg_bold'), text_color=get_style('dark_active'))
            name_thesis.pack(side='left')

            name_teacher = CTkLabel(align_content, text=data['name_teacher'], width=200, font=get_style('font_bold'), text_color=get_style('secondary_active'))
            name_teacher.pack(side='left', padx=20)

            CTkLabel(align_content, text='No Task', width=30, font=get_style('font_lg_bold_italic'), text_color=get_style('danger_active')).pack(side='left', padx=20)


    def handle_most_registered_teacher(self, container = None):
        if hasattr(self, 'inner_frame_show'):
            self.inner_frame_show.destroy()
        
        self.inner_frame_show = CTkFrame(container)
        self.inner_frame_show.pack(fill='both', expand=True)

        get_all_thesis = self.thesis_dao.get_all()

        list_teacher = []
        for thesis in get_all_thesis:
            list_teacher.append(thesis.account.name)

        dict_teacher = {}
        for teacher in list_teacher:
            if teacher in dict_teacher:
                dict_teacher[teacher] += 1
            else:
                dict_teacher[teacher] = 1

        sorted_dict_teacher = dict(sorted(dict_teacher.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_dict_teacher.items():
            row = CTkFrame(self.inner_frame_show)
            row.pack(fill='x', padx=3, pady=1)

            align_content = CTkFrame(row, fg_color='transparent')
            align_content.pack(fill='x', padx=10 , pady=5)

            name_teacher = CTkLabel(align_content, text=key, width=400, font=get_style('font_lg_bold'), text_color=get_style('dark_active'))
            name_teacher.pack(side='left')

            amount_registered = CTkLabel(align_content, text=str(value), width=200, font=get_style('font_bold'), text_color=get_style('secondary_active'))
            amount_registered.pack(side='left', padx=20)

            CTkLabel(align_content, text='Registered', width=30, font=get_style('font_lg_bold_italic'), text_color=get_style('success_active')).pack(side='left', padx=20)

    def init_body_ui(self):
        if hasattr(self, 'frame_show'):
            self.frame_show.destroy()
        self.frame_show = CTkFrame(self.body_frame)
        self.frame_show.pack(fill='both', expand=True)


        if self.loggin_account.role == 'lecturer':
            if self.menu_options.get() == 'Teacher No Task':
                self.handle_teacher_no_task(self.frame_show)
            elif self.menu_options.get() == 'Most Registered Teacher':
                self.handle_most_registered_teacher(self.frame_show)
            elif self.menu_options.get() == 'Grade By Council':
                self.init_ui_council_join_the_thesis()
        else:
            self.init_ui_council_join_the_thesis()

    def get_data_teacher_no_task(self):
        get_all_thesis = self.thesis_dao.get_all()

        list_teacher_no_task = []
        for thesis in get_all_thesis:
            print(thesis.name)
            print(thesis.account.name)
            amount_task = [
                task for task in thesis.account.task_list
            ].__len__()
            if amount_task == 0:
                list_teacher_no_task.append(
                    {
                        'name_thesis': thesis.name,
                        'name_teacher': thesis.account.name,
                    }
                )

        return list_teacher_no_task
    
    def init_ui_council_join_the_thesis(self):
        if hasattr(self, 'inner_frame_show'):
            self.inner_frame_show.destroy()
        
        self.inner_frame_show = CTkFrame(self.frame_show)
        self.inner_frame_show.pack(fill='both', expand=True)
        if self.loggin_account.role == 'lecturer':
            for grade_by_council in self.gradebycouncil.get_all():
                if self.loggin_account in grade_by_council.account_list:
                    self.grade_by_council = grade_by_council
                    for group in grade_by_council.thesis.group_list:
                        for member in group.account_list:
                            #* Grade all member in group
                            row = CTkFrame(self.inner_frame_show)
                            row.pack(fill='x', padx=3, pady=1)

                            align_content = CTkFrame(row, fg_color='transparent')
                            align_content.pack(fill='x', padx=10 , pady=5)

                            name_thesis = CTkLabel(align_content, text=grade_by_council.thesis.name, width=400, font=get_style('font_lg_bold'), text_color=get_style('dark_active'))
                            name_thesis.pack(side='left')

                            name_member = CTkLabel(align_content, text=member.name, width=200, font=get_style('font_bold'), text_color=get_style('secondary_active'))
                            name_member.pack(side='left', padx=20)

                            CTkLabel(align_content, text=f"Grade: {AccountUtil.get_grade_of_account(member)}", width=30, font=get_style('font_lg_bold_italic'), text_color=get_style('success_active')).pack(side='left', padx=20)

                            if self.loggin_account.role == 'lecturer':
                                CTkButton(align_content, text='View', fg_color=get_style('success'), text_color=get_style('white'), command=lambda member=member: self.view_grade(member)).pack(side='right', padx=10)

        else:
            row = CTkFrame(self.inner_frame_show)
            row.pack(fill='x', padx=3, pady=1)

            align_content = CTkFrame(row, fg_color='transparent')
            align_content.pack(fill='x', padx=10 , pady=5)

            name_thesis = CTkLabel(align_content, text="Name Thesis", width=400, font=get_style('font_lg_bold'), text_color=get_style('dark_active'))
            name_thesis.pack(side='left')

            name_teacher = CTkLabel(align_content, text="Name Teacher", width=200, font=get_style('font_bold'), text_color=get_style('secondary_active'))
            name_teacher.pack(side='left', padx=20)

            CTkLabel(align_content, text=f"Grade", width=30, font=get_style('font_lg_bold_italic'), text_color=get_style('success_active')).pack(side='left', padx=20)
            for grade_by_council in self.gradebycouncil.get_all():
                for grade in grade_by_council.grade_list:
                    if grade.account == self.loggin_account:
                        row = CTkFrame(self.inner_frame_show)
                        row.pack(fill='x', padx=3, pady=1)

                        align_content = CTkFrame(row, fg_color='transparent')
                        align_content.pack(fill='x', padx=10 , pady=5)

                        name_thesis = CTkLabel(align_content, text=grade_by_council.thesis.name, width=400, font=get_style('font_lg_bold'), text_color=get_style('dark_active'))
                        name_thesis.pack(side='left')

                        name_teacher = CTkLabel(align_content, text=grade.name_teacher_grade, width=200, font=get_style('font_bold'), text_color=get_style('secondary_active'))
                        name_teacher.pack(side='left', padx=20)

                        CTkLabel(align_content, text=f"{grade.score}", width=30, font=get_style('font_lg_bold_italic'), text_color=get_style('success_active')).pack(side='left', padx=20)
                    

    def view_grade(self, member):
        self.slide_grade_account.animate()
        if hasattr(self, 'slide_grade_account_inner'):
            self.slide_grade_account_inner.destroy()
        
        self.slide_grade_account_inner = CTkFrame(self.slide_grade_account)
        self.slide_grade_account_inner.pack(fill='both', expand=True, padx=3, pady=3)
        header_row = CTkFrame(self.slide_grade_account_inner)
        header_row.pack(fill='x', pady=5, padx=5)

        button_close = CTkButton(header_row, text='', image=AssetUtil.get_icon('x'), width=40, height=40, fg_color='red',command=self.slide_grade_account.animate)
        button_close.pack(side='right', pady=5, padx=5)

        body_row = CTkFrame(self.slide_grade_account_inner)
        body_row.pack(fill='both', expand=True, pady=5, padx=5)

        row_grade = CTkFrame(body_row)
        row_grade.pack(fill='x', pady=5, padx=5)

        CTkLabel(row_grade, text='Grade:', font=get_style('font_bold'), width=200).pack(side='left', padx=10)

        slider_grade = CTkSlider(row_grade, to=100, from_=0, width=200)
        slider_grade.pack(side='right', padx=10, fill='x')

        row_submit = CTkFrame(body_row)
        row_submit.pack(fill='x', pady=5, padx=5)

        button_submit = CTkButton(row_submit, text='Submit', fg_color=get_style('success'), text_color=get_style('white'), command=lambda member=member, grade=slider_grade: self.submit_grade(member, grade))
        button_submit.pack(side='right', padx=10)


    def submit_grade(self, member, grade):
        grade=(grade.get())
        if self.loggin_account.name in [grade.name_teacher_grade for grade in self.grade_by_council.grade_list]:
            get_grade = [
                grade
                for grade in self.grade_by_council.grade_list if grade.name_teacher_grade == self.loggin_account.name
            ][0]
            # print(get_grade.score, get_grade.account.name, get_grade.name_teacher_grade)
            get_grade.score = grade
            self.gradebycouncil.update(self.grade_by_council)
            self.slide_grade_account.animate()
            print('Update grade')
            self.init_ui_council_join_the_thesis()
            return
        _grade = Grade(
            score=grade,
            account=member,
            name_teacher_grade=self.loggin_account.name,
            thesis=self.grade_by_council.thesis
        )
        self.grade_by_council.grade_list.append(_grade)
        self.gradebycouncil.update(self.grade_by_council)
        self.slide_grade_account.animate()
        print('Submit grade')
        self.init_ui_council_join_the_thesis()


                        

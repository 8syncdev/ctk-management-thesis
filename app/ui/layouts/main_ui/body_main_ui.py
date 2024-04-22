from app.setting.setting import *
from app.custom.TableView import TableView
from app.db.main import *
from app.utils.main import *
from app.asset.styles.style import *
from app.custom.SlideControl import SlideControl
from app.ui.layouts.main_ui.tab_group.tab_group_ui import TabGroupUI
from app.ui.layouts.main_ui.tab_grade.tab_grade_ui import TabGradeUI


class BodyMain(CTkFrame):

    def __init__(self, parent, account, role, **kwargs):
        super().__init__(parent.body, **kwargs)
        self.parent = parent
        self.account = account
        self.role = account.role
        self.pack(fill='both', expand=True)
        # --------------- DAO ---------------
        self.thesis_dao = ThesisDAO()
        self.tech_require_dao = TechnologyRequirementDAO()
        self.tech_cate_dao = TechnologyCategoryDAO()
        self.group_dao = GroupDAO()
        self.account_dao = AccountDAO()
        # --------------- Init UI ---------------
        self.init_ui()

    def init_ui(self):
        # --------------- Menu Bar ---------------
        self.menu_bar = CTkFrame(self, width=200)
        self.menu_bar.pack(side='left', fill='y', padx=(0, 5))

        self.button_bar = CTkButton(self.menu_bar, text='', image=AssetUtil.get_icon('menu'), command=lambda: self.inner_menu_bar.animate())
        self.button_bar.pack(fill='x', pady=(0, 5), padx=(0,5))

        self.inner_menu_bar = SlideControl(self.menu_bar, -1, 0)
        self.inner_menu_bar.animate()

        self.button_home = CTkButton(self.inner_menu_bar, text='', image=AssetUtil.get_icon('home'), command=lambda: self.event_change_tab('Home'))
        self.button_home.pack(fill='x', pady=(0,5), padx=(0,5))

        self.button_group = CTkButton(self.inner_menu_bar, text='', image=AssetUtil.get_icon('activity'), command=lambda: self.event_change_tab('Group'))
        self.button_group.pack(fill='x', pady=(0,5), padx=(0,5))

        self.button_grade = CTkButton(self.inner_menu_bar, text='', image=AssetUtil.get_icon('award'), command=lambda: self.event_change_tab('Grade'))
        self.button_grade.pack(fill='x', pady=(0,5), padx=(0,5))
        
        # --------------- Content ---------------
        # Tab
        self.tab_view_content = CTkTabview(self, command=self.event_change_tab)
        self.tab_view_content.pack(fill='both', expand=True)
        #----------------- Tab Home -----------------
        '''
            Tab Home:
        '''
        self.tab_view_content.add('Home')
        self.content_home = CTkFrame(self.tab_view_content.tab('Home'))
        self.content_home.pack(side='right', fill='both', expand=True)
        #----------------- Search -----------------
        self.search_frame = CTkFrame(self.content_home)
        self.search_frame.pack(fill='x', pady=5)

        self.search_entry = CTkEntry(self.search_frame)
        self.search_entry.pack(side='left', fill='x', expand=True)

        self.search_button = CTkButton(self.search_frame, text='',image=AssetUtil.get_icon('search'))
        self.search_button.pack(side='right', padx=(5, 0))
        #----------------- Table -----------------
        self.scroll_frame_table = CTkScrollableFrame(self.content_home, height=600)
        self.scroll_frame_table.pack(fill='x')
        # Get data from database
        self.origin_data_table = self.get_values_thesis(self.thesis_dao.get_all())
        # Table View
        self.table_view_home = TableView(self.scroll_frame_table, 
                                         column=self.origin_data_table[0].__len__(), 
                                         row=self.origin_data_table.__len__(), 
                                         wraplength=2000, 
                                         command=self.show_detail_thesis,
                                         values=self.origin_data_table
                                         )
        self.table_view_home.pack(fill='x')
        # self.table_view_home.update_values(self.get_values_thesis(self.thesis_dao.get_all()))

        # Event Table
        TableUtil.base_ui = self
        TableUtil.table_ui = self.table_view_home
        TableUtil.func_format_data = self.get_values_thesis
        self.search_entry.bind('<Return>', lambda event: TableUtil.find_data(self.thesis_dao, self.search_entry.get()))

        #----------------- End Table -----------------
        
        # --------------- Event ---------------
        """
            # Implement when click on table
            # show_detail_thesis()
            # init_ui_show_detail_thesis()
        """

        # --------------- Slide Show ---------------
        # Left Slide Show
        self.slide_show_detail = SlideControl(self, -0.5, 0, options={
            'rely': 0.05,
            'relheight': 0.95,
        }, time_duration=0.01)
        self.scroll_frame_detail_left = CTkFrame(self.slide_show_detail, border_width=5)
        self.scroll_frame_detail_left.pack(fill='both', expand=True)
        # Right Slide Show
        self.slide_show_form = SlideControl(self, 1, 0.5, options={
            'rely': 0.1,
            'relheight': 0.8,
        }, time_duration=0.01, direction='-x')
        # self.slide_show_form.animate_forward()
        self.scroll_frame_form = CTkFrame(self.slide_show_form, border_width=5)
        self.scroll_frame_form.pack(fill='both', expand=True)
        self.init_ui_form_register_thesis()

        # --------------- Action ---------------
        self.frame_action = CTkFrame(self.content_home)
        self.frame_action.pack(fill='both', pady=5, expand=True)

        self.button_register_thesis = CTkButton(self.frame_action, text='Register Thesis', image=AssetUtil.get_icon('plus-circle'), command=lambda: self.slide_show_form.animate())
        self.button_register_thesis.pack(pady=5, padx=5, side='left')
        # print(self.account.role)
        #----------------- End Tab Home -----------------

        '''
            Tab Group:
        '''

        self.tab_view_content.add(f'Group')
        self.content_group = CTkFrame(self.tab_view_content.tab(f'Group'))
        self.content_group.pack(fill='both', expand=True)
        self.tab_group_ui = TabGroupUI(self.content_group, self.account, self)

        '''
            Tab Grade:
        '''

        self.tab_view_content.add(f'Grade')
        self.content_grade = CTkFrame(self.tab_view_content.tab(f'Grade'))
        self.content_grade.pack(fill='both', expand=True)
        self.tab_grade_ui = TabGradeUI(self.content_grade, self.account)

        
        
        # --------------- Event ---------------
        self.tab_view_content._command = self.event_change_tab


    def event_change_tab(self, selected_tab = None):
        if selected_tab != None:
            self.tab_view_content.set(selected_tab)

        if self.tab_view_content.get() == 'Home':
            self.table_view_home.update_values(self.get_values_thesis(self.thesis_dao.get_all()))
            # print('Home')
        elif self.tab_view_content.get() == 'Group':
            self.tab_group_ui.init_ui()

        elif self.tab_view_content.get() == 'Grade':
            self.tab_grade_ui.init_ui()
            # print('Grade')    



    def get_values_thesis(self, thesis_list: List[Thesis]=[]):
        data = [[thesis.id, thesis.name, self.get_tech_cate_thesis(thesis),self.get_detail_info_thesis(thesis), thesis.account.name, self.get_number_of_group(thesis)] for thesis in thesis_list if thesis.account.role == 'lecturer']
        # print(data)
        return [
            ['ID', 'Name', 'Technology','Criterion','Lecturer', 'Number Of Group'],
            *data
        ]
    
    def get_detail_info_thesis(self, thesis: Thesis) -> str:
        try:
            detail_info = ''
            tech_requires = thesis.technology_requirement_list
            cnt = 0
            for tech_require in tech_requires:
                if tech_require.description.__len__() > 30:
                    detail_info += tech_require.description[:30]+'...\n'
                else:
                    detail_info += tech_require.description
            return detail_info
        except Exception as e:
            print('Error: ' + str(e))
            return 'No Found'
        
    def get_number_of_group(self, thesis: Thesis) -> int:
        return thesis.group_list.__len__()
    
    def get_tech_cate_thesis(self, thesis: Thesis) -> str:
        try:
            tech_cate = ''
            tech_cates = thesis.technology_category_list
            cnt = 0
            for tech in tech_cates:
                tech_cate += tech.name + ','
                cnt += 1
                if cnt == 2:
                    tech_cate += '\n'
                    cnt = 0
            return tech_cate
        except Exception as e:
            print('Error: ' + str(e))
            return 'No Found'
    
    def selected_cell_thesis(self, *args):
        data = {
            'row': args[0].get('row'),
            'column': args[0].get('column'),
            'value': args[0].get('value')
        }
        return data
    
    def show_detail_thesis(self, *args):
        data = self.selected_cell_thesis(*args)
        selected_row = self.table_view_home.select_row(data.get('row'))
        thesis_id = selected_row[0]
        # Get data from database
        self.selected_thesis = self.thesis_dao.get(int(thesis_id))
        # create slide control

        self.slide_show_detail.animate()
        #- Show Detail Thesis
        self.init_ui_show_detail_thesis()
        self.table_view_home.deselect_row(data.get('row'))


    def init_ui_form_register_thesis(self):
        if hasattr(self, 'detail_right_frame'):
            self.detail_right_frame.destroy()
        #----------------- Detail Right -----------------
        self.detail_right_frame = CTkFrame(self.scroll_frame_form,)
        self.detail_right_frame.pack(fill='both', expand=True, padx=5, pady=5)
        self._scroll_frame_form = CTkScrollableFrame(self.detail_right_frame)
        self._scroll_frame_form.pack(fill='both', expand=True)
        #----------------- Form Register Thesis -----------------
        self.form_register_frame = CTkFrame(self._scroll_frame_form)
        self.form_register_frame.pack(fill='both', expand=True, padx=5, pady=5)
        # Header
        self.header_frame_register = CTkFrame(self.form_register_frame)
        self.header_frame_register.pack(fill='x', pady=5, padx=5)

        self.label_register = CTkLabel(self.header_frame_register, text='Register Thesis')
        self.label_register.pack(fill='x', pady=5, side='left', padx=5)
        self.button_close_register = CTkButton(self.header_frame_register, text='', image=AssetUtil.get_icon('x-circle'), command=lambda: self.slide_show_form.animate())
        self.button_close_register.pack(fill='x', pady=5, side='right', padx=5)
        # Name Thesis
        self.name_thesis_frame = CTkFrame(self.form_register_frame)
        self.name_thesis_frame.pack(fill='x', pady=5, padx=5)
        self.name_thesis_label = CTkLabel(self.name_thesis_frame, text='Name Thesis')
        self.name_thesis_label.pack(side='left', padx=5, pady=5)
        self.name_thesis_entry = CTkEntry(self.name_thesis_frame)
        self.name_thesis_entry.pack(side='right', fill='x', expand=True, padx=5, pady=5)
        # Technology Category
        self.tech_cate_frame = CTkFrame(self.form_register_frame)
        self.tech_cate_frame.pack(fill='x', pady=5, padx=5)
        self.tech_cate_label = CTkLabel(self.tech_cate_frame, text='Technology Category')
        self.tech_cate_label.pack(fill='x', padx=5, pady=5)
        self.scroll_frame_tech_cate = CTkScrollableFrame(self.tech_cate_frame,)
        self.scroll_frame_tech_cate.pack(fill='x', padx=5, pady=5)
        self.tech_cate_data = [tech_cate.name for tech_cate in self.tech_cate_dao.get_all()]
        self.all_tech_option=[]
        self.selection_tech_value = []
        for tech_cate in self.tech_cate_data:
            self.tech_cate_option = CTkCheckBox(self.scroll_frame_tech_cate, text=tech_cate, command=lambda category=tech_cate: self.selected_tech_cate(category))
            self.all_tech_option.append(self.tech_cate_option)
            self.tech_cate_option.pack(fill='x', padx=5, pady=5)
        # Description for Thesis
        self.description_frame = CTkFrame(self.form_register_frame)
        self.description_frame.pack(fill='x', pady=5, padx=5)
        self.description_label = CTkLabel(self.description_frame, text='Description')
        self.description_label.pack(fill='x', padx=5, pady=5)
        self.description_entry = CTkTextbox(self.description_frame, height=200)
        self.description_entry.pack(fill='x', expand=True, padx=5, pady=5)
        # Select Teacher
        list_teacher = [f'{account.id} - {account.name}' for account in self.account_dao.get_all() if account.role == 'lecturer']
        self.menu_lecture = CTkOptionMenu(self.form_register_frame, values=list_teacher,)
        self.menu_lecture.pack(fill='x', pady=5, padx=5)
        # Button Register
        self.btn_reg_frame = CTkFrame(self.form_register_frame)
        self.btn_reg_frame.pack(fill='x', pady=5, padx=5)
        self.button_register = CTkButton(self.btn_reg_frame, text='Register', image=AssetUtil.get_icon('send'), height=50, command=lambda : AccountUtil.on_send_btn_register_thesis(self.name_thesis_entry.get(), self.selection_tech_value, self.description_entry.get("0.0", "end"), self.menu_lecture.get()))
        self.button_register.pack(fill='x', pady=5, padx=5)

    def init_ui_show_detail_thesis(self):
        
        if hasattr(self, 'intro_detail_left_frame'):
            self.intro_detail_left_frame.destroy()
        # --------------- Detail Left ---------------
        '''
            Base on:
                - Frame: self.scroll_frame_detail_left
                - Data: self.selected_thesis
        '''
        # Intro Detail Left Frame
        self.intro_detail_left_frame = CTkFrame(self.scroll_frame_detail_left, height=500)
        self.intro_detail_left_frame.pack(fill='both', pady=5, padx=5, expand=True)

        # Inner Header Frame
        self.inner_header_frame_detail = CTkFrame(self.intro_detail_left_frame)
        self.inner_header_frame_detail.pack(fill='x', pady=5, padx=5)

        self.label_inner_header = CTkLabel(self.inner_header_frame_detail, text='Detail Thesis')
        self.label_inner_header.pack(side='left', padx=5, pady=5, fill='x')

        self.button_back = CTkButton(self.inner_header_frame_detail, text='', command=lambda: self.slide_show_detail.animate_backwards(), image=AssetUtil.get_icon('x-circle'))
        self.button_back.pack(side='right', padx=5, pady=5)


        # Intro Frame CTN:
        # self.intro_frame = CTkFrame(self.intro_detail_left_frame)
        # self.intro_frame.pack(fill='x', pady=5, padx=5, side='top')
    
        # Avatar Frame:
        # self.avatar_frame = CTkFrame(self.intro_frame)
        # self.avatar_frame.pack(fill='y', pady=5, padx=5, side='left')
        
        # self.ctn_avatar_frame = CTkFrame(self.avatar_frame)
        # self.ctn_avatar_frame.pack(padx=5, pady=5)

        # self.label_avatar = CTkLabel(self.ctn_avatar_frame, text='', image=AssetUtil.get_icon('user'),)
        # self.label_avatar.pack(padx=5, pady=5, fill='x')

        # self.label_name_lecturer = CTkLabel(self.ctn_avatar_frame, text=f'Lecturer:\n{self.selected_thesis.account.name}')
        # self.label_name_lecturer.pack(padx=5, pady=5, fill='x')
        # ------------------------------------------------------

        # Intro Detail Left Frame:
        # self.inner_intro_detail_left_frame = CTkScrollableFrame(self.intro_frame)
        # self.inner_intro_detail_left_frame.pack(fill='both', pady=5, padx=5)

        # Body Intro Detail Frame:
        self.scroll_detail_thesis = CTkScrollableFrame(self.intro_detail_left_frame, height=500)
        self.scroll_detail_thesis.pack(fill='both', pady=5, padx=5, expand=True)

        self.ctn_critias_requirement_frame = CTkFrame(self.scroll_detail_thesis)
        self.ctn_critias_requirement_frame.pack(fill='x')

        self.label_critias_requirement = CTkLabel(self.ctn_critias_requirement_frame, text='Criteria Requirement')
        self.label_critias_requirement.pack(fill='x', pady=5)

        # self.criterion_frame = CTkScrollableFrame(self.ctn_critias_requirement_frame, height=20)
        # self.criterion_frame.pack(fill='x', pady=5, side='top')

        for criterion in self.selected_thesis.criteria_list:
            self.label_criterion_line = CTkLabel(self.scroll_detail_thesis, text=criterion.description)
            self.label_criterion_line.pack(fill='x', pady=5)
        # --------------------------- Technology Requirement ---------------------------
        self.ctn_tech_requirement_frame = CTkFrame(self.scroll_detail_thesis)
        self.ctn_tech_requirement_frame.pack(fill='x')

        self.label_tech_requirement = CTkLabel(self.ctn_tech_requirement_frame, text='Technology Requirement')
        self.label_tech_requirement.pack(fill='x', pady=5)

        # self.tech_requirement_frame = CTkScrollableFrame(self.ctn_tech_requirement_frame, height=20)
        # self.tech_requirement_frame.pack(fill='x', pady=5, side='top')

        for tech_require in self.selected_thesis.technology_requirement_list:
            self.label_tech_require_line = CTkLabel(self.scroll_detail_thesis, text=tech_require.name)
            self.label_tech_require_line.pack(fill='x', pady=5)

        # Section Register Group
        # self.ctn_register_group_frame = CTkFrame(self.scroll_detail_thesis)
        # self.ctn_register_group_frame.pack(fill='x', pady=5, padx=5)

        # self.label_register_group = CTkLabel(self.ctn_register_group_frame, text='Register Group')
        # self.label_register_group.pack(fill='x', pady=5)

        # self.register_group = CTkFrame(self.ctn_register_group_frame)
        # self.register_group.pack(fill='x', pady=5)

        self.button_out_group = None
        # List All Group in Register Group
        for group in self.selected_thesis.group_list:

            self.group_frame = CTkFrame(self.scroll_detail_thesis)
            self.group_frame.pack(fill='x', pady=5, padx=5)

            self.label_group = CTkLabel(self.group_frame, text=f'Group {group.id}')
            self.label_group.pack(side='left', padx=10, pady=10)

            self.label_amount_member = CTkLabel(self.group_frame, text=f'Member: {group.account_list.__len__()}/ {AccountUtil.max_member}')
            self.label_amount_member.pack(side='left', padx=5)


            self.button_register_group = CTkButton(self.group_frame, text='Register', command=lambda group=group, label=self.label_amount_member, btn_cancel_state=self.button_out_group: AccountUtil.on_join_group(group, self.account, label, btn_cancel_state))
            self.button_register_group.pack(side='right',padx=10, pady=10)

            self.button_out_group = CTkButton(self.group_frame, text='Out', command=lambda group=group, label=self.label_amount_member, btn_cancel_state=self.button_out_group: AccountUtil.on_out_group(group, self.account, label, btn_cancel_state))
            self.button_out_group.pack(side='right',padx=10, pady=10)

        # print('Show Detail Thesis')
        self.after(1000, self.slide_show_detail.animate_forward)

    def selected_tech_cate(self, category):
        for option in self.all_tech_option:
            if option.cget('text') == category:
                if option.get() == 1:
                    self.selection_tech_value.append(category)
                else:
                    if category in self.selection_tech_value:
                        self.selection_tech_value.remove(category)
        # print(self.selection_tech_value)
        return self.selection_tech_value



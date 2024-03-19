from app.setting.setting import *
from app.custom.TableView import TableView
from app.db.main import *
from app.utils.main import AssetUtil
from app.asset.styles.style import *


class BodyMain(CTkFrame):

    def __init__(self, parent, **kwargs):
        super().__init__(parent.body, **kwargs)
        self.parent = parent
        self.pack(fill='both', expand=True)
        # --------------- DAO ---------------
        self.thesis_dao = ThesisDAO()
        self.tech_require_dao = TechnologyRequirementDAO()
        self.tech_cate_dao = TechnologyCategoryDAO()
        self.group_dao = GroupDAO()
        # --------------- Init UI ---------------
        self.init_ui()

    def init_ui(self):
        # --------------- Menu Bar ---------------
        self.menu_bar = CTkFrame(self, width=200)
        self.menu_bar.pack(side='left', fill='y', padx=(0, 5))
        self.button_home = CTkButton(self.menu_bar, text='', image=AssetUtil.get_icon('home'), **BUTTON_PRIMARY_STYLE)
        self.button_home.pack(fill='x', pady=(0,5), padx=(0,5))
        
        # --------------- Content ---------------
        # Tab
        self.tab_view_content = CTkTabview(self)
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
        self.search_button = CTkButton(self.search_frame, text='',image=AssetUtil.get_icon('search'), **BUTTON_PRIMARY_STYLE)
        self.search_button.pack(side='right', padx=(5, 0))
        #----------------- Table -----------------
        self.scroll_frame_table = CTkScrollableFrame(self.content_home, height=300)
        self.scroll_frame_table.pack(fill='x')
        # Get data from database
        self.data_table = self.get_values_thesis()
        # Table View
        self.table_view_home = TableView(self.scroll_frame_table, 
                                         column=self.data_table[0].__len__(), 
                                         row=self.data_table.__len__(), 
                                         header_color='#232323', 
                                         hover_color="#131313", 
                                         wraplength=2000, 
                                         command=self.show_detail_thesis,
                                         )
        self.table_view_home.pack(fill='x')
        self.table_view_home.update_values(self.get_values_thesis())
        # See Detail Each Thesis
        self.show_detail_frame = CTkFrame(self.content_home)
        self.show_detail_frame.pack(fill='both', pady=5, expand=True)


        #----------------- Detail Left -----------------
        self.detail_left_frame = CTkFrame(self.show_detail_frame)
        self.detail_left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        self.scroll_frame_detail_left = CTkScrollableFrame(self.detail_left_frame, fg_color=["gray85", "gray16"], bg_color='#232323')
        self.scroll_frame_detail_left.pack(fill='both', expand=True)
        self.label_detail = CTkLabel(self.scroll_frame_detail_left, text='Detail Thesis')
        self.label_detail.pack(fill='x', pady=5)

        
        #----------------- Detail Right -----------------
        self.detail_right_frame = CTkFrame(self.show_detail_frame)
        self.detail_right_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        self.scroll_frame_form = CTkScrollableFrame(self.detail_right_frame, fg_color=["gray85", "gray16"], bg_color='#232323')
        self.scroll_frame_form.pack(fill='both', expand=True)
        #----------------- Form Register Thesis -----------------
        self.form_register_frame = CTkFrame(self.scroll_frame_form, fg_color='#232323', bg_color='#232323',)
        self.form_register_frame.pack(fill='both', expand=True, padx=5, pady=5)
        self.label_register = CTkLabel(self.form_register_frame, text='Register Thesis')
        self.label_register.pack(fill='x', pady=5)
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
        self.scroll_frame_tech_cate = CTkScrollableFrame(self.tech_cate_frame, fg_color=["gray85", "gray16"], bg_color='#232323')
        self.scroll_frame_tech_cate.pack(fill='x', padx=5, pady=5)
        self.tech_cate_data = [tech_cate.name for tech_cate in self.tech_cate_dao.get_all()]
        for tech_cate in self.tech_cate_data:
            self.tech_cate_option = CTkCheckBox(self.scroll_frame_tech_cate, text=tech_cate, fg_color='#232323', bg_color='#232323', command=lambda category=tech_cate: self.selected_tech_cate(category))
            self.tech_cate_option.pack(fill='x', padx=5, pady=5)
        # Description for Thesis
        self.description_frame = CTkFrame(self.form_register_frame)
        self.description_frame.pack(fill='x', pady=5, padx=5)
        self.description_label = CTkLabel(self.description_frame, text='Description')
        self.description_label.pack(fill='x', padx=5, pady=5)
        self.description_entry = CTkTextbox(self.description_frame, height=200)
        self.description_entry.pack(fill='x', expand=True, padx=5, pady=5)
        # Button Register
        self.btn_reg_frame = CTkFrame(self.form_register_frame)
        self.btn_reg_frame.pack(fill='x', pady=5, padx=5)
        self.button_register = CTkButton(self.btn_reg_frame, **BUTTON_PRIMARY_STYLE, text='Register', image=AssetUtil.get_icon('send'), height=50)
        self.button_register.pack(fill='x', pady=5, padx=5)
        
        # Implement when click on table

        



        #----------------- Tab Account -----------------

    def get_values_thesis(self):
        data = [[thesis.id, thesis.name, self.get_detail_info_thesis(thesis), thesis.account.name, self.get_number_of_group(thesis)] for thesis in self.thesis_dao.get_all() ]
        return [
            ['ID', 'Name', 'Detail Info', 'Lecturer', 'Number Of Group'],
            *data
        ]
    
    def get_detail_info_thesis(self, thesis: Thesis) -> str:
        try:
            detail_info = ''
            criterias = thesis.criteria_list
            cnt = 0
            for criteria in criterias:
                detail_info += criteria.name + ', '
                cnt += 1
                if cnt == 5:
                    detail_info += '\n'
                    cnt = 0
            return detail_info
        except Exception as e:
            print('Error: ' + str(e))
            return 'No Found'
        
    def get_number_of_group(self, thesis: Thesis) -> int:
        cnt = 0
        for group in self.group_dao.get_all():
            if group == thesis.group:
                cnt += 1
        return cnt
    
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
        self.init_ui_show_detail_thesis()
        self.table_view_home.deselect_row(data.get('row'))

    def init_ui_show_detail_thesis(self):
        if hasattr(self, 'intro_detail_left_frame'):
            self.intro_detail_left_frame.destroy()
        # --------------- Detail Left ---------------
        '''
            Base on:
                - Frame: self.scroll_frame_detail_left
                - Data: self.selected_thesis
        '''
        self.intro_detail_left_frame = CTkFrame(self.scroll_frame_detail_left, fg_color='#232323', bg_color='#232323', )
        self.intro_detail_left_frame.pack(fill='x', pady=5, padx=5, side='top')
    
        self.avatar_frame = CTkFrame(self.intro_detail_left_frame)
        self.avatar_frame.pack(fill='x', pady=5, padx=5, side='left')

        self.label_avatar = CTkLabel(self.avatar_frame, text='', image=AssetUtil.get_icon('user'),)
        self.label_avatar.pack(padx=5, pady=5, fill='both')

        self.inner_intro_detail_left_frame = CTkFrame(self.intro_detail_left_frame, fg_color='#232323', bg_color='#232323')
        self.inner_intro_detail_left_frame.pack(fill='x', pady=5, padx=5)

    def selected_tech_cate(self, category):
        print(category)
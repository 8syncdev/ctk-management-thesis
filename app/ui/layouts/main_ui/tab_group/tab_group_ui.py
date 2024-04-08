from app.setting.setting import *
from app.custom.TableView import TableView
from app.db.main import *
from app.utils.main import *
from app.asset.styles.style import *
from app.custom.SlideControl import SlideControl
from app.custom.CalenderControl import CalenderControl

'''
    KW:
    - master: master widget
    - **kw: keyword arguments
        - loggin_account
'''


class TabGroupUI(CTkFrame):

    def __init__(self, master=None, loggin_account = None, **kw):
        super().__init__(master=master, **kw)
        self.master = master
        self.loggin_account = loggin_account
        self.pack(fill='both', expand=True)
        # ------------ Dao ------------
        self.group_dao = GroupDAO()
        self.task_dao = TaskDAO()
        self.account_dao = AccountDAO()
        # print(AccountUtil.get_joined_group(self.loggin_account))
        # ----------------- Variable -----------------
        self.selected_group = None
        if self.loggin_account.role == 'lecturer':
            self.selected_group = self.loggin_account.group_list[0]

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
        self.body_section.pack(fill='both', expand=True, side='top', padx=5, pady=(0, 5))
        self.implement_body()


    def implement_header(self):
        # ----------------- Left Header -----------------
        self.left_header = CTkFrame(self.header_section, width=300, height=50)
        self.left_header.pack(side='left', fill='x', pady=5, padx=5)

        if self.loggin_account.role=='lecturer':
            name_group = self.selected_group.name if self.selected_group != None else "No Group"

        self.label_name_group = CTkLabel(self.left_header, 
                                         text=f'Group: {AccountUtil.get_joined_group(self.loggin_account).name if AccountUtil.get_joined_group(self.loggin_account) != None and self.loggin_account.role=="student" else name_group}', 
                                         width=300)
        self.label_name_group.pack(pady=5, padx=5)

        # ----------------- Right Header -----------------
        self.right_header = CTkFrame(self.header_section, width=300, height=50)
        self.right_header.pack(side='right', fill='x', pady=5, padx=5)

        if self.loggin_account.role=='lecturer':
            self.menu_option_groups_of_lecturer = CTkOptionMenu(self.right_header, values=[group.name for group in self.loggin_account.group_list], command=self.on_change_group)
            self.menu_option_groups_of_lecturer.pack(side='right', padx=5)

    def on_change_group(self, e):
        try:
            self.implement_body()
        except Exception as e:
            print(f'Error: {e}')
            pass

    def implement_body(self):
        if AccountUtil.get_joined_group(self.loggin_account) != None:
            if hasattr(self, 'inner_body_section'):
                self.inner_body_section.destroy()
            
            self.inner_body_section = CTkFrame(self.body_section)
            self.inner_body_section.pack(fill='both', expand=True)

            self.left_body = CTkFrame(self.inner_body_section, width=400)
            self.left_body.pack(side='left', fill='y', padx=5)

            self.right_body = CTkFrame(self.inner_body_section)
            self.right_body.pack(side='right', fill='both', expand=True, padx=5)

            # ----------------- Left Body -----------------
            self.label_name_member = CTkLabel(self.left_body, text='Member:', width=400)
            self.label_name_member.pack(pady=5, padx=5)

            self.scroll_frame_show_member = CTkScrollableFrame(self.left_body, height=50)
            self.scroll_frame_show_member.pack(fill='both', expand=True, pady=5, padx=5)

            #- Show member
            get_all_memeber = AccountUtil.get_joined_group(self.loggin_account).account_list

            for member in get_all_memeber:
                CTkLabel(self.scroll_frame_show_member, text=member.name).pack(pady=5, padx=5)

            # ---------------------
            
            self.label_add_task = CTkLabel(self.left_body, text='Add Task:', width=400)
            self.label_add_task.pack(pady=5, padx=5)
            
            # --------------------- Add Task ---------------------
            self.frame_add_task = CTkFrame(self.left_body)
            self.frame_add_task.pack(fill='both', expand=True, pady=5, padx=5)

            self.label_name_task = CTkLabel(self.frame_add_task, text='Name:', width=400)
            self.label_name_task.pack()

            self.entry_name_task = CTkEntry(self.frame_add_task, width=200)
            self.entry_name_task.pack(pady=5, padx=5)

            self.label_deadline_task = CTkLabel(self.frame_add_task, text='Deadline:', width=400)
            self.label_deadline_task.pack()

            self.entry_deadline_task = CalenderControl(self.frame_add_task)
            self.entry_deadline_task.pack(pady=5, padx=5)


            self.label_progress_task = CTkLabel(self.frame_add_task, text='Progress:', width=400)
            self.label_progress_task.pack()

            self.slide_progress_task = CTkEntry(self.frame_add_task, width=200)
            self.slide_progress_task.pack(pady=5, padx=5)

            # Action Group:

            self.frame_group_action = CTkFrame(self.left_body)
            self.frame_group_action.pack(fill='both', expand=True, pady=5, padx=5)

            self.btn_add_task = CTkButton(self.frame_group_action, text='Add Task', command=self.on_add_task)
            self.btn_add_task.pack(pady=5, padx=5)

            self.frame_edit_task = CTkFrame(self.frame_group_action)
            self.frame_edit_task.pack(fill='both', expand=True, pady=5, padx=5)

            self.entry_id_task = CTkEntry(self.frame_edit_task, width=200)
            self.entry_id_task.pack(side='left', pady=5, padx=5)

            self.btn_edit_task = CTkButton(self.frame_edit_task, text='Edit Task', command=self.on_edit_task)
            self.btn_edit_task.pack(side='left', pady=5, padx=5, fill='x')


            #----------------- Right Body -----------------

            self.scroll_show_all_task = CTkScrollableFrame(self.right_body, height=300)
            self.scroll_show_all_task.pack(fill='x', pady=5, padx=5)

            # Show all task
            self.implement_show_all_task()
            

    def on_add_task(self):
        try:
            name = self.entry_name_task.get()
            deadline = self.entry_deadline_task.get_value()
            progress = self.slide_progress_task.get()

            task = Task(name=name, progress=progress, deadline=deadline)
            self.loggin_account.task_list.append(task)
            self.account_dao.update(self.loggin_account)

            self.entry_name_task.delete(0, 'end')
            self.slide_progress_task.delete(0, 'end')
            # self.init_ui()
            print('Add task success')
        except Exception as e:
            print(f'Error: {e}')
            pass

    def implement_show_all_task(self):
        try:
            get_all_member = AccountUtil.get_joined_group(self.loggin_account).account_list
            _list_task = []
            for member in get_all_member:
                if member.task_list != []:
                    for task in member.task_list:
                        _list_task.append((
                            task.id,
                            member.name,
                            task.name,
                            task.progress,
                            task.deadline
                        ))

            if hasattr(self, 'task_table_view'):
                self.task_table_view.destroy()

            self.task_table_view = CTkFrame(self.scroll_show_all_task)
            self.task_table_view.pack(fill='both', expand=True)

            for _task in _list_task:
                content_label= f'Task ID: {_task[0]}, Member: {_task[1]}, Task Name: {_task[2]}, Progress: {_task[3]}, Deadline: {_task[4]}'

                CTkLabel(self.task_table_view, text=content_label).pack(pady=5, padx=5)

                
        except Exception as e:
            print(f'Error: {e}')
            return None
        
    def on_edit_task(self):
        try:
            task_id = self.entry_id_task.get()
            for task in self.loggin_account.task_list:
                if task.id == int(task_id):
                    task.name = self.entry_name_task.get() if self.entry_name_task.get() != '' else task.name
                    task.progress = self.slide_progress_task.get() if self.slide_progress_task.get() != '' else task.progress
                    task.deadline = self.entry_deadline_task.get_value() if self.entry_deadline_task.get_value() != '' else task.deadline

                    self.account_dao.update(self.loggin_account)
                    print('Edit task success')
                    self.implement_show_all_task()
                    return
        except Exception as e:
            print(f'Error: {e}')
            pass

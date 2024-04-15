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
        self.comment_dao = CommentDAO()
        # print(AccountUtil.get_joined_group(self.loggin_account))
        # ----------------- Variable -----------------
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
        self.body_section.pack(fill='both', expand=True, side='top', padx=5, pady=(0, 5))
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
        if (self.loggin_account.role=='student' and AccountUtil.get_joined_group(self.loggin_account) != None) or self.loggin_account.role=='lecturer':
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
            get_all_memeber = AccountUtil.get_joined_group(self.loggin_account).account_list if self.loggin_account.role == 'student' else self.selected_group.account_list

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
            
            # Add member task
            if hasattr(self, 'member_task'):
                    self.member_task.destroy()

            if self.loggin_account.role == 'lecturer':
                self.label_name_member_task = CTkLabel(self.frame_add_task, text='Member:', width=400)
                self.label_name_member_task.pack(pady=5, padx=5)
                
                self.member_task = CTkOptionMenu(self.frame_add_task, values=[member.email for member in get_all_memeber], width=200)
                self.member_task.pack(pady=5, padx=5)



            # Action Group:

            self.frame_group_action = CTkFrame(self.left_body)
            self.frame_group_action.pack(fill='both', expand=True, pady=5, padx=5)

            self.btn_add_task = CTkButton(self.frame_group_action, text='Add Task', command=self.on_add_task)
            self.btn_add_task.pack(pady=5, padx=5)

            self.frame_edit_task = CTkFrame(self.frame_group_action)
            self.frame_edit_task.pack(fill='both', expand=True, pady=5, padx=5)

            self.label_id_task = CTkLabel(self.frame_edit_task, text='Task ID:', width=50)
            self.label_id_task.pack(side='left', pady=5, padx=5)

            self.entry_id_task = CTkEntry(self.frame_edit_task, width=50)
            self.entry_id_task.pack(side='left', pady=5, padx=5)

            self.btn_edit_task = CTkButton(self.frame_edit_task, text='Edit Task', command=self.on_edit_task)
            self.btn_edit_task.pack(side='left', pady=5, padx=5, fill='x')

            self.btn_delete_task = CTkButton(self.frame_edit_task, text='Delete Task', command=self.on_delete_task)
            self.btn_delete_task.pack(side='left', pady=5, padx=5, fill='x')


            #----------------- Right Body -----------------

            self.scroll_show_all_task = CTkScrollableFrame(self.right_body, height=300)
            self.scroll_show_all_task.pack(fill='both', pady=5, padx=5, expand=True)

            # Show all task
            self.implement_show_all_task()

    def on_delete_task(self):
        try:
            if self.loggin_account.role == 'student':
                task_id = self.entry_id_task.get()
                for task in self.loggin_account.task_list:
                    if task.id == int(task_id):
                        self.loggin_account.task_list.remove(task)
                        self.account_dao.update(self.loggin_account)
                        print('Delete task success')
                        self.implement_show_all_task()
                        return
            else:
                task_id = self.entry_id_task.get()
                for group_account in self.selected_group.account_list:
                    for task in group_account.task_list:
                        if task.id == int(task_id):
                            group_account.task_list.remove(task)
                            self.account_dao.update(group_account)
                            print('Delete task success')
                            self.implement_show_all_task()
                            return
        except Exception as e:
            print(f'Error: {e}')
            pass


            

    def on_add_task(self):
        try:
            if self.loggin_account.role == 'lecturer':
                member_email = self.member_task.get()
                for member in self.selected_group.account_list:
                    if member.email == member_email:
                        name = self.entry_name_task.get()
                        deadline = self.entry_deadline_task.get_value()
                        progress = self.slide_progress_task.get()

                        task = Task(name=name, progress=progress, deadline=deadline)
                        member.task_list.append(task)
                        self.account_dao.update(member)

                        self.entry_name_task.delete(0, 'end')
                        self.slide_progress_task.delete(0, 'end')
                        self.implement_show_all_task()
                        print('Add task success')
                        return
            # Student
            name = self.entry_name_task.get()
            deadline = self.entry_deadline_task.get_value()
            progress = self.slide_progress_task.get()

            task = Task(name=name, progress=progress, deadline=deadline)
            self.loggin_account.task_list.append(task)
            self.account_dao.update(self.loggin_account)

            self.entry_name_task.delete(0, 'end')
            self.slide_progress_task.delete(0, 'end')
            self.implement_show_all_task()
            print('Add task success')
        except Exception as e:
            print(f'Error: {e}')
            pass

    def get_all_task(self):
        get_all_member = AccountUtil.get_joined_group(self.loggin_account).account_list if self.loggin_account.role == 'student' else self.selected_group.account_list
        _list_task = []
        for member in get_all_member:
            if member.task_list != []:
                for task in member.task_list:
                    _list_task.append((
                        task.id,
                        member.name,
                        member.email,
                        task.name,
                        task.progress,
                        task.deadline
                    ))
        return _list_task

    def implement_show_all_task(self):
        try:
            _list_task = self.get_all_task()

            if hasattr(self, 'task_table_view'):
                self.task_table_view.destroy()

            self.task_table_view = CTkFrame(self.scroll_show_all_task)
            self.task_table_view.pack(fill='both', expand=True)

            self.list_widgets_task = []


            for _task in _list_task:
                _item_attr = {
                    'task_id': None,
                    'widget': None,
                }
                row = CTkFrame(self.task_table_view)
                row.pack(fill='x', pady=5, padx=5)

                innerr_frame = CTkFrame(row)
                innerr_frame.pack(fill='x', pady=5, padx=5, side='top')

                content_label= f'Task ID: {_task[0]}, Name: {_task[1]}|{_task[2]}, Task: {_task[3]}\n Progress: {_task[4]}, Deadline: {_task[5]}'

                CTkLabel(innerr_frame, text=content_label, anchor='w').pack(pady=5, padx=5, side='left')

                right_frame = CTkFrame(innerr_frame)
                right_frame.pack(side='right', fill='x', pady=5, padx=5)

                btn_add_comment = CTkButton(right_frame, text='', command=lambda task_id=_task[0]: self.on_add_comment(task_id), image=AssetUtil.get_icon('edit'), width=40, height=40)
                btn_add_comment.pack(pady=5, padx=5, side='right')

                btn_delete_task = CTkButton(right_frame, text='', command=lambda task_id=_task[0]: self.on_delete_task(task_id), image=AssetUtil.get_icon('delete'), width=40, height=40, fg_color='red')
                btn_delete_task.pack(pady=5, padx=5, side='right')

                # Update item attribute for each row to add comment items.
                _item_attr['task_id'] = _task[0]
                _item_attr['widget'] = row
                self.list_widgets_task.append(_item_attr)

            if hasattr(self, 'frame_evalute_task'):
                self.frame_evalute_task.destroy()
            
            self.frame_evalute_task = CTkFrame(self.right_body)
            self.frame_evalute_task.pack(fill='x', side='bottom', pady=5, padx=5)

            self.frame_progress_task = CTkFrame(self.frame_evalute_task)
            self.frame_progress_task.pack(fill='x', pady=5, padx=5)

            list_progress = [task[4] for task in _list_task]
            self.label_id_task = CTkLabel(self.frame_progress_task, text=f'Progress Task : {sum(list_progress)/list_progress.__len__()}', width=400, font=('Arial', 17, 'bold'), text_color='green')
            self.label_id_task.pack(pady=5, padx=5, side='left')

            # if hasattr(self, 'frame_evalute_task'):
            #     self.frame_evalute_task.destroy()

            # if self.loggin_account.role == 'lecturer':
            #     self.frame_evalute_task = CTkFrame(self.right_body)
            #     self.frame_evalute_task.pack(fill='both', expand=True, pady=5, padx=5)

            #     self.label_id_task = CTkLabel(self.frame_evalute_task, text='Task ID:', width=400)
            #     self.label_id_task.pack()

            #     self.entry_id_task = CTkEntry(self.frame_evalute_task, width=200)
            #     self.entry_id_task.pack(pady=5, padx=5)

            #     self.btn_evalute_task = CTkButton(self.frame_evalute_task, text='Evalute Task', command=self.on_evalute_task)
            #     self.btn_evalute_task.pack(pady=5, padx=5)




                
        except Exception as e:
            print(f'Error: {e}')
            return None
        
    def on_add_comment(self, task_id):
        try:
            get_all_comment_of_task = [comment for comment in self.comment_dao.get_all() if comment.task_id == task_id]
            # if get_all_comment_of_task != []:
            #     self.init_ui_comments_for_task(get_all_comment_of_task, task_id)

            get_row = [item for item in self.list_widgets_task if item['task_id'] == task_id]
            if get_row != []:
                row = get_row[0]['widget']
                # row.configure(height=500)
                # row.update()

                if not hasattr(row, 'frame_comment') or row.open==False:
                    print('Add comment success')
                    row.open = True

                    row.frame_comment = CTkFrame(row, height=500)
                    row.frame_comment.pack(fill='both', pady=5, padx=5, expand=True)

                    row_show_comment = CTkScrollableFrame(row.frame_comment, height=400)
                    row_show_comment.pack(fill='both', pady=5, padx=5, expand=True)

                    row_add_comment = CTkFrame(row.frame_comment)
                    row_add_comment.pack(fill='x', pady=(0,5), padx=5, side='bottom')

                    row.btn_add_comment = CTkButton(row_add_comment, text='', command=lambda: self.on_add_comment_task(self.task_dao.get(task_id), self.loggin_account, row), image=AssetUtil.get_icon('upload'), width=40, height=40)
                    row.btn_add_comment.pack(pady=5, padx=5, side='right', fill='x')

                    row.entry_comment = CTkTextbox(row_add_comment, height=50, width=500)
                    row.entry_comment.pack(pady=5, padx=5, side='right', fill='x')

                    # Override scroll_frame_comment to row
                    print(get_all_comment_of_task)
                    if get_all_comment_of_task == []:
                        ...

                else:
                    print('Remove comment success')
                    row.frame_comment.destroy()
                    row.open = False

        except Exception as e:
            print(f'Error: {e}')
            pass
        
    def on_add_comment_task(self, task, account, current_row):
        try:
            if current_row.entry_comment.get('1.0', 'end-1c') != '':
                comment = Comment(content=current_row.entry_comment.get('1.0', 'end-1c'), account_id=account.id)
                self.comment_dao.create(comment)

                task.comment_list.append(comment)
                self.task_dao.update(task)
                print('Add comment success')
        except Exception as e:
            print(f'Error: {e}')
            pass
    def on_evalute_task(self):
        try:
            ...            

        except Exception as e:
            print(f'Error: {e}')
            pass

    def on_edit_task(self):
        try:
            if self.loggin_account.role == 'student':
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
            else:
                task_id = self.entry_id_task.get()
                for group_account in self.selected_group.account_list:
                    for task in group_account.task_list:
                        if task.id == int(task_id):
                            task.name = self.entry_name_task.get() if self.entry_name_task.get() != '' else task.name
                            task.progress = self.slide_progress_task.get() if self.slide_progress_task.get() != '' else task.progress
                            task.deadline = self.entry_deadline_task.get_value() if self.entry_deadline_task.get_value() != '' else task.deadline

                            self.account_dao.update(group_account)
                            print('Edit task success')
                            self.implement_show_all_task()
                            return
        except Exception as e:
            print(f'Error: {e}')
            pass

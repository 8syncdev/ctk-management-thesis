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

    def __init__(self, master=None, loggin_account = None, base_master = None, **kw):
        super().__init__(master=master, **kw)
        self.master = master
        self.base_master = base_master
        self.loggin_account = loggin_account
        self.pack(fill='both', expand=True)
        # ------------ Dao ------------
        self.group_dao = GroupDAO()
        self.task_dao = TaskDAO()
        self.account_dao = AccountDAO()
        self.comment_dao = CommentDAO()
        # print(AccountUtil.get_joined_group(self.loggin_account))
        # ----------------- Variable -----------------
        

        self.init_ui()

    def init_ui(self):
        self.selected_group = AccountUtil.get_joined_group(self.loggin_account) if AccountUtil.get_joined_group(self.loggin_account) != None else None
        if self.loggin_account.role == 'lecturer':
            self.selected_group = AccountUtil.get_all_group_of_thesis(self.loggin_account)[0] if AccountUtil.get_all_group_of_thesis(self.loggin_account) != [] else None
        self.selected_theis = AccountUtil.get_thesis_of_selected_group(self.selected_group) if self.selected_group != None else None
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
        if hasattr(self, 'left_header'):
            self.left_header.destroy()
        self.left_header = CTkFrame(self.header_section, width=300, height=50)
        self.left_header.pack(side='left', fill='x', pady=5, padx=5)

        if self.loggin_account.role=='lecturer':
            name_group = self.selected_group.name if self.selected_group != None else "No Group"
        else:
            name_group = AccountUtil.get_joined_group(self.loggin_account).name if AccountUtil.get_joined_group(self.loggin_account) != None else "No Group"
        self.label_name_group = CTkLabel(self.left_header, 
                                         text=f'Group: {AccountUtil.get_joined_group(self.loggin_account).name if AccountUtil.get_joined_group(self.loggin_account) != None and self.loggin_account.role=="student" else name_group}', 
                                         width=50)
        self.label_name_group.pack(pady=5, padx=5, side='left')

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
            self.slide_show_group_task.animate_backwards()
            get_all_group = AccountUtil.get_all_group_of_thesis(self.loggin_account, self.selected_theis)
            # print([group.name for group in get_all_group])
            # print(self.menu_option_groups_of_lecturer.get())
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
        if (self.loggin_account.role=='student' and AccountUtil.get_joined_group(self.loggin_account) != None) or self.loggin_account.role=='lecturer':
            if hasattr(self, 'inner_body_section'):
                self.inner_body_section.destroy()
            
            self.inner_body_section = CTkFrame(self.body_section)
            self.inner_body_section.pack(fill='both', expand=True)

            self.left_body = CTkFrame(self.inner_body_section, width=200)
            self.left_body.pack(side='left', fill='y', padx=5,)

            CTkLabel(self.left_body, text='Action Task', width=200).pack(pady=5, padx=5)

            self.button_open_slide_show_group_task = CTkButton(self.left_body, text='Group Task', command=self.on_open_slide_show_group_task)
            self.button_open_slide_show_group_task.pack(pady=5, padx=5)

            self.slide_show_group_task = SlideControl(self.base_master, -0.5, 0, options={
                'rely': 0.1,
                'relheight': 0.8,
            }, time_duration=0.01)

            self.inner_left_body = CTkScrollableFrame(self.slide_show_group_task, border_width=5)
            self.inner_left_body.pack(fill='both', expand=True)

            header_row = CTkFrame(self.inner_left_body)
            header_row.pack(fill='x', pady=5, padx=5)

            button_close = CTkButton(header_row, text='', image=AssetUtil.get_icon('x'), width=40, height=40, fg_color='red',command=self.on_open_slide_show_group_task)
            button_close.pack(side='right', pady=5, padx=5)

            self.right_body = CTkFrame(self.inner_body_section)
            self.right_body.pack(side='right', fill='both', expand=True, padx=5)

            # ----------------- Left Body -----------------
            self.label_name_member = CTkLabel(self.inner_left_body, text='Member:', width=400)
            self.label_name_member.pack(pady=5, padx=5)

            self.scroll_frame_show_member = CTkScrollableFrame(self.inner_left_body, height=50)
            self.scroll_frame_show_member.pack(fill='both', expand=True, pady=5, padx=5)

            #- Show member
            get_all_memeber = AccountUtil.get_joined_group(self.loggin_account).account_list if self.loggin_account.role == 'student' else self.selected_group.account_list.remove(self.loggin_account) if self.loggin_account in self.selected_group.account_list else self.selected_group.account_list

            for member in get_all_memeber:
                CTkLabel(self.scroll_frame_show_member, text=member.name).pack(pady=5, padx=5)

            # ---------------------
            
            self.label_add_task = CTkLabel(self.inner_left_body, text='Add Task:', width=400)
            self.label_add_task.pack(pady=5, padx=5)
            
            # --------------------- Add Task ---------------------
            self.frame_add_task = CTkFrame(self.inner_left_body)
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

            self.slide_progress_task = CTkSlider(self.frame_add_task, to=100, from_=0, width=200)
            self.slide_progress_task.pack(pady=5, padx=5)
            
            # Add member task
            if hasattr(self, 'member_task'):
                    self.member_task.destroy()

            if self.loggin_account.role == 'lecturer' and get_all_memeber != []:
                self.label_name_member_task = CTkLabel(self.frame_add_task, text='Member:', width=400)
                self.label_name_member_task.pack(pady=5, padx=5)
                
                self.member_task = CTkOptionMenu(self.frame_add_task, values=[member.email for member in get_all_memeber], width=200)
                self.member_task.pack(pady=5, padx=5)



            # Action Group:

            self.frame_group_action = CTkFrame(self.inner_left_body)
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

            # self.btn_delete_task = CTkButton(self.frame_edit_task, text='Delete Task', command=self.on_delete_task)
            # self.btn_delete_task.pack(side='left', pady=5, padx=5, fill='x')


            #----------------- Right Body -----------------

            self.scroll_show_all_task = CTkScrollableFrame(self.right_body, height=300)
            self.scroll_show_all_task.pack(fill='both', pady=5, padx=5, expand=True)

            # Show all task
            self.implement_show_all_task()

    def on_open_slide_show_group_task(self):
        self.slide_show_group_task.animate()

    def on_delete_task(self, row, task_id=None):
        print('Delete task')
        print(task_id)
        print([task.id for task in self.loggin_account.task_list])
        try:
            task_id = self.entry_id_task.get() if task_id == None else task_id
            for account in self.account_dao.get_all():
                for task in account.task_list:
                    if task.id == int(task_id):
                        account.task_list.remove(task)
                        self.account_dao.update(account)
                        self.task_dao.delete(task)
                        # print('Delete task success')
                        row.destroy()
                        return
        except Exception as e:
            print(f'Error: {e}')
            pass


            

    def on_add_task(self):
        try:
            if self.loggin_account.role == 'lecturer':
                if self.selected_group.account_list == []:
                    name = self.entry_name_task.get()
                    deadline = self.entry_deadline_task.get_value()
                    progress = self.slide_progress_task.get()

                    task = Task(name=name, progress=progress, deadline=deadline)
                    # task.account_list.append(self.loggin_account)
                    self.loggin_account.task_list.append(task)
                    self.account_dao.update(self.loggin_account)
                    self.selected_group.task_list.append(task)
                    self.group_dao.update(self.selected_group)

                    self.entry_name_task.delete(0, 'end')
                    # self.slide_progress_task.delete(0, 'end')
                    self.implement_show_all_task()
                    return
                member_email = self.member_task.get()
                for member in self.selected_group.account_list:
                    if member.email == member_email:
                        name = self.entry_name_task.get()
                        deadline = self.entry_deadline_task.get_value()
                        progress = self.slide_progress_task.get()

                        task = Task(name=name, progress=progress, deadline=deadline)
                        task.account_list.append(member)
                        self.account_dao.update(member)
                        self.selected_group.task_list.append(task)
                        self.group_dao.update(self.selected_group)

                        self.entry_name_task.delete(0, 'end')
                        # self.slide_progress_task.delete(0, 'end')
                        self.implement_show_all_task()
                        # print('Add task success')
                        return
            # Student
            name = self.entry_name_task.get()
            deadline = self.entry_deadline_task.get_value()
            progress = self.slide_progress_task.get()

            task = Task(name=name, progress=progress, deadline=deadline)
            # task.account_list.append(self.loggin_account)
            self.loggin_account.task_list.append(task)
            self.account_dao.update(self.loggin_account)
            self.selected_group.task_list.append(task)
            self.group_dao.update(self.selected_group)

            self.entry_name_task.delete(0, 'end')
            # self.slide_progress_task.delete(0, 'end')
            self.implement_show_all_task()
            # print('Add task success')
        except Exception as e:
            print(f'Error: {e}')
            pass

    def get_all_task(self):
        # get_all_member = AccountUtil.get_joined_group(self.loggin_account).account_list if self.loggin_account.role == 'student' else self.selected_group.account_list
        # _list_task = []
        # for member in get_all_member:
        #     if member.task_list != []:
        #         for task in member.task_list:
        #             _list_task.append((
        #                 task.id,
        #                 member.name,
        #                 member.email,
        #                 task.name,
        #                 task.progress,
        #                 task.deadline
        #             ))
        # return _list_task
        get_all_task_of_group = self.selected_group.task_list
        _list_task = []
        for task in get_all_task_of_group:
            if task.account_list != []:
                    _list_task.append((
                        task.id,
                        task.account_list[0].name,
                        task.account_list[0].email,
                        task.name,
                        task.progress,
                        task.deadline
                    ))   
        print(self.selected_group.name)
        print(_list_task)
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

                content_label= f'Task ID: {_task[0]}, Author Task: {_task[1]}\nEmail:{_task[2]}\nTask: {_task[3]}\n Progress: {_task[4]}, Deadline: {_task[5]}'

                CTkLabel(innerr_frame, text=content_label, anchor='w', width=200, font=get_style('font_bold'), text_color=get_style('dark_active')).pack(pady=5, padx=5, side='left')

                contant_participant = '\n'.join([account.name for account in self.task_dao.get(_task[0]).account_list if account.role == 'student'])
                label_participant = CTkLabel(innerr_frame, text=f'Participant:\n{contant_participant}', width=200, font=get_style('font_italic'), text_color=get_style('secondary_active'))
                label_participant.pack(pady=5, padx=5, side='left')

                right_frame = CTkFrame(innerr_frame)
                right_frame.pack(side='right', fill='x', pady=5, padx=5)

                btn_add_comment = CTkButton(right_frame, text='', command=lambda task_id=_task[0]: self.on_add_comment(task_id), image=AssetUtil.get_icon('edit'), width=40, height=40)
                btn_add_comment.pack(pady=5, padx=5, side='right')

                btn_delete_task = CTkButton(right_frame, text='', command=lambda row=row, task_id=_task[0]: self.on_delete_task(row, task_id), image=AssetUtil.get_icon('delete'), width=40, height=40, fg_color='red')
                btn_delete_task.pack(pady=5, padx=5, side='right')

                btn_get_task = CTkButton(right_frame, text='', command=lambda task_id=_task[0], label_participant=label_participant: self.on_get_task(task_id, label_participant), image=AssetUtil.get_icon('target'), width=40, height=40)
                btn_get_task.pack(pady=5, padx=5, side='right')

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
            self.label_id_task = CTkLabel(self.frame_progress_task, text=f'Progress Task : {sum(list_progress)/list_progress.__len__() if list_progress.__len__()!=0 else 0}', width=400, font=('Arial', 17, 'bold'), text_color='green')
            self.label_id_task.pack(pady=5, padx=5, side='left')
                
        except Exception as e:
            print(f'Error: {e}')
            return None
        

    def on_get_task(self, task_id, label_participant):
        try:
            get_task = self.task_dao.get(task_id)
            if get_task in self.loggin_account.task_list:
                self.loggin_account.task_list.remove(get_task)
            else:
                self.loggin_account.task_list.append(get_task)
            self.account_dao.update(self.loggin_account)

            content_participant = '\n'.join([account.name for account in get_task.account_list if account.role == 'student'])
            label_participant.configure(text=f'Participant:\n{content_participant}')
            #  1 task has many account
        except Exception as e:
            print(f'Error: {e}')
            pass

    def on_add_comment(self, task_id):
        try:
            get_all_comment_of_task = [comment for comment in self.task_dao.get(task_id).comment_list]
            # if get_all_comment_of_task != []:
            #     self.init_ui_comments_for_task(get_all_comment_of_task, task_id)

            get_row = [item for item in self.list_widgets_task if item['task_id'] == task_id]
            if get_row != []:
                row = get_row[0]['widget']
                # row.configure(height=500)
                # row.update()

                if not hasattr(row, 'frame_comment') or row.open==False:
                    # print('Add comment success')
                    row.open = True

                    row.frame_comment = CTkFrame(row, height=500)
                    row.frame_comment.pack(fill='both', pady=5, padx=5, expand=True)

                    row.row_show_comment = CTkScrollableFrame(row.frame_comment, height=400)
                    row.row_show_comment.pack(fill='both', pady=5, padx=5, expand=True)

                        # Create row for comment
                    if hasattr(row, 'wrapper_comment'):
                        row.wrapper_comment.destroy()

                    row.wrapper_comment = CTkFrame(row.row_show_comment)
                    row.wrapper_comment.pack(fill='both', expand=True)

                    row.row_add_comment = CTkFrame(row.frame_comment)
                    row.row_add_comment.pack(fill='x', pady=(0,5), padx=5, side='bottom')

                    row.btn_add_comment = CTkButton(row.row_add_comment, text='', command=lambda: self.on_add_comment_task(self.task_dao.get(task_id), self.loggin_account, row), image=AssetUtil.get_icon('upload'), width=40, height=40)
                    row.btn_add_comment.pack(pady=5, padx=5, side='right', fill='x')

                    row.entry_comment = CTkTextbox(row.row_add_comment, height=50, width=500)
                    row.entry_comment.pack(pady=5, padx=5, side='right', fill='x')

                    # Override scroll_frame_comment to row
                    # print(get_all_comment_of_task)
                    if get_all_comment_of_task != []:
                        self.init_ui_comments_for_task(get_all_comment_of_task, row)

                else:
                    # print('Remove comment success')
                    row.frame_comment.destroy()
                    row.open = False

        except Exception as e:
            print(f'Error: {e}')
            pass
    
    def init_ui_row_comment(self, comment, row):
        try:
            # Add comment to row
            row_comment = CTkFrame(row.wrapper_comment)
            row_comment.pack(fill='x')

            if self.loggin_account.id == comment.account_id:
                line_comment = CTkFrame(row_comment)
                line_comment.pack(pady=5, padx=5, side='right')
            else:
                line_comment = CTkFrame(row_comment, width=300)
                line_comment.pack(side='left', pady=5, padx=5)

            frame_wrap_avatar = CTkFrame(line_comment)
            frame_wrap_avatar.pack(side='left', padx=5, pady=5)

            CTkLabel(frame_wrap_avatar,text='', image=AssetUtil.get_icon('user', resize=(20,20)) if self.loggin_account.path_img == None else pillow_image_open(self.loggin_account.path_img).resize(20,20)).pack(pady=5, padx=5, side='left')

            CTkLabel(frame_wrap_avatar, text=self.account_dao.get(comment.account_id).name).pack(side='left', padx=5)

            CTkLabel(line_comment, text=f'{comment.content}',).pack(pady=5, padx=15, side='left')

            # Add delete comment when if this is current account
            if self.loggin_account.id == comment.account_id:
                right_frame = CTkFrame(line_comment)
                right_frame.pack(side='right', fill='x', pady=5, padx=5)

                btn_delete_comment = CTkButton(right_frame, text='', command=lambda comment=comment, row_comment=row_comment: self.on_delete_comment(comment, row_comment), image=AssetUtil.get_icon('x-circle'), width=25, height=25, fg_color='red')
                btn_delete_comment.pack(pady=5, padx=5, side='right')
                # print('Add comment success')
        except Exception as e:
            print(f'Error: {e}')
            pass

    def init_ui_comments_for_task(self, get_all_comment_of_task, row):
        try:
            if hasattr(row, 'wrapper_comment'):
                    row.wrapper_comment.destroy()

            row.wrapper_comment = CTkFrame(row.row_show_comment)
            row.wrapper_comment.pack(fill='both', expand=True)

            for comment in get_all_comment_of_task:    
                self.init_ui_row_comment(comment, row)
               
        except Exception as e:
            print(f'Error: {e}')
            pass
    
    def on_delete_comment(self, comment, row_comment):
        try:
            self.comment_dao.delete(comment)
            row_comment.destroy()
            # print(comment.content)
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
                current_row.entry_comment.delete('1.0', 'end-1c')
                # print('Add comment success')


                # Add comment to row
                self.init_ui_row_comment(comment, current_row)
                # print('Add comment success')
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
                        # print('Edit task success')
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
                            # print('Edit task success')
                            self.implement_show_all_task()
                            return
        except Exception as e:
            print(f'Error: {e}')
            pass

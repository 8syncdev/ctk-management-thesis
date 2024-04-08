from app.db.main import *
from customtkinter import *



class AccountUtil:

    base_ui = None
    # GroupDAO
    group_dao = GroupDAO()
    max_member = 6
    #

    @staticmethod
    def on_send_btn_register_thesis(name_thesis: str, tech_cate, description: str, lecturer):
        try:
            print('------------------------------ Register thesis ------------------------------')
            print(f'Name: {name_thesis}')
            print(tech_cate)
            print(f'Description: {description}')
            print(f'Lecturer: {lecturer}')
            print('------------------------------ Register thesis ------------------------------')
        except Exception as e:
            print(f'Error: {e}')

    @staticmethod
    def on_join_group(group: Group, account: Account, label: CTkLabel, btn_cancel_state: CTkButton):
        try:
            if group.account_list.__len__() < AccountUtil.max_member and account.group_list == []:
                group.account_list.append(account)
                AccountUtil.group_dao.update(group)
                print(f'Join group: {group.name}')
                label.configure(text=f'Member: {group.account_list.__len__()} / {AccountUtil.max_member}')
                # btn_cancel_state.configure(state='normal')
            else:
                print('Group is full')
        except Exception as e:
            print(f'Error: {e}')

    @staticmethod
    def on_out_group(group: Group, account: Account, label: CTkLabel, btn_cancel_state: CTkButton):
        try:
            if account in group.account_list and account.group_list != []:
                group.account_list.remove(account)
                AccountUtil.group_dao.update(group)
                print(f'Out group: {group.name}')
                label.configure(text=f'Member: {group.account_list.__len__()} / {AccountUtil.max_member}')
                # btn_cancel_state.configure(state='disabled')
            else:
                print('Account not in group')
        except Exception as e:
            print(f'Error: {e}')

    @staticmethod
    def get_joined_group(account: Account):
        try:
            return account.group_list[0]
        except Exception as e:
            print(f'Error: {e}')
            return None

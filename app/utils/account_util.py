from app.db.main import *
from customtkinter import *
import random as r


class AccountUtil:

    base_ui = None
    group_dao = GroupDAO()
    thesis_dao = ThesisDAO()
    account_dao = AccountDAO()
    task_dao = TaskDAO()
    grade_by_council_dao = GradeByCouncilDAO()
    grade_dao = GradeDAO()
    tech_cate_dao = TechnologyCategoryDAO()
    technology_requirement_list_dao = TechnologyRequirementDAO()
    max_member = 6
    criteria_list_dao = CriterionDAO()
    #

    @staticmethod
    def on_send_btn_register_thesis(name_thesis: str, tech_cate, description: str, lecturer: str):
        try:
            print('------------------------------ Register thesis ------------------------------')
            print(f'Name: {name_thesis}')
            print(tech_cate)
            print(f'Description: {description}')
            print(f'Lecturer: {lecturer}')
            print('------------------------------ Register thesis ------------------------------')
            list_tech_cate = []
            for tech_name in tech_cate:
                for tech in AccountUtil.tech_cate_dao.get_all():
                    if tech_name == tech.name:
                        list_tech_cate.append(tech)

            for thesis in AccountUtil.thesis_dao.get_all():
                if thesis.name == name_thesis:
                    print('Thesis already exists')
                    AccountUtil.base_ui.slide_show_form.animate()
                    return
            thesis = Thesis(name=name_thesis, account=AccountUtil.account_dao.get(int(lecturer.split('-')[0])), technology_category_list=list_tech_cate, technology_requirement_list=r.choices(AccountUtil.technology_requirement_list_dao.get_all(), k=AccountUtil.technology_requirement_list_dao.get_all().__len__() % 4), criteria_list=r.choices(AccountUtil.criteria_list_dao.get_all(), k=AccountUtil.criteria_list_dao.get_all().__len__() % 4))
            AccountUtil.thesis_dao.create(thesis)
            print('Register thesis successfully')
            AccountUtil.base_ui.slide_show_form.animate()

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
    def get_joined_group(account: Account) -> Group:
        try:
            get_group = account.group_list[0]
            return get_group if get_group != None else None
        except Exception as e:
            print(f'Error: {e}')
            return None
        
    @staticmethod
    def get_all_group_of_thesis(account: Account, _thesis: Thesis=None):
        try:
            get_all_thesis = AccountUtil.thesis_dao.get_all()
            for thesis in get_all_thesis:
                if _thesis != None and account.email == thesis.account.email and _thesis == thesis:
                    return thesis.group_list
            for thesis in get_all_thesis:
                if account.email == thesis.account.email:
                    return thesis.group_list
            return []
        except Exception as e:
            print(f'Error: {e}')
            return None
    
    @staticmethod
    def get_all_thesis_of_account(account: Account):
        try:
            list_thesis = []
            get_all_thesis = AccountUtil.thesis_dao.get_all()
            for thesis in get_all_thesis:
                if account.email == thesis.account.email:
                    list_thesis.append(thesis)
            return list_thesis
                
        except Exception as e:
            print(f'Error: {e}')
            return None

    @staticmethod
    def get_thesis_of_account(account: Account):
        try:
            get_all_thesis = AccountUtil.thesis_dao.get_all()
            for thesis in get_all_thesis:
                if account.email == thesis.account.email:
                    return thesis
                
        except Exception as e:
            print(f'Error: {e}')
            return None
        
    @staticmethod
    def get_total_progress_of_account(account: Account):
        try:
            return sum([task.progress for task in account.task_list]) / account.task_list.__len__() if account.task_list.__len__() != 0 else 0
                
        except Exception as e:
            print(f'Error: {e}')
            return 
        
    @staticmethod
    def get_thesis_of_selected_group(group: Group):
        base_not_found = {
            'name': 'No thesis',
        }
        try:
            for thesis in AccountUtil.thesis_dao.get_all():
                if group in thesis.group_list:
                    return thesis
            return base_not_found
        except Exception as e:
            print(f'Error: {e}')
            return base_not_found
        
    @staticmethod
    def get_grade_of_account(account: Account):
        try:
            list_grade = []
            get_all_grade = AccountUtil.grade_dao.get_all()
            for grade in get_all_grade:
                if account.email == grade.account.email:
                    list_grade.append(grade)
            return "No grade" if list_grade.__len__() == 0 else sum([grade.score for grade in list_grade]) / list_grade.__len__()
                
        except Exception as e:
            print(f'Error: {e}')
            return
        
    @staticmethod
    def on_create_group(name: str, thesis: Thesis, account: Account):
        try:
            print('------------------------------ Create group ------------------------------')
            print(f'Name: {name}')
            print(f'Thesis: {thesis.name}')
            print(f'Account: {account.email}')
            print('------------------------------ Create group ------------------------------')
            for group in AccountUtil.group_dao.get_all():
                if group.name == name:
                    print('Group already exists')
                    AccountUtil.base_ui.slide_show_detail.animate()
                    return
            group = Group(name=name)
            AccountUtil.group_dao.create(group)
            thesis.group_list.append(group)
            thesis.account = account
            AccountUtil.thesis_dao.update(thesis)
            print('Create group successfully')
            AccountUtil.base_ui.slide_show_detail.animate()
        except Exception as e:
            print(f'Error: {e}')
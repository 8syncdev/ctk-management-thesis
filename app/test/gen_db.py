from app.db.main import *
from app.setting.setting import *
import random
import sqlalchemy

class DBGenerator:
    def __init__(self):
        self.account_dao = AccountDAO()
        self.group_dao = GroupDAO()
        self.task_dao = TaskDAO()
        self.thesis_dao = ThesisDAO()
        self.tech_cate_dao = TechnologyCategoryDAO()
        self.tech_require_dao = TechnologyRequirementDAO()
        self.criterion_dao = CriterionDAO()


    def generate_thesis_tech_cate(self):
        for thesis in self.thesis_dao.get_all():
            _length = self.tech_cate_dao.count()
            min_length = random.randint(0, _length % (_length // 2))
            max_length = random.randint(min_length, _length)
            if min_length > max_length:
                min_length, max_length = max_length, min_length  
            if max_length - min_length > 10:
                max_length = min_length + 10              
            for tech_cate in self.tech_cate_dao.get_all()[min_length:max_length]:
                if tech_cate not in thesis.technology_category_list:
                    thesis.technology_category_list.append(tech_cate)
            self.thesis_dao.update(thesis)

    def generate_thesis_criteria(self):
        for thesis in self.thesis_dao.get_all():
            _length = self.criterion_dao.count()
            min_length = random.randint(0, _length % (_length // 2))
            max_length = random.randint(min_length, _length)
            if min_length > max_length:
                min_length, max_length = max_length, min_length
            if max_length - min_length > 10:
                max_length = min_length + 10
            for criterion in self.criterion_dao.get_all()[min_length:max_length]:
                if criterion not in thesis.criteria_list:
                    thesis.criteria_list.append(criterion)
            self.thesis_dao.update(thesis)

    def generate_thesis_tech_require(self):
        for thesis in self.thesis_dao.get_all():
            _length = self.tech_require_dao.count()
            min_length = random.randint(0, _length % (_length // 2))
            max_length = random.randint(min_length, _length)
            if min_length > max_length:
                min_length, max_length = max_length, min_length
            if max_length - min_length > 10:
                max_length = min_length + 10
            for tech_require in self.tech_require_dao.get_all()[min_length:max_length]:
                if tech_require not in thesis.technology_requirement_list:
                    thesis.technology_requirement_list.append(tech_require)
            self.thesis_dao.update(thesis)


    def generate_group_thesis(self):
        i = 0
        for thesis in self.thesis_dao.get_all():
            for group in self.group_dao.get_all()[i:i+6]:
                thesis.group_list.append(group)
            self.thesis_dao.update(thesis)
            i += 6

    def generate_task(self):
        ...


    def main(self):
        self.generate_thesis_tech_cate()
        self.generate_thesis_criteria()
        self.generate_thesis_tech_require()
        self.generate_group_thesis()
        self.generate_task()
        



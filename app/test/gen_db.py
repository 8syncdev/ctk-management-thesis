from app.db.main import *
import random

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
            _len_tech_cate = random.randint(0, self.tech_cate_dao.count())
            for tech_cate in self.tech_cate_dao.get_all()[:_len_tech_cate]:
                thesis.technology_category_list.append(tech_cate)
            self.thesis_dao.update(thesis)

    def generate_thesis_criteria(self):
        for thesis in self.thesis_dao.get_all():
            _len_criteria = random.randint(0, self.criterion_dao.count())
            for criterion in self.criterion_dao.get_all()[:_len_criteria]:
                thesis.criteria_list.append(criterion)
            self.thesis_dao.update(thesis)

        
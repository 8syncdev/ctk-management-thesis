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
            if _len_tech_cate == 0:
                _len_tech_cate = 2
            for tech_cate in self.tech_cate_dao.get_all()[:_len_tech_cate]:
                thesis.technology_category_list.append(tech_cate)
            self.thesis_dao.update(thesis)

    def generate_thesis_criteria(self):
        for thesis in self.thesis_dao.get_all():
            _len_criteria = random.randint(0, self.criterion_dao.count())
            if _len_criteria == 0:
                _len_criteria = 2
            for criterion in self.criterion_dao.get_all()[:_len_criteria]:
                thesis.criteria_list.append(criterion)
            self.thesis_dao.update(thesis)

    def generate_thesis_tech_require(self):
        for thesis in self.thesis_dao.get_all():
            _len_tech_require = random.randint(0, self.tech_require_dao.count())
            if _len_tech_require == 0:
                _len_tech_require = 2
            for tech_require in self.tech_require_dao.get_all()[:_len_tech_require]:
                thesis.technology_requirement_list.append(tech_require)
            self.thesis_dao.update(thesis)

        
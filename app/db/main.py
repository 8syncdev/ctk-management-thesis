from app.db.init_db import connect_to_db
# ---------------- DAO ----------------
from app.db.dao.account_dao import AccountDAO
from app.db.dao.group_dao import GroupDAO
from app.db.dao.task_dao import TaskDAO
from app.db.dao.thesis_dao import ThesisDAO
from app.db.dao.technology_cate_dao import TechnologyCategoryDAO
from app.db.dao.technology_require_dao import TechnologyRequirementDAO
from app.db.dao.thesis_requirement_dao import ThesisRequirementDAO




# ---------------- InterfaceDAO ----------------
from app.db.interface_dao import InterfaceDAO, _T, Generic

#----------------- Models ----------------
from app.db.init_db import Account, Group, Task, Thesis, TechnologyCategory, TechnologyRequirement, ThesisRequirement
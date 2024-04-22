from app.ui.auth_ui import AuthUI
from app.ui.main_ui import MainUI
from app.ui.base.base_ui import BaseUI
from app.db.main import AccountDAO



def main():
    main_ui = MainUI(account=AccountDAO().get(1))
    # auth_ui = AuthUI()
    main_ui.run_ui()
    # auth_ui.run_ui()
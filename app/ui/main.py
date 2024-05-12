from app.ui.auth_ui import AuthUI
from app.ui.main_ui import MainUI
from app.ui.base.base_ui import BaseUI
from app.db.main import AccountDAO



def main(selected_account_id: int = 2):
    main_ui = MainUI(account=AccountDAO().get(selected_account_id))
    main_ui.run_ui()
    # auth_ui = AuthUI()
    # auth_ui.run_ui()
from app.ui.main import main
import customtkinter as ctk
from app.db.init_db import connect_to_db

if __name__ == "__main__":
    connect_to_db()
    ctk.set_appearance_mode("light")
    main(selected_account_id=14)
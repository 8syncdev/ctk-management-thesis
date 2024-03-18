from app.ui.main import main
import customtkinter as ctk
from app.db.init_db import connect_to_db

if __name__ == "__main__":
    connect_to_db()
    main()
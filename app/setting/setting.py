import os
from typing import List, Dict, Union, Any, Literal
from app.anotation.main import *
from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkFont,
    CTkImage,
    CTkLabel,
    CTkOptionMenu,
    CTkScrollableFrame,
    CTkToplevel,
    CTkFrame,
    CTkScrollbar,
    CTkTabview,
    CTkSegmentedButton,
    CTkSwitch,
    CTkTextbox,
    CTkCheckBox,
    CTkProgressBar,
    CTkComboBox,
    CTkSlider,
    filedialog,
    set_appearance_mode,
    set_default_color_theme,
)


from PIL.Image import (
    open      as pillow_image_open,
    fromarray as pillow_image_fromarray
)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# --------------- Icon ---------------
icon_path = BASE_DIR / 'asset' / 'icons' / 'feather'

LIST_ICONS_MATERIAL_DESIGN = {}

for file in os.listdir(icon_path):
    if file.endswith('.png'):
        # LIST_ICONS_MATERIAL_DESIGN.append(CTkImage(pillow_image_open(icon_path / file)))
        LIST_ICONS_MATERIAL_DESIGN[file.split('.')[0]] = pillow_image_open(icon_path / file)



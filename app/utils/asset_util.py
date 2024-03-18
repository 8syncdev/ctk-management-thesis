from app.setting.setting import *

class AssetUtil:
    @staticmethod
    def get_icon(name: KEY_ICONS_TYPE) -> CTkImage:
        return LIST_ICONS_MATERIAL_DESIGN[name]
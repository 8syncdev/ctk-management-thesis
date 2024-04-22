from app.setting.setting import *

class AssetUtil:
    @staticmethod
    def get_icon(name: KEY_ICONS_TYPE, resize=(30,30)) -> CTkImage:
        return CTkImage(LIST_ICONS_MATERIAL_DESIGN[name].resize(resize))
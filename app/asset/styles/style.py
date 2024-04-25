from typing import *
# Full color tailwind css
COLOR_STYLE = {
    'primary': '#2563EB',
    'primary_hover': '#1D4ED8',
    'primary_active': '#1E40AF',
    'secondary': '#10B981',
    'secondary_hover': '#059669',
    'secondary_active': '#047857',
    'danger': '#DC2626',
    'danger_hover': '#B91C1C',
    'danger_active': '#991B1B',
    'warning': '#F59E0B',
    'warning_hover': '#D97706',
    'warning_active': '#A45308',
    'success': '#34D399',
    'success_hover': '#10B981',
    'success_active': '#059669',
    'info': '#3B82F6',
    'info_hover': '#2563EB',
    'info_active': '#1D4ED8',
    'dark': '#111827',
    'dark_hover': '#1F2937',
    'dark_active': '#374151',
    'light': '#F9FAFB',
    'light_hover': '#F3F4F6',
    'light_active': '#E5E7EB',
    'gray': '#6B7280',
    'gray_hover': '#4B5563',
    'gray_active': '#374151',
    'black': '#000000',
    'white': '#FFFFFF',
    'transparent': 'transparent',
}


FONT_STYLE = {
    'font': ('Arial', 13),
    'font_bold': ('Arial', 13, 'bold'),
    'font_italic': ('Arial', 13, 'italic'),
    'font_bold_italic': ('Arial', 13, 'bold', 'italic'),
    'font_sm_bold': ('Arial', 8, 'bold'),
    'font_sm_italic': ('Arial', 8, 'italic'),
    'font_sm_bold_italic': ('Arial', 8, 'bold', 'italic'),
    'font_lg_bold': ('Arial', 16, 'bold'),
    'font_lg_italic': ('Arial', 16, 'italic'),
    'font_lg_bold_italic': ('Arial', 16, 'bold', 'italic'),
    'font_size': 13,
    'font_size_large': 16,
    'font_size_small': 8,
}

KEY_FONT_STYLE = Literal['font', 'font_bold', 'font_italic', 'font_bold_italic', 'font_sm_bold', 'font_sm_italic', 'font_sm_bold_italic', 'font_lg_bold', 'font_lg_italic', 'font_lg_bold_italic', 'font_size', 'font_size_large', 'font_size_small']

KEY_COLOR_STYLE = Literal['primary', 'primary_hover', 'primary_active', 'secondary', 'secondary_hover', 'secondary_active', 'danger', 'danger_hover', 'danger_active', 'warning', 'warning_hover', 'warning_active', 'success', 'success_hover', 'success_active', 'info', 'info_hover', 'info_active', 'dark', 'dark_hover', 'dark_active', 'light', 'light_hover', 'light_active', 'gray', 'gray_hover', 'gray_active', 'black', 'white', 'transparent']


def get_style(name_style: Union[KEY_FONT_STYLE, KEY_COLOR_STYLE]) -> str:
    return FONT_STYLE[name_style] if name_style in list(FONT_STYLE.keys()) else COLOR_STYLE[name_style]
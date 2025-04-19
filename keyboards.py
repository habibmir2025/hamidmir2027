from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📦 مشاهده جیمیل‌ها", callback_data="view_gmails")]
    ])

def generate_buy_button(email):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 پرداخت تستی", callback_data=f"buy_{email}")]
    ])
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📦 مشاهده جیمیل‌ها", callback_data="view_gmails"))
    return keyboard

def generate_buy_button(email):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("💳 پرداخت تستی", callback_data=f"buy_{email}"))
    return keyboard
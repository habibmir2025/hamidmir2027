from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from database import get_available_gmails, remove_gmail
from keyboards import main_menu, generate_buy_button

router = Router()

def register_handlers(dp):
    dp.include_router(router)

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("سلام 👋\nبه ربات فروش جیمیل *hamidmir2027* خوش اومدی!\n\nبرای دیدن جیمیل‌های موجود دکمه زیر رو بزن:", 
                         reply_markup=main_menu(), parse_mode="Markdown")

@router.callback_query(F.data == "view_gmails")
async def view_gmails_handler(callback: CallbackQuery):
    gmails = get_available_gmails()
    if not gmails:
        await callback.message.edit_text("❌ هیچ جیمیلی موجود نیست.")
        return
    
    text = "📋 لیست جیمیل‌های موجود:\n\n"
    for g in gmails:
        text += f"📧 {g['email']}\n💰 قیمت: {g['price']} تومان\n\n"
        await callback.message.answer(text, reply_markup=generate_buy_button(g["email"]))
        text = ""

@router.callback_query(F.data.startswith("buy_"))
async def fake_buy_handler(callback: CallbackQuery):
    email = callback.data[4:]
    gmails = get_available_gmails()
    gmail = next((g for g in gmails if g["email"] == email), None)

    if not gmail:
        await callback.message.answer("❌ این جیمیل دیگر موجود نیست.")
        return
    
    remove_gmail(email)
    await callback.message.answer(
        f"✅ پرداخت موفق!\n\n📧 *{gmail['email']}*\n🔑 *{gmail['password']}*",
        parse_mode="Markdown"
    )
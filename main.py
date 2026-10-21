import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ⚠️ ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ BOTFATHER В КАВЫЧКАХ:
BOT_TOKEN = "8480835882:AAGtP6aE0Die8mitp_8S6j3p6VydQay4HpE"

# Версия проекта
BOT_VERSION = "v0.1.0 Beta"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Главное меню (кнопки под окном ввода)
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 ПРОФИЛЬ"), KeyboardButton(text="📋 ЗАДАНИЯ")],
        [KeyboardButton(text="💰 БАЛАНС"), KeyboardButton(text="🛒 МАГАЗИН")],
        [KeyboardButton(text="❓ ПОМОЩЬ"), KeyboardButton(text="ℹ️ ВЕРСИЯ")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"🎯 **Добро пожаловать в TaskEarned!**\n\n"
        f"Выполняй простые задания, получай монеты и обменивай их на подарочные карты и игровую валюту!\n\n"
        f"Используй меню ниже для навигации.",
        reply_markup=main_keyboard,
        parse_mode="Markdown"
    )

@dp.message(F.text == "👤 ПРОФИЛЬ")
@dp.message(Command("profile"))
async def cmd_profile(message: types.Message):
    user = message.from_user
    username = f"@{user.username}" if user.username else user.first_name
    
    profile_text = (
        f"👤 **Профиль**\n"
        f"🆔 **ID:** `{user.id}`\n"
        f"👤 **Ник:** {username}\n"
        f"📊 **Всего выполнено заданий:** 0\n"
        f"💰 **Текущий баланс:** 0 монет"
    )
    await message.answer(profile_text, parse_mode="Markdown")

@dp.message(F.text == "📋 ЗАДАНИЯ")
@dp.message(Command("tasks"))
async def cmd_tasks(message: types.Message):
    await message.answer("📋 **Доступные задания:**\n\nСейчас идёт подготовка бета-теста! Скоро здесь появятся первые каналы для подписки.")

@dp.message(F.text == "💰 БАЛАНС")
@dp.message(Command("balance"))
async def cmd_balance(message: types.Message):
    await message.answer("💰 **Твой баланс:** 0 монет.\n\nЗарабатывай монеты, выполняя задания в разделе 📋 **ЗАДАНИЯ**!")

@dp.message(F.text == "🛒 МАГАЗИН")
@dp.message(Command("store"))
async def cmd_store(message: types.Message):
    await message.answer("🛒 **Магазин наград:**\n\n• Подарочные карты Google Play\n• Игровая валюта (Robux, Stars и др.)\n\nВывод станет доступен при наборе минимального баланса.")

@dp.message(F.text == "❓ ПОМОЩЬ")
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("❓ **Помощь и Поддержка:**\n\nПо всем вопросам пиши администратору: @Colanov")

@dp.message(F.text == "ℹ️ ВЕРСИЯ")
async def cmd_version(message: types.Message):
    await message.answer(
        f"ℹ️ **Информация о системе:**\n\n"
        f"📌 **Версия:** `{BOT_VERSION}`\n"
        f"🧪 **Статус:** Закрытое Бета-Тестирование\n"
        f"🛠 **Разработчик:** @Colanov\n\n"
        f"Следите за обновлениями в официальном канале!",
        parse_mode="Markdown"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  

import logging
import os
import asyncio
import sys
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, types
from aiogram import F
from os import getenv

from aiogram.filters import CommandStart
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from dotenv import load_dotenv

load_dotenv()
# Bot tokenini atrof-muhit o'zgaruvchisidan oling yoki to'liq yozing
TOKEN =getenv("Bot_token")

# Bot va Dispatcher ni yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Boshlang'ich ReplyKeyboardMarkup
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [  KeyboardButton(text="✈️ Telegram"),
           KeyboardButton(text="☎️Admin bilan aloqa")],
        [     KeyboardButton(text="📸 Instagram"),
              KeyboardButton(text="▶️ YouTube")],
        [KeyboardButton(text="🆓 Bepul darslik")],
    ],
    resize_keyboard=True
)

# /start komandasi handler
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        text="Quyidagi tugmalardan birini tanlang:",
        reply_markup=start_kb
    )


@dp.message(F.photo)
async def get_file_id(message: types.Message):
    file_id = message.photo[-1].file_id  # Eng yuqori sifatdagi rasm
    print("file_id:", file_id)
    await message.answer(f"✅ Rasm file_id: `{file_id}`")


# "Telegram" tugmasi bosilganda inline tugma chiqarish
@dp.message(lambda msg: msg.text == "✈️ Telegram")
async def on_telegram(message: types.Message):
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="@shunchakitrading", url="https://t.me/shunchakiTrading")]
        ]
    )
    await message.answer(
        text="Bizning Telegram kanalimiz:",
        reply_markup=inline_kb
    )

# "Admin bilan aloqa" tugmasi bosilganda Livegram link
@dp.message(lambda msg: msg.text == "☎️Admin bilan aloqa")
async def on_admin_contact(message: types.Message):
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Admin bilan bog'lanish",
                url="https://t.me/shokhzod_sadullayev"
            )]
        ]
    )
    await message.answer(
        text="Admin bilan aloqa uchun quyidagi tugmani bosing:",
        reply_markup=inline_kb
    )



# "Instagram" tugmasi bosilganda
@dp.message(lambda msg: msg.text == "📸 Instagram")
async def on_instagram(message: types.Message):
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/shakhzodsadullayev?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")]
        ]
    )
    await message.answer(
        text="Instagram sahifamiz:",
        reply_markup=inline_kb
    )

# "YouTube" tugmasi bosilganda
@dp.message(lambda msg: msg.text == "▶️ YouTube")
async def on_youtube(message: types.Message):
    file_id = "AgACAgIAAxkBAAOuaBRyFz2TEVOv1iJHCTDFc8Dmsy0AAhz5MRu4mqBIRbYIFtbG9KUBAAMCAAN4AAM2BA"  # Rasm nomini tekshiring


    await message.answer_photo(
        photo=file_id,
        caption="Youtube sahifamiz ishlovda...\n\n Tez orada ishga tushiriladi ✅"
    )

# "Bepul darslik" tugmasi bosilganda
@dp.message(lambda msg: msg.text == "🆓 Bepul darslik")
async def on_free_course(message: types.Message):
    file_id = "AgACAgIAAxkBAAOuaBRyFz2TEVOv1iJHCTDFc8Dmsy0AAhz5MRu4mqBIRbYIFtbG9KUBAAMCAAN4AAM2BA"  # Rasm nomini tekshiring

    await message.answer_photo(
        photo=file_id,
        caption="Bepul darsligimiz  ishlovda...\n\n Tez orada ishga tushiriladi ✅"
    )

# Botni ishga tushirish funksiyasi
def main():
    dp.run_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8969050666:AAG8tqFNRvnYc5_LEU8ZNPaxccCEfZ6KPVQ")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """🎓 NFT kolleksiyasini yaratishni o‘rganing!

0 dan boshlab o‘z NFT kolleksiyangizni yaratish, dizayn qilish, marketplace'ga joylashtirish va sotishni o‘rganing.

📚 Online va offline darslar mavjud."""

    keyboard = [
        [
            InlineKeyboardButton(
                "📚 KURS HAQIDA MA’LUMOT OLISH",
                url="https://islomabdugafforov.tilda.ws/"
            )
        ]
    ]

    await update.message.reply_photo(
        photo=open("nft_academy.png", "rb"),
        caption=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("🤖 Bot ishga tushdi...")

app.run_polling()
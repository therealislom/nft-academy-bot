import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


# =========================================================
# SOZLAMALAR
# =========================================================

# Tokenni GitHub'ga yozmang.
# Render -> Environment Variables -> BOT_TOKEN orqali beriladi.
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Tilda saytingiz
WEBSITE_URL = "https://islomabdugafforov.tilda.ws/"


# =========================================================
# /START
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🚀 <b>TON BLOCKCHAIN'DA NFT YARATISHNI O'RGANING!</b>

NFT yaratishni bilmayapsizmi? Muammo emas.

TON blockchain'da o'z NFT kolleksiyangizni <b>0 dan boshlab yaratish, ishga tushirish va rivojlantirishni</b> amaliy tarzda o'rganing.

🎓 Online + Offline ta'lim
💎 Amaliy mashg'ulotlar
🌐 TON Blockchain
👨‍💻 3 yillik Web3 tajribasi

Kurs dasturi, narxi, mentor haqida va kursga yozilish bo'yicha barcha ma'lumotlarni saytdan ko'rishingiz mumkin.

👇 Batafsil ma'lumot olish uchun:
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🌐 SAYTGA O'TISH",
                url=WEBSITE_URL
            )
        ]
    ])

    try:

        with open("nft_academy.png", "rb") as photo:

            await update.message.reply_photo(
                photo=photo,
                caption=text,
                parse_mode="HTML",
                reply_markup=keyboard
            )

    except FileNotFoundError:

        await update.message.reply_text(
            text,
            parse_mode="HTML",
            reply_markup=keyboard
        )


# =========================================================
# RENDER HEALTH CHECK
# =========================================================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/plain"
        )

        self.end_headers()

        self.wfile.write(
            b"NFT Academy Bot is running!"
        )

    def log_message(self, format, *args):
        return


def start_server():

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    server = HTTPServer(
        ("0.0.0.0", port),
        HealthHandler
    )

    server.serve_forever()


# =========================================================
# BOTNI ISHGA TUSHIRISH
# =========================================================

if not BOT_TOKEN:

    raise ValueError(
        "BOT_TOKEN topilmadi! "
        "Render Environment Variables ichida "
        "BOT_TOKEN yarating."
    )


# Render uchun HTTP server
threading.Thread(
    target=start_server,
    daemon=True
).start()


# Telegram bot
app = Application.builder().token(
    BOT_TOKEN
).build()


# /start komandasi
app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


# =========================================================
# START
# =========================================================

print("🤖 NFT Academy Bot ishga tushdi!")

app.run_polling()

import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


# =========================================================
# SOZLAMALAR
# =========================================================

# MUHIM:
# Bot tokenini bu yerga yozmang.
# Render -> Environment Variables -> BOT_TOKEN orqali beriladi.
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Tilda saytingiz
WEBSITE_URL = "https://islomabdugafforov.tilda.ws/"


# =========================================================
# ASOSIY MENYU
# =========================================================

def main_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📚 Kurs dasturi",
                callback_data="program"
            ),
            InlineKeyboardButton(
                "💰 Kurs narxi",
                callback_data="price"
            )
        ],
        [
            InlineKeyboardButton(
                "👨‍💻 Mentor haqida",
                callback_data="mentor"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Saytni ko'rish",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "✍️ Kursga yozilish",
                callback_data="register"
            )
        ]
    ])


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

Kurs haqida batafsil ma'lumot olish uchun quyidagi bo'limlardan birini tanlang 👇
"""

    try:
        with open("nft_academy.png", "rb") as photo:

            await update.message.reply_photo(
                photo=photo,
                caption=text,
                parse_mode="HTML",
                reply_markup=main_keyboard()
            )

    except FileNotFoundError:

        await update.message.reply_text(
            text,
            parse_mode="HTML",
            reply_markup=main_keyboard()
        )


# =========================================================
# KURS DASTURI
# =========================================================

async def program(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    text = """
📚 <b>KURS DASTURI</b>

Kurs davomida quyidagilarni o'rganasiz:

🔹 TON blockchain asoslari
🔹 NFT nima va qanday ishlaydi
🔹 NFT kolleksiya g'oyasini yaratish
🔹 NFT dizayn va metadata
🔹 TON'da NFT kolleksiya yaratish
🔹 NFT marketplace bilan ishlash
🔹 Kolleksiyani ishga tushirish
🔹 NFT marketing asoslari
🔹 Kolleksiyani rivojlantirish
🔹 Web3 loyiha yaratish asoslari

🎯 <b>Maqsad:</b>

Kurs oxiriga kelib TON blockchain'da o'z NFT kolleksiyangizni yaratish bo'yicha amaliy bilimga ega bo'lish.
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💰 Kurs narxi",
                callback_data="price"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Batafsil ma'lumot",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Orqaga",
                callback_data="back"
            )
        ]
    ])

    await query.edit_message_text(
        text,
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================================================
# KURS NARXI
# =========================================================

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    text = """
💰 <b>KURS NARXI</b>

💻 <b>ONLINE — $100</b>

🌐 Masofadan turib o'qish
📚 Kurs materiallari
💎 Amaliy mashg'ulotlar
🌐 TON Blockchain
🎨 NFT kolleksiya yaratish


🏫 <b>OFFLINE — $300</b>

👨‍💻 Shaxsan mentor bilan
📚 Amaliy mashg'ulotlar
💎 NFT kolleksiya yaratish
🌐 TON Blockchain
🚀 Loyihani ishga tushirish


👇 Kurs haqida batafsil ma'lumot:
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💻 ONLINE — $100",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "🏫 OFFLINE — $300",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Saytni ko'rish",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Orqaga",
                callback_data="back"
            )
        ]
    ])

    await query.edit_message_text(
        text,
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================================================
# MENTOR
# =========================================================

async def mentor(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    text = """
👨‍💻 <b>MENTOR HAQIDA</b>

<b>Islom Abdugafforov</b>

🌐 TON Blockchain / Web3 Expert

⏳ 3 yillik Web3 tajribasi

💎 TON ekotizimi
🎨 NFT
🚀 Web3 loyihalar
📈 NFT kolleksiyalarini rivojlantirish

Kurs davomida nazariy bilim bilan birga amaliy ko'nikmalarga ham e'tibor beriladi.
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🌐 Saytni ko'rish",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Orqaga",
                callback_data="back"
            )
        ]
    ])

    await query.edit_message_text(
        text,
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================================================
# KURSGA YOZILISH
# =========================================================

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    text = """
✍️ <b>KURSGA YOZILISH</b>

Sizga mos ta'lim formatini tanlang:

💻 Online — <b>$100</b>
🏫 Offline — <b>$300</b>

Kurs dasturi, darslar va boshqa ma'lumotlar bilan saytimizda tanishishingiz mumkin.

👇 Batafsil ma'lumot olish uchun:
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💻 ONLINE — $100",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "🏫 OFFLINE — $300",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 SAYTGA O'TISH",
                url=WEBSITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Orqaga",
                callback_data="back"
            )
        ]
    ])

    await query.edit_message_text(
        text,
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================================================
# ORQAGA
# =========================================================

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    text = """
🚀 <b>TON BLOCKCHAIN'DA NFT YARATISHNI O'RGANING!</b>

NFT yaratishni bilmayapsizmi? Muammo emas.

TON blockchain'da o'z NFT kolleksiyangizni <b>0 dan boshlab</b> yaratishni amaliy tarzda o'rganing.

🎓 Online + Offline ta'lim
💎 Amaliy mashg'ulotlar
🌐 TON Blockchain
👨‍💻 3 yillik Web3 tajribasi

👇 Quyidagi bo'limlardan birini tanlang:
"""

    await query.edit_message_text(
        text,
        parse_mode="HTML",
        reply_markup=main_keyboard()
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


# =========================================================
# HANDLERS
# =========================================================

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CallbackQueryHandler(
        program,
        pattern="^program$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        price,
        pattern="^price$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        mentor,
        pattern="^mentor$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        register,
        pattern="^register$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        back,
        pattern="^back$"
    )
)


# =========================================================
# START
# =========================================================

print("🤖 NFT Academy Bot ishga tushdi!")

app.run_polling()

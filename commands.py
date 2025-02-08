from telegram import Update
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я шагомер-бот. Отправь мне количество шагов, и я их запомню.")
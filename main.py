from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = "6297007825:AAGaKHiJvLkZUxxeMoVgWFewbXHjwv7E1Bg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Вітаю це мій перший телеграм бот написанний мовою python!")

def run():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("help", start))

    application.run_polling()

if __name__ == "__main__":
    run()
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to SecurePass!\n\n"
        "Use /generate to create a strong password.\n"
        "Use /check to test a password's strength.\n"
        "Use /help for more info."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Main menu\n"
        "/generate - Generate a secure password\n"
        "/check - Check password strength\n"
        "/help - Show this message"
    )

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set!")
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to SecurePass! Use /generate to create a password or /check to test one."
    )

app = ApplicationBuilder().token("YOUR_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

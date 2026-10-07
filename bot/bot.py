import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

def is_admin(update: Update):
    return str(update.effective_chat.id) == str(ADMIN_CHAT_ID)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ WiFiSentinel License Bot\n\n"
        "Bot is online.\n"
        "Use /help to see available commands."
    )

async def admin_only(update: Update):
    if not is_admin(update):
        await update.message.reply_text("⛔ Admin access required.")
        return False
    return True

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "WiFiSentinel Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show help\n"
        "/status - Check bot status"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 WiFiSentinel Bot is online."
    )

def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN is not configured.")
        return

    print("WiFiSentinel Telegram license bot")
    print("Developer:", os.getenv("DEVELOPER", "Arman YB"))
    print("Bot is starting...")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))

    app.run_polling()

if __name__ == "__main__":
    main()

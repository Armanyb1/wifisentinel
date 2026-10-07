import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from app.license import set_license

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

PRICE_PLANS = {
    "7day": {"days": 7, "price": 100, "label": "7 Days"},
    "1month": {"days": 30, "price": 330, "label": "1 Month"},
    "lifetime": {"days": None, "price": 600, "label": "Lifetime"},
}


def is_admin(update: Update):
    return str(update.effective_chat.id) == str(ADMIN_CHAT_ID)


async def admin_only(update: Update):
    if not is_admin(update):
        await update.message.reply_text("⛔ Admin access required.")
        return False
    return True


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ WiFiSentinel License Bot\n\n"
        "Bot is online.\n"
        "Use /help to see available commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ WiFiSentinel Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show help\n"
        "/status - Check bot status\n"
        "/pricing - Show license prices\n"
        "/activate DEVICE_ID PLAN - Activate a license"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 WiFiSentinel Bot is online.")


async def pricing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 WiFiSentinel License Pricing\n\n"
        "7 Days  — ৳100\n"
        "1 Month — ৳330\n"
        "Lifetime — ৳600\n\n"
        "Plans: 7day / 1month / lifetime"
    )


async def activate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await admin_only(update):
        return

    if len(context.args) != 2:
        await update.message.reply_text(
            "Usage:\n/activate DEVICE_ID PLAN\n\n"
            "Plans:\n"
            "7day = ৳100 / 7 days\n"
            "1month = ৳330 / 30 days\n"
            "lifetime = ৳600 / lifetime"
        )
        return

    device_id = context.args[0].upper()
    plan_key = context.args[1].lower()

    if plan_key not in PRICE_PLANS:
        await update.message.reply_text(
            "⛔ Invalid plan. Use: 7day, 1month, or lifetime."
        )
        return

    plan = PRICE_PLANS[plan_key]

    if plan["days"] is None:
        expires_at = None
        expiry_text = "LIFETIME"
    else:
        expires_at = (
            datetime.now(timezone.utc)
            + timedelta(days=plan["days"])
        ).strftime("%Y-%m-%d %H:%M:%S UTC")
        expiry_text = expires_at

    set_license(device_id, plan_key, expires_at)

    await update.message.reply_text(
        f"✅ License activated.\n\n"
        f"Device: {device_id}\n"
        f"Plan: {plan['label']}\n"
        f"Price: ৳{plan['price']}\n"
        f"Expires: {expiry_text}"
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
    app.add_handler(CommandHandler("pricing", pricing))
    app.add_handler(CommandHandler("activate", activate))

    app.run_polling()


if __name__ == "__main__":
    main()

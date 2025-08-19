from telegram.ext import Updater, CommandHandler

# اینجا توکن رباتت رو بذار
TOKEN = "8301356047:AAHmUtLyxG6dNwfGVL7iXEo9rUf28v7pdQU"

# دستور شروع
def start(update, context):
    update.message.reply_text("سلام! 🌹 من یک ربات ساده تلگرام هستم.")

# دستور راهنما
def help_command(update, context):
    update.message.reply_text("دستورات من:\n/start - شروع\n/help - راهنما")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # اضافه کردن دستورها
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # اجرای ربات
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

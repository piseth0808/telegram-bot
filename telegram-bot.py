from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import yt_dlp
import os

TOKEN = "your-bot-token"

def download_video(url):
    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "video.mp4"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("👋 Hello! Send me a YouTube link to download 📥")

def download(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    update.message.reply_text("🔄 Downloading...")

    try:
        video_path = download_video(url)
        update.message.reply_video(video=open(video_path, 'rb'))
        os.remove(video_path)
    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

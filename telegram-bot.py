from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import yt_dlp
import os

TOKEN = "7799417641:AAHx8Yd6zpJ0Bw2CMXnfsBhzUy-2Om2poEU"

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "video.mp4"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("👋 សួស្តី! ផ្ញើលីង YouTube មកខ្ញុំដើម្បីទាញយកវីដេអូ 📥")

def download(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    update.message.reply_text("🔄 กำลังดาวน์โหลด...")
    
    try:
        video_path = download_video(url)
        update.message.reply_video(video=open(video_path, 'rb'))
        os.remove(video_path)
    except Exception as e:
        update.message.reply_text(f"❌ មានបញ្ហា: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
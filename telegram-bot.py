from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import yt_dlp
import os

TOKEN = "your-telegram-bot-token"

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "video.mp4"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 សួស្តី! ផ្ញើលីង YouTube មកខ្ញុំដើម្បីទាញយកវីដេអូ 📥")

async def download(update: Update, context: CallbackContext):
    url = update.message.text
    await update.message.reply_text("🔄 กำลังดาวน์โหลด...")
    
    try:
        video_path = download_video(url)
        await update.message.reply_video(video=open(video_path, 'rb'))
        os.remove(video_path)
    except Exception as e:
        await update.message.reply_text(f"❌ មានបញ្ហា: {e}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

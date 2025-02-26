from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import datetime
import asyncio
import os
from dotenv import load_dotenv
from flask import Flask

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv("TOKEN")

# Global variable to store chat ID
CHAT_ID = None

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram bot is running!"

# Command handler for /start
async def start_command(update: Update, context):
    global CHAT_ID
    CHAT_ID = update.message.chat_id
    await update.message.reply_text("Hello user! I will remind you to drink water every hour from 8 AM to 11 PM.")

# Function to send water reminders every hour from 8 AM to 11 PM
async def send_water_reminder(context):
    if CHAT_ID is None:
        return  # Do nothing if CHAT_ID is not set
    now = datetime.datetime.now().time()
    if 8 <= now.hour <= 23 and now.minute == 0:
        await context.bot.send_message(chat_id=CHAT_ID, text="Reminder: Drink water! 💧")

# Main function to start the bot
async def main():
    print("Starting up bot...")

    # Create the application
    application = Application.builder().token(TOKEN).build()

    # Check if JobQueue is available
    if not application.job_queue:
        print("Error: JobQueue not available!")
        return

    job_queue = application.job_queue

    # Add command handler
    application.add_handler(CommandHandler("start", start_command))

    # Schedule water reminders
    job_queue.run_repeating(send_water_reminder, interval=60.0, first=0.0)

    # Start the bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    # Keep the bot running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        # Create a new event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Start the Flask server in a separate thread
        from threading import Thread
        flask_thread = Thread(target=lambda: app.run(host="0.0.0.0", port=5000))
        flask_thread.daemon = True
        flask_thread.start()

        # Run the bot
        loop.run_until_complete(main())
    except RuntimeError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    finally:
        # Clean up the event loop
        loop.close()

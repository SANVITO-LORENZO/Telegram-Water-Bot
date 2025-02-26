# Telegram-Water-Bot
This is a Telegram bot that reminds you to drink water. The bot automatically sends a message every hour from 8 AM to 11 PM, encouraging you to stay hydrated. It's built using Python, the python-telegram-bot library for Telegram integration, and Flask to keep the service running.
Key Features
✔ Sends hourly reminders to drink water.
✔ Can be deployed on Render or other hosting platforms.
✔ Uses environment variables to keep the bot token secure.

How to Use This Project
1️⃣ Create a Telegram Bot with BotFather
Before running this project, you need to create a Telegram bot:

Open Telegram and search for @BotFather.
Start a chat and send the command /newbot.
Choose a name for your bot (e.g., WaterReminderBot).
Pick a unique username (e.g., WaterReminderBot123).
BotFather will generate an API token – save it, as you'll need it later.
2️⃣ Download and Set Up the Project
Option 1: Clone the Repository (Recommended)
If the project is on GitHub, clone it:

bash
Copy
Edit
git clone https://github.com/your-username/water-reminder-bot.git
cd water-reminder-bot
Option 2: Download the Files Manually
Create a new folder on your computer.
Add the files main.py, requirements.txt, .env, and render.yaml to the folder.
3️⃣ Install Dependencies
Make sure you have Python 3.10+ installed. Then run:

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up the .env File
Create a .env file in the project directory and add your Telegram bot token:

ini
Copy
Edit
TOKEN=your_botfather_token_here
5️⃣ Run the Bot Locally
To test the bot on your local machine, run:

bash
Copy
Edit
python main.py
If everything is set up correctly, the bot will start running and send you water reminders!

6️⃣ Deploy the Bot on Render
To keep the bot running 24/7, deploy it on Render:

Sign up at Render and create a Web Service.
Connect your GitHub repository or manually upload the files.
Ensure that the render.yaml file is correctly set up with the bot’s name.
Add an environment variable called TOKEN and paste your bot token.
Start the service – your bot will now work automatically!

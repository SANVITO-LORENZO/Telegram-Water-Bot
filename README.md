# Telegram-Water-Bot  

This is a **Telegram bot** that reminds you to drink water. It automatically sends a message **every hour from 8 AM to 11 PM**, encouraging you to stay hydrated.  

The bot is built using **Python**, with:  
- `python-telegram-bot` for Telegram integration  
- `Flask` to keep the service running  
- `dotenv` for managing environment variables  

---

## **Key Features**  
✔ Sends **hourly reminders** to drink water  
✔ Can be deployed on **Render** or other hosting platforms  
✔ Uses **environment variables** to keep the bot token secure  

---

## **1️⃣ Prerequisites**  

Before running this project, make sure you have:  
- **Python 3.10+** installed  
- A **Telegram bot token** (instructions below)  
- Git installed (optional, but recommended for cloning the repository)  

---

## **2️⃣ Create a Telegram Bot with BotFather**  

1. Open Telegram and search for **@BotFather**  
2. Start a chat and send the command: /newbot
3. Choose a **name** for your bot (e.g., `WaterReminderBot`)  
4. Pick a **unique username** (e.g., `WaterReminderBot123`)  
5. **BotFather will generate an API token** – copy and save it.  

---

## **3️⃣ Download and Set Up the Project**  

### **Option 1: Clone the Repository (Recommended)**  
If the project is on GitHub, clone it.  

### **Option 2: Download the Files Manually**
Create a new folder on your computer
Add the following files to the folder:
main.py
requirements.txt
.env
render.yaml

---

## **4️⃣ Install Dependencies**
Navigate to the project folder and install the required dependencies:

pip install -r requirements.txt

---

## **5️⃣ Set Up the .env File**
Create a .env file in the project directory and add your Telegram bot token:

TOKEN=your_botfather_token_here

---

## **6️⃣ Run the Bot Locally**
To test the bot on your local machine, run:

python main.py
If everything is set up correctly, the bot will start running and send you hourly reminders to drink water!

---

## **7️⃣ Deploy the Bot on Render**
To keep the bot running 24/7, deploy it on Render:

1. Sign up at Render and create a Web Service.
2. Connect your GitHub repository or manually upload the files.
3. Ensure that the render.yaml file is correctly set up with the bot’s name.
4. Add an environment variable called TOKEN and paste your bot token.
5. Start the service – your bot will now work automatically!

---

# Project Files Explanation

---

##  📄 main.py (The Bot's Code)
This file contains the main logic of the bot.

It handles messages and commands from users
Sends hourly water reminders from 8 AM to 11 PM
Uses Flask to keep the bot running
Schedules messages using the JobQueue feature of python-telegram-bot

---

## 📄 .env (Environment Variables) 
This file stores sensitive data like your Telegram bot token.

---

##  📄 requirements.txt (Dependencies) 
Contains all necessary Python libraries for running the bot:

---

##  📄 render.yaml (Deployment Configuration) 
This file is used to deploy the bot on Render.

---

# 🎯 Summary

This bot reminds you to drink water every hour from 8 AM to 11 PM.
You can run it locally or deploy it on Render for 24/7 functionality.
It's built with Python, python-telegram-bot, and Flask.

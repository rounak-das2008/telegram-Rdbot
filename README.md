# Telegram-Rdbot
This Telegram bot, developed using the python-telegram-bot library, allows users to access information from various sources such as Wolfram Alpha, Wikipedia, and Google directly within a Telegram chat. With this bot, users can perform calculations, search for information, get summaries, and perform other useful tasks.

* **Features**
Wolfram Alpha Integration: Provides access to the powerful computational knowledge engine of Wolfram Alpha, allowing users to perform complex calculations, get mathematical solutions, and more.
Wikipedia Integration: Retrieves summaries and information from Wikipedia on a wide range of topics, making it easy to obtain knowledge directly in the Telegram chat.
Google Search: Enables users to perform Google searches and receive relevant search results without leaving the Telegram app.
User-friendly Interface: Offers a user-friendly and interactive interface to easily interact with the bot and access various functionalities.
Error Handling: Handles errors gracefully and provides informative error messages.

* **Prerequisites**
To run this bot, you will need the following:

Python (v3.7 or later)
python-telegram-bot library (v13.0.0 or later)
OpenAI API key (Obtain an API key from the OpenAI Developer Portal)
Wolfram Alpha API Key (Obtain an API key from the Wolfram Alpha Developer Portal)
Wikipedia API Key (Create an account on the Wikimedia Developer Portal to obtain an API key)
Google Custom Search JSON API Key (Refer to the Google Developers Console for information on obtaining an API key)

* **Installation**
Git clone this repository and run
```python
pip install -r requirements.txt
```
Make an .env (given example in .env.example file) file and add 
OPENAI_API_KEY= {your openai api key}
TELEGRAM_BOT_TOKEN= {your bot api key obtained from @BotFather in telegram}
ADMIN_USER_IDS={your telegram user key obtained from @userinfobot in telegram}
ALLOWED_TELEGRAM_USER_IDS={user ids whom you want to give access}


Usage
To start the bot, run the following command in the project directory:
```python
python bot/main.py
```
Once the bot is running, find it on Telegram and start a chat with it. You can now use various commands to interact with the bot and access information.

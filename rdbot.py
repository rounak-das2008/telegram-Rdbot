import logging
import random
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv('_TOKEN_')
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def ankur_tmkc(update, context):
    lis1 = ['Ankur bhai, tmkc bhai 🙂', 'Ankur khankir chele bara',
    'Ankur to bara bokachoda', 'Ankur guud marani',
    'Hat bara choto nuni 🥒, beshi kotha bolish na to']
    update.message.reply_text(random.choice(lis1))

def kaptaan_tmkc(update, context):
    lis2 = ['Dhemnaq er maa ke chudi bhai', 'Laura ka Kaptaan  hai',
    'Dhemnaq beta khankir cheley', 'MC Dhemnaq  er bestie ! 😁',
    'TMKC kaptaan, TMKC , bhujecho ? ....T M K C' ]
    update.message.reply_text(random.choice(lis2))
def md_tmkc(update, context):
    lis3 = ["MD banchod tor maa ke chudi rendir chele bara !", "tmkc sid dhemna bhai" ,
    "gudir beta md banchod", "md khankir chudi 💥","MD bhai, TMKC bhai!"]
    update.message.reply_text (random.choice(lis3))
def tmkc_everyone(update,context):
    update.message.reply_text('TMKC everyone 😎!')
def deba_tmkc(update, context):
    lis6 = ['Dhemnanko bhai, tmkc bhai! 🥱', 'Deba to banchod bara', 'Dhur bara deba banchod', 'Deba khankur chele']
    update.message.reply_text(random.choice(lis6))

# def ooh_bhai(update, context):
#       update.sendAudio(audio=open('ooh_bhai.mp3', 'rb'))

def echo(update, context):
	"""Echo the user message."""
	lis4 = ['tor baah er mkc bhai', 'tor baah er maa ke ei chudey ashlam',
	'hai hai tor baah er pod merediyechi ami', 
	'tor baah er puro choddo gusti ke chudi bara']
	
	user_id = update.message.from_user.id
	
	if update.message.from_user.username == None:
		user_name = update.message.from_user.first_name       #first name
	else:
		user_name = update.message.from_user.username
		
	mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
	
	for i in ['baah', 'baaah', 'baaaahh', 'bah']:
		if i in update.message.text.lower():
			if user_name != 'Name_Rounak':
				update.message.reply_text(random.choice(lis4))
				break
		else:
			pass
	lis5 = ['tor maa ke chudi','khankir chele', 'guud marani','gandur baccha',
	'bokachoda', 'tmkc', 'laurar baal']
	for j in ['rd', 'dhounak' ,'dhemnak', 'ranaghat']:
		if j in update.message.text or j.upper() in update.message.text or j.capitalize() in update.message.text:
			
			if user_name != 'Name_Rounak':
			# try:
				update.message.reply_text(random.choice(lis5) + ' ' + mention,parse_mode="Markdown")

			# except:
			# 	update.message.reply_text(random.choice(lis5) + ' @' +name['first_name'])

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("tmkc_ankur", ankur_tmkc))
    dp.add_handler(CommandHandler("tmkc_dhemnaq", kaptaan_tmkc))
    dp.add_handler(CommandHandler("tmkc_everyone", tmkc_everyone))
    # dp.add_handler(CommandHandler("ooh_bhai", ooh_bhai))
    dp.add_handler(CommandHandler("tmkc_md", md_tmkc))
    dp.add_handler(CommandHandler("tmkc_dhemnanko", deba_tmkc))


    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

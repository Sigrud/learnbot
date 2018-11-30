from telegram.ext import Updater, CommandHandler,MessageHandler , Filters
import logging
import settings
import ephem, datetime

date=datetime.datetime.now()
today=date.strftime('%Y-%m-%d')



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
	level = logging.INFO,
	filename = 'bot.log')

def greet_user(bot,update):
	text='вызван  /start'
	logging.info(text)
	update.message.reply_text(text)
	print(update.message.text)

def  talk_to_me(bot,update):
	user_text = "Привет {} Ты написал : {}".format(update.message.chat.first_name,
		update.message.text)
	logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
		update.message.chat.id, update.message.text)
	update.message.reply_text(user_text)



def talk_about_planet(bot,update):
	
	logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
		update.message.chat.id, update.message.text)
	user_text = (update.message.text)
	planets=user_text.split()
	name_pl=(planets[1].strip()).title()
	pl=getattr(ephem,name_pl)(today)	
	update.message.reply_text(f'Планета {name_pl} \
		находится в созвездии \n{ephem.constellation(pl)}')
	


def main():
	mybot = Updater(settings.API_KEY, 
		request_kwargs=settings.PROXY)

	logging.info('бот запускается')

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start',greet_user))
	dp.add_handler(MessageHandler(Filters.text,talk_to_me))
	dp.add_handler(CommandHandler('planet',talk_about_planet))

	mybot.start_polling()
	mybot.idle()



main()
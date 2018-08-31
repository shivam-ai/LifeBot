from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram
import logging as log 
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT)


class Sender:   

	def __init__(self, chatid, bot, update):
		self.chatid= chatid  
		self.bot= bot 
		self.update= update

	def sendText(self, msg):
		log.info("Sending text: "+msg)
		self.bot.send_message(chat_id= self.chatid,text= msg)

	def sendTextM(self, msg):
		log.info("Sending text: "+msg)
		self.bot.send_message(chat_id= self.chatid,text= msg, parse_mode=telegram.ParseMode.MARKDOWN)


	def sendImg(self, url): 
		pass

	def sendAudio(self, url):
		log.info("Sending Audio: "+url)
		self.bot.send_audio(chat_id=self.chatid, audio=open(url, 'rb'), timeout=1000)

	def sendVideo(self, url):
		pass 

	def sendDoc(self, url):
		pass
from haikugen import gethaiku

updater = Updater(token='')
dispatcher = updater.dispatcher


def start(bot, update):
   bot.send_message(chat_id=update.message.chat_id, text=gethaiku())


start_handler = CommandHandler('start', start)


def inline_haiku(bot, update):
    results = list()
    query = update.inline_query.query
    haiku = gethaiku()
    results.append(
        InlineQueryResultArticle(

            id = query.upper(),

            title = "haiku",
            description = haiku,

            input_message_content = InputTextMessageContent(haiku)    ) )
    bot.answer_inline_query(update.inline_query.id,results )


inline_caps_handler = InlineQueryHandler(inline_haiku)

from telegram.ext import Updater
from telegram.ext import CommandHandler

dispatcher.add_handler(start_handler)

from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

dispatcher.add_handler(inline_caps_handler)
updater.start_polling()
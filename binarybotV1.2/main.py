from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import API_ID, API_HASH, BOT_TOKEN
from utiles import binary
from __version__ import __version__

#setup the bot 
bi = binary()

app = Client(
    'binary bot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# tracking the user status
user_status = None

          
# inline keyboard 
start_buttons = [
    [
        InlineKeyboardButton(text='text to binary', callback_data='bi'),
        InlineKeyboardButton(text='binary to text', callback_data='text')
    ]
]
#start message
@app.on_message(filters.command('start'))
def start(_, message):
    start_message = 'Welcome to binary bot. Please make a choice:'
    markup = InlineKeyboardMarkup(start_buttons)
    app.send_message(
        message.chat.id,
        text=start_message,
        reply_markup=markup
    )
# callback query
@app.on_callback_query()
def callback(_, callback_query: CallbackQuery):
    global user_status
    if callback_query.data == 'bi':
        user_status = 'waiting for binary'
        app.send_message(callback_query.message.chat.id, 'Send me text to turn it into a binary code')
    elif callback_query.data == 'text':
        user_status = 'waiting for text'
        app.send_message(callback_query.message.chat.id, 'Send me a binary code to turn it into a string')
#message_handler
@app.on_message(filters.text)
def message_handler(_, message):
    global user_status
    if user_status == 'waiting for binary':
        try:
            binary_result = bi.into_binary(message.text)
            message.reply_text(f'Here is the binary code:\n{binary_result}')
        except:
            message.reply_text('Sorry, I cannot turn this into binary.')
    elif user_status == 'waiting for text':
        try:
            binary_string = bi.binary_to_string(message.text)
            message.reply(f'Here is the text of the binary code:\n\n{binary_string}')
        except:
            message.reply('Sorry, I cannot turn this into a string.')
#run the app
app.run()

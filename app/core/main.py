from config import *
from profile import Profile
import telebot
from telebot.types import ReplyKeyboardMarkup, ForceReply

bot = telebot.TeleBot(TOKEN_TELEGRAM)
accounts = {}


@bot.message_handler(commands=['iniciar','start'])
def cmd_start(message):
    bot.send_message(message.chat.id,'¡Bienvenido!, Puedes escribir /info para conocer nuestros comandos')


@bot.message_handler(commands=['ayuda'])
def cmd_help(message):
    bot.send_message(message.chat.id,'Puedes contactar a @amner_py para cualquier duda')


@bot.message_handler(commands=['editar_cuenta'])
def cmd_edit_account(message):
    if message.chat.id in accounts:
        markup = ForceReply()
        name = bot.send_message(message.chat.id, 'Ingresa tu nombre', reply_markup=markup)
        bot.register_next_step_handler(name, set_address)
    else:
        bot.send_message(message.chat.id,'No tiene ninguna cuenta asociada ingrese el comando: /crear_cuenta para crearse una cuenta')


@bot.message_handler(commands=['crear_cuenta'])
def cmd_create_account(message):
    if message.chat.id in accounts:
        bot.send_message(message.chat.id,'Ya posee una cuenta, puede editar sus datos con /editar_cuenta')
    else:
        markup = ForceReply()
        name = bot.send_message(message.chat.id,'Ingresa tu nombre',reply_markup=markup)
        bot.register_next_step_handler(name,set_address)


def set_address(message):
    accounts[message.chat.id] = {}
    accounts[message.chat.id]['id'] = message.chat.id
    accounts[message.chat.id]['name'] = message.text
    markup = ForceReply()
    address = bot.send_message(message.chat.id,'Ingresa tu dirección',reply_markup=markup)
    bot.register_next_step_handler(address,account_created)


def account_created(message):
    accounts[message.chat.id]['address'] = message.text
    profile_acccount = Profile()
    profile_acccount.set_id(accounts[message.chat.id]['id'])
    profile_acccount.set_name(accounts[message.chat.id]['name'])
    profile_acccount.set_address(accounts[message.chat.id]['address'])
    msn = f'''
    Se ha creado de forma exitosa. :D 
    Nombre: {profile_acccount.get_name()}
    Dirección: {profile_acccount.get_address()}
    '''
    bot.send_message(message.chat.id,msn)


@bot.message_handler(commands=['mi_cuenta'])
def cmd_my_account(message):
    if message.chat.id in accounts:
        msg = f'''
            Los datos de su cuenta son:
            Nombre: {accounts[message.chat.id]['name']}
            Dirección: {accounts[message.chat.id]['address']}
            '''
        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id,'No tiene ninguna cuenta asociada ingrese el comando: /crear_cuenta para crearse una cuenta')


@bot.message_handler(commands=['info'])
def cmd_info(message):
    all_commands = '''
    Los comandos que puedes usar son:
    /info
    /iniciar
    /ayuda
    /crear_cuenta
    /mi_cuenta
    /editar_cuenta
    '''
    bot.send_message(message.chat.id,all_commands)


if __name__ == '__main__':
    print('Starting bot...')
    print('Bot is listening...')
    bot.infinity_polling()
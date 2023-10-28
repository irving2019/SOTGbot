import telebot
from telebot import types
from Groups import *
from Locations import *
from Guns import *
from Armors import *
from Kordon import *

botTimeWeb = telebot.TeleBot('Ваш токен от BotFather')

@botTimeWeb.message_handler(commands=['start'])
def startbot(message):
    first_message = (f"Добро пожаловать в зону <b>{message.from_user.first_name}</b>! "
                     f"Меня зовут лейтенант Слипченко, я из группировки "
                     f" {Military_Group} и мы здесь ох как"
                     f" не любим разного рода сталкеров. "
                     f"\nВижу ты не особо общителен, да и правильно, здесь болтливых не любят. "
                     f"Давай-ка я объясню тебе, что к чему, пока ты не стал очередным аномальным фаршем.")

    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text="Дерзай", callback_data="yes")
    markup.add(button_yes)
    botTimeWeb.send_message(message.chat.id, first_message, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call: call.data == "yes")
def response(function_call):
    second_mess = (f"Итак, ты на территории зоны отчуждения, сейчас мы находимся непосредственно"
                   f" на локации {Cordon_location} - это относительно безопасное место для новичков, но"
                   f" и здесь хватает всяких тварей и даже Бандюков. В данной локации базируются"
                   f" две группировки, это {Single_Group} и непосредственно мы, {Military_Group}."
                   f" К северу отсюда находится {Dump_location}, там сидят {Bandit_Group}, а также там"
                   f" огромное количество артефактов, артефактов больше чем на Свалке, пожалуй "
                   f" можно найти только у самого центра зоны хех, а к западу находятся {Swamps_location},"
                   f" очень не рекомендую туда суваться если ты не любитель поплавать в трясине, "
                   f" да и делать там особо нечего, поговаривают, что там сидят {Clear_sky_Group}"
                   f" и какие-то недобандиты {Renegade_Group}, но всем на них плевать если честно."
                   f" В общем не важно какой дорогой ты пойдёшь, главное лишь то, что за твой проход сюда"
                   f" очень хорошо заплатили, лишь поэтому ты ещё дышишь и можешь говорить стоя здесь!")

    markup = types.InlineKeyboardMarkup()
    button_armor = types.InlineKeyboardButton(text="Мне должны были выдать экипировку",
                                              callback_data="Armor")
    markup.add(button_armor)
    botTimeWeb.send_message(function_call.message.chat.id, second_mess, parse_mode='html', reply_markup=markup)
    botTimeWeb.answer_callback_query(function_call.id)


@botTimeWeb.callback_query_handler(func=lambda call: call.data == "Armor")
def answer(function_call):
    double_mess = (f"Получите, распишитесь, хех."
                   f"\nСлипченко достал рацию и начал грубым тоном отдавать приказ:"
                   f"\n-Пилипенко! Тут новый кусок мяса, выдай ему всё как договаривались!"
                   f"\n-Принято!"
                   f"\nНу что-же, забирай свой \"хабар\" и дуй отсюда пока начальство не пришло."
                   f"И кстати, ты бы подумал, может вступишь к нам? Нам крепкие парни вроде тебя всегда нужны.")

    markup = types.InlineKeyboardMarkup()
    button_question = (types.InlineKeyboardButton(text="Я подумаю на досуге", callback_data="No"))
    markup.add(button_question)
    botTimeWeb.send_message(function_call.message.chat.id, double_mess, parse_mode='html', reply_markup=markup)
    botTimeWeb.answer_callback_query(function_call.id)


@botTimeWeb.callback_query_handler(func=lambda call: call.data == "No")
def answer(function_call):
    triple_mess = f"Как знаешь, удачи, \"сталкер\" {function_call.from_user.first_name} гы-гы"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="К Пилипенко", callback_data="Go_Armor"))
    botTimeWeb.send_message(function_call.message.chat.id, triple_mess, parse_mode='html', reply_markup=markup)
    botTimeWeb.answer_callback_query(function_call.id)


@botTimeWeb.callback_query_handler(func=lambda call: call.data == "Go_Armor")
def pilipenko(function_call):
    pilipenko_mess = (f"Привет {function_call.from_user.first_name}! Вот твоя экипировка: "
                      f"\nПолучено:\n{pm.name}\n{knife.name}\n{leather_jacket.name}"
                      f"\nА теперь дуй в лагерь новичков, оттуда начнётся твой путь")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="В лагерь новичков", callback_data="Kordon"))
    botTimeWeb.send_message(function_call.message.chat.id, pilipenko_mess, parse_mode='html', reply_markup=markup)
    botTimeWeb.answer_callback_query(function_call.id)

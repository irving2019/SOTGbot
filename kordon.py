from main import *

@botTimeWeb.callback_query_handler(func=lambda call: call.data == "Kordon")
def kordon(function_call):
    cordmes = "Локация кордон, деревня новичков"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("🎒 Инвентарь")
    btn2 = types.KeyboardButton("⬆️ Вперёд")
    btn3 = types.KeyboardButton("🔍 Осмотреться")
    btn4 = types.KeyboardButton("⬅️ Влево")
    btn5 = types.KeyboardButton("⬇️ Назад")
    btn6 = types.KeyboardButton("➡️ Вправо")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    botTimeWeb.send_message(function_call.message.chat.id, cordmes, parse_mode='html', reply_markup=markup)
    botTimeWeb.answer_callback_query(function_call.id)

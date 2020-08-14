from telebot import types

keyboard_hello = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_1 = types.KeyboardButton(text='Прогноз на сьогодні')
button_2 = types.KeyboardButton(text='Прогноз на завтра')
button_3 = types.KeyboardButton(text='Інше')
keyboard_hello.add(button_1, button_2)


keyboard_test2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_1 = types.KeyboardButton(text='You are kek2')
button_2 = types.KeyboardButton(text='No u2')
keyboard_test2.add(button_1, button_2)


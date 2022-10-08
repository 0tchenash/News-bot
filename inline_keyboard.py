from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_ALLNEWS = InlineKeyboardButton('All news', callback_data='news')
BTN_LOCALNEWS = InlineKeyboardButton('Local news', callback_data='localnews')
BTN_HOLIDAYSTODAY = InlineKeyboardButton('What holidays are today?', 
                                    callback_data='holidays')

ALLNEWS = InlineKeyboardMarkup().add(BTN_LOCALNEWS, BTN_HOLIDAYSTODAY)
LOCALNEWS = InlineKeyboardMarkup().add(BTN_ALLNEWS).add(BTN_HOLIDAYSTODAY)
HOLIDAYSTODAY = InlineKeyboardMarkup().add(BTN_ALLNEWS, BTN_LOCALNEWS)
HELP = InlineKeyboardMarkup().add(BTN_ALLNEWS, BTN_LOCALNEWS).add(BTN_HOLIDAYSTODAY)

# BTN_HELP = InlineKeyboardButton('Help', callback_data='help')

# HELP = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND).add(BTN_SUN_TIME)
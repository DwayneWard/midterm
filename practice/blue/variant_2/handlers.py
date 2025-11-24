"""
Модуль с обработчиками команд и сообщений бота.
"""
import telebot
from telebot import types

from api_client import get_exchange_rates
from storage import get_user_favorites, add_favorite_pair, remove_favorite_pair

def register_handlers(bot: telebot.TeleBot):
    """
    Регистрация всех обработчиков команд и сообщений.
    
    TODO: Реализовать функцию:
    1. Зарегистрировать обработчик команды /start используя декоратор @bot.message_handler(commands=['start'])
       Функция-обработчик должна вызывать start_handler(bot, message)
    
    2. Зарегистрировать обработчик команды /rates используя декоратор @bot.message_handler(commands=['rates'])
       Функция-обработчик должна вызывать rates_handler(bot, message)
    
    3. Зарегистрировать обработчик команды /favorites используя декоратор @bot.message_handler(commands=['favorites'])
       Функция-обработчик должна вызывать favorites_handler(bot, message)
    
    4. Зарегистрировать обработчик текстовых сообщений используя декоратор @bot.message_handler(func=lambda message: True)
       Функция-обработчик должна вызывать rates_handler(bot, message)
    
    5. Зарегистрировать обработчик callback-запросов от inline-кнопок используя декоратор @bot.callback_query_handler(func=lambda call: True)
       Функция-обработчик должна вызывать button_callback_handler(bot, call)
    """
    pass


def start_handler(bot: telebot.TeleBot, message: types.Message):
    """
    Обработчик команды /start.
    
    TODO: Реализовать обработчик:
    1. Отправить приветственное сообщение пользователю используя bot.send_message()
    2. Сообщение должно содержать информацию о доступных командах:
       - /rates <валюта> - получить курсы валют (например, /rates USD)
       - /favorites - показать избранные валютные пары
    """
    pass


def rates_handler(bot: telebot.TeleBot, message: types.Message):
    """
    Обработчик команды /rates и текстовых сообщений с кодом валюты.
    
    TODO: Реализовать обработчик:
    1. Получить код валюты:
       - Если это команда /rates, взять валюту из message.text (разделить по пробелам и взять второй элемент, если есть)
       - Если это текстовое сообщение, взять весь message.text как код валюты (привести к верхнему регистру)
    
    2. Если валюта не указана (пустая строка или только команда), отправить сообщение: 
       "Пожалуйста, укажите код валюты (например, USD, EUR, RUB)"
    
    3. Вызвать get_exchange_rates(base_currency) для получения данных о курсах
    
    4. Если данные получены успешно (не None):
       - Извлечь из ответа: 
         * Базовую валюту: data['base']
         * Дата обновления: data['date']
         * Курсы: data['rates'] (словарь с курсами)
       - Выбрать несколько популярных валют для отображения (например, USD, EUR, RUB, GBP, JPY)
       - Сформировать сообщение вида:
         "Курсы валют относительно {base}:
         Дата: {date}
         
         USD: {rate_usd}
         EUR: {rate_eur}
         RUB: {rate_rub}
         GBP: {rate_gbp}
         JPY: {rate_jpy}"
       - Создать inline-кнопку "Добавить в избранное" для каждой популярной валюты
         callback_data должен быть f"add_{base}_{target}" (например, "add_USD_EUR")
       - Создать клавиатуру и добавить кнопки
       - Отправить сообщение с клавиатурой
       Примечание: если какой-то валюты нет в rates, пропустите её
    
    5. Если данные не получены (None):
       - Отправить сообщение: "Не удалось получить курсы валют. Проверьте код валюты."
    
    6. Обработать возможные исключения используя try/except
    """
    pass


def favorites_handler(bot: telebot.TeleBot, message: types.Message):
    """
    Обработчик команды /favorites - показывает список избранных валютных пар.
    
    TODO: Реализовать обработчик:
    1. Получить user_id
    
    2. Получить список избранных валютных пар через соответсвующий функционал
    
    3. Если список пуст:
       - Отправить сообщение: "У вас пока нет избранных валютных пар. Используйте /rates для добавления."
    
    4. Если список не пуст:
       - Создать inline-клавиатуру
       - Для каждой пары создать кнопку:
         * Текст кнопки - валютная пара (например, "USD/EUR")
         * callback_data для каждой кнопки: f"rates_{base}_{target}" (например, "rates_USD_EUR")
       - Добавить кнопку "Очистить все" с callback_data="clear_all"
       - Отправить сообщение: "Ваши избранные валютные пары:" с клавиатурой
    """
    pass


def button_callback_handler(bot: telebot.TeleBot, call: types.CallbackQuery):
    """
    Обработчик нажатий на inline-кнопки.
    
    TODO: Реализовать обработчик:
    1. Получить callback_data из call.data
    
    2. Обработать разные типы callback_data:
       a) Если callback_data начинается с "add_":
          - Извлечь коды валют из callback_data (формат: "add_BASE_TARGET")
          - Получить user_id
          - Вызвать add_favorite_pair(user_id, base_currency, target_currency)
          - Если успешно: ответить "Пара {BASE}/{TARGET} добавлена в избранное"
          - Если уже была: ответить "Пара {BASE}/{TARGET} уже в избранном"
       
       b) Если callback_data начинается с "rates_":
          - Извлечь коды валют из callback_data (формат: "rates_BASE_TARGET")
          - Вызвать get_exchange_rates(base_currency)
          - Если данные получены, найти курс для target_currency в data['rates']
          - Сформировать сообщение: "Курс {BASE}/{TARGET}: {rate}"
          - Отправить сообщение с данными о курсе
          - Создать кнопку "Добавить в избранное" если пары ещё нет в избранном
       
       c) Если callback_data равен "clear_all":
          - Получить user_id
          - Получить список пар через соответсвующий функционал
          - Для каждой пары извлечь base и target и вызвать remove_favorite_pair(user_id, base, target)
          - Ответить: "Все пары удалены из избранного"
    
    3. После обработки вызвать bot.answer_callback_query(call.id) чтобы убрать индикатор загрузки
    
    4. Обработать возможные исключения используя try/except
    """
    pass


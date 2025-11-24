"""
Модуль с обработчиками команд и сообщений бота.
"""
import telebot
from telebot import types

from api_client import get_news
from storage import get_user_favorites, add_favorite_category, remove_favorite_category

def register_handlers(bot: telebot.TeleBot):
    """
    Регистрация всех обработчиков команд и сообщений.
    
    TODO: Реализовать функцию:
    1. Зарегистрировать обработчик команды /start используя декоратор @bot.message_handler(commands=['start'])
       Функция-обработчик должна вызывать start_handler(bot, message)
    
    2. Зарегистрировать обработчик команды /news используя декоратор @bot.message_handler(commands=['news'])
       Функция-обработчик должна вызывать news_handler(bot, message)
    
    3. Зарегистрировать обработчик команды /favorites используя декоратор @bot.message_handler(commands=['favorites'])
       Функция-обработчик должна вызывать favorites_handler(bot, message)
    
    4. Зарегистрировать обработчик текстовых сообщений используя декоратор @bot.message_handler(func=lambda message: True)
       Функция-обработчик должна вызывать news_handler(bot, message)
    
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
       - /news <категория> - получить новости по категории (например, /news technology)
       - /favorites - показать избранные категории
    """
    pass


def news_handler(bot: telebot.TeleBot, message: types.Message):
    """
    Обработчик команды /news и текстовых сообщений с категорией новостей.
    
    TODO: Реализовать обработчик:
    1. Получить категорию новостей:
       - Если это команда /news, взять категорию из message.text (разделить по пробелам и взять второй элемент, если есть)
       - Если это текстовое сообщение, взять весь message.text как категорию (привести к нижнему регистру)
    
    2. Если категория не указана (пустая строка или только команда), отправить сообщение: 
       "Пожалуйста, укажите категорию новостей (например, technology, business, sports)"
    
    3. Вызвать get_news(category) для получения данных о новостях
    
    4. Если данные получены успешно (не None):
       - Извлечь из ответа: 
         * Статус: data['status']
         * Количество новостей: data['totalResults']
         * Статьи: data['articles'] (массив)
       - Взять первые 3-5 новостей из массива articles
       - Для каждой новости извлечь: title, description, url
       - Сформировать сообщение вида:
         "Новости по категории {category}:
         Всего найдено: {totalResults}
         
         1. {title}
         {description}
         {url}
         
         2. {title}
         ..."
       - Создать inline-кнопку "Добавить категорию в избранное"
         callback_data должен быть f"add_{category}"
       - Создать клавиатуру и добавить кнопку
       - Отправить сообщение с клавиатурой
       Примечание: если description отсутствует, используйте только title и url
    
    5. Если данные не получены (None):
       - Отправить сообщение: "Не удалось получить новости. Проверьте категорию."
    
    6. Обработать возможные исключения используя try/except
    """
    pass


def favorites_handler(bot: telebot.TeleBot, message: types.Message):
    """
    Обработчик команды /favorites - показывает список избранных категорий.
    
    TODO: Реализовать обработчик:
    1. Получить user_id
    
    2. Получить список избранных категорий через соответсвующий функционал
    
    3. Если список пуст:
       - Отправить сообщение: "У вас пока нет избранных категорий. Используйте /news для добавления."
    
    4. Если список не пуст:
       - Создать inline-клавиатуру
       - Для каждой категории создать кнопку:
         * Текст кнопки - название категории
         * callback_data для каждой кнопки: f"news_{category}"
       - Добавить кнопку "Очистить все" с callback_data="clear_all"
       - Отправить сообщение: "Ваши избранные категории:" с клавиатурой
    """
    pass


def button_callback_handler(bot: telebot.TeleBot, call: types.CallbackQuery):
    """
    Обработчик нажатий на inline-кнопки.
    
    TODO: Реализовать обработчик:
    1. Получить callback_data из call.data
    
    2. Обработать разные типы callback_data:
       a) Если callback_data начинается с "add_":
          - Извлечь категорию из callback_data (убрать префикс "add_")
          - Получить user_id
          - Вызвать add_favorite_category(user_id, category)
          - Если успешно: ответить "Категория {category} добавлена в избранное"
          - Если уже была: ответить "Категория {category} уже в избранном"
       
       b) Если callback_data начинается с "news_":
          - Извлечь категорию из callback_data (убрать префикс "news_")
          - Вызвать get_news(category)
          - Если данные получены, сформировать сообщение как в news_handler
          - Отправить сообщение с данными о новостях
          - Создать кнопку "Добавить в избранное" если категории ещё нет в избранном
       
       c) Если callback_data равен "clear_all":
          - Получить user_id
          - Получить список категорий через соответсвующий функционал
          - Для каждой категории вызвать remove_favorite_category(user_id, category)
          - Ответить: "Все категории удалены из избранного"
    
    3. После обработки вызвать bot.answer_callback_query(call.id) чтобы убрать индикатор загрузки
    
    4. Обработать возможные исключения используя try/except
    """
    pass


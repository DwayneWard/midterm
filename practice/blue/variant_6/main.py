"""
Главный файл для запуска Telegram-бота рецептов.
"""
import telebot

from config import BOT_TOKEN
from handlers import register_handlers

# TODO: Создать экземпляр бота используя BOT_TOKEN из config
# Подсказка: используйте telebot.TeleBot(BOT_TOKEN)
# bot = ...

# TODO: Зарегистрировать обработчики команд
# Вызвать функцию register_handlers(bot) из модуля handlers

# TODO: Запустить бота в режиме polling
# Используйте bot.infinity_polling()


def main():
    """Запуск бота."""
    pass


if __name__ == "__main__":
    main()


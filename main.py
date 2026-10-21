import os
import time
import requests

# Токен зашит прямо в код для удобства
TOKEN = "8480835882:AAGtP6aE0Die8mitp_8S6j3p6VydQay4HpE"
URL = f"https://api.telegram.org/bot{TOKEN}/"

print("Бот TaskEarned успешно запущен!")

def get_updates(offset=None):
    url = f"{URL}getUpdates?timeout=30"
    if offset:
        url += f"&offset={offset}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return {}

def send_message(chat_id, text):
    url = f"{URL}sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        if "result" in updates:
            for update in updates["result"]:
                offset = update["update_id"] + 1
                if "message" in update and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"]["text"]
                    user = update["message"]["from"]
                    username = user.get("username", "не указан")
                    user_id = user.get("id")

                    if text.startswith("/start"):
                        msg = (
                            "💼 <b>Добро пожаловать в TaskEarned!</b>\n\n"
                            "Выполняй простые задания → Получай монеты → Обменивай на подарки.\n\n"
                            "📋 <b>Доступные команды:</b>\n"
                            "/start - Начать работу\n"
                            "/profile - Профиль\n"
                            "/tasks - Задания\n"
                            "/balance - Баланс\n"
                            "/store - Магазин\n"
                            "/help - Помощь\n\n"
                            "🚀 Начни зарабатывать уже сегодня!"
                        )
                        send_message(chat_id, msg)

                    elif text.startswith("/profile"):
                        msg = (
                            f"👤 <b>Ваш профиль:</b>\n\n"
                            f"🆔 ID: <code>{user_id}</code>\n"
                            f"@{username}\n\n"
                            f"📊 Выполнено заданий: 0\n"
                            f"💰 Баланс: 0 монет\n\n"
                            f"🏷 Версия бота: v0.1.0 Beta"
                        )
                        send_message(chat_id, msg)

                    elif text.startswith("/tasks"):
                        send_message(chat_id, "📌 На данный момент доступных заданий нет. Следите за обновлениями в нашем канале!")

                    elif text.startswith("/balance"):
                        send_message(chat_id, "💰 Ваш баланс: <b>0 монет</b>.")

                    elif text.startswith("/store"):
                        send_message(chat_id, "🛒 Магазин подарков и игровой валюты пуст. Скоро здесь появятся товары!")

                    elif text.startswith("/help"):
                        send_message(chat_id, "ℹ️ По всем вопросам обращайтесь к администратору: @Colanov")

        time.sleep(1)

if __name__ == "__main__":
    main()
                        

# Messenger
import flask
import datetime
from datetime import datetime, date, time

#now = datetime.now()
timenow = datetime.now().strftime("%H:%M")

all_messages = [] # Список всех сообщений
# append - добавить новый элемент в конец списка
all_messages.append({
    "text": "Это первый мессадж",
    "time": "00:00",
    "sender": "root"
})

# Функция для печати всех сообщений
def display_all_messages():
    for message in all_messages:
        name = message["sender"]
        text = message["text"]
        time = message["time"]
        print(f"[{name}]: {text} / {time}")

# display_all_messages()

# Функция для добавления нового сообщения 
def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": timenow # TODO: Подставить текущее время datetime.now, strftime # Сделано
    }
    all_messages.append(new_message)

add_message("Mike", "Hello ALL")
add_message("Vasya", "Nice to meet you")
display_all_messages()


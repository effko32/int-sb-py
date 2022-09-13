# import flask
from datetime import datetime, date, time
from flask import Flask, request, render_template
import json
# flask - название пакета
# Flask - класс "веб-приложения"

app = Flask(__name__)

# Загрузка данных из файла
def load_chat():
    with open("C:\\repos\\int-sb-py\\chat.json", "r") as json_file: # Открыть файл на чтение (r)
        data = json.load(json_file) # Загрузить файл в переменную data
        return data["messages"] # Взять messages из данных

all_messages = load_chat() # Загрузить в all_messages

# Запись данных в файл
def save_chat():
    data = {"messages": all_messages} # Готовим данные
    with open("C:\\repos\\int-sb-py\\chat.json", "w") as json_file: # Открыть для записи (w)
        json.dump(data, json_file) # Сохранить данные в файл

@app.route("/chat")
def display_chat():
    return render_template ("form.html")

# return - возврат, результат работы функции
@app.route("/")
def index_page():
    return "Welcome to Skillbox Messenger"

@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}

# http://127.0.0.1:5000/send_message?name=Mike&text=Hello

@app.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    save_chat()
    return "OK"

def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M"),
    }
    all_messages.append(new_message)

# add_message("Mike", "Test")

app.run() # Запуск приложения

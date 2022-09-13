print("Всем приветы в этом чате!")

# Variables
speaker = "Mike"
duration = 110
title = "Знакомимся с Python"
# print(title)

duration_hours = round(duration / 60, 2)
print(f"Вебинар {title} будет длится около {duration_hours} часов, ведущий сегодня: {speaker}")
minutes = 158
hours = int(minutes/60)
rest = minutes % 60

print (f"В минутах ровно {hours} часов и {rest} минут")

# Сколько часов в 110 минутах
# h = int(110 / 60)
# print (h)
# Сколько минут осталось?
# 110 % 60

# Списки
visitors = ["Дмитрий", "Никита", "Sergey", "Vasya"]
# print(visitors[0])
# print(visitors[1:3])

# Циклы
# Для каждого посетителя (объявляем переменную visitor) в списке посетителей сделать
for visitor in visitors:
    print (f"Приветствуем слушателя {visitor}")

# Словать (dictionary)
# Ключ: значение
message = {
    "text": "Всем привет",
    "time": "23:09",
    "sender": "Мистер Майк"
}

# Messenger
all_messages = [] # Список всех сообщений
# append - добавить новый элемент в конец списка
all_messages.append({
    "text": "Это первый мессадж",
    "time": "00:00",
    "sender": "root"
})

print(all_messages)
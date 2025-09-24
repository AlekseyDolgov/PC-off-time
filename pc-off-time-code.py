import os
from datetime import datetime, timedelta

# Вводим целевое время
target_time_str = input("Введи время в формате ЧЧ:ММ -> ")

# Текущее время
now = datetime.now()

# Преобразуем введённую строку в объект времени
target_time = datetime.strptime(target_time_str, "%H:%M").time()

# Создаём datetime с этим временем для сегодняшнего дня
target_datetime = datetime.combine(now.date(), target_time)

# Если указанное время уже прошло сегодня → переносим на завтра
if target_datetime <= now:
    target_datetime += timedelta(days=1)

# Считаем разницу
seconds_left = int((target_datetime - now).total_seconds())

print(f"До {target_time_str} осталось {seconds_left} секунд.")

# Отменяем предыдущее выключение (если было)
os.system("shutdown -a")

# Устанавливаем новый таймер выключения
os.system(f"shutdown -s -t {seconds_left}")
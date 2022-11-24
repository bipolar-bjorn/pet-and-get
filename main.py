import random
import time

# Рандомайзер приоритетов снимает груз ответственности за принятие решений
# и расстановки приоритетов задачам, которые надо делать.

# Алгоритм:
# 1. Получить количество и список задач
# 2. Закинуть их в список


def main():
    greetings = input('Привет дорогой друг! Как тебя зовут?: ')
    print(f'Очень приятно {greetings}',
          f'Итак...', sep='\n')
    time.sleep(2)
    tasks_count = int(input(f"Сколько задач ты себе напланировал, {greetings}?: "))  # количество задач
    tasks_name = [input("Перечисли их: (по одной задаче на строчке) ") for _ in range(tasks_count)]  # список задач

    # переменные для согласования в принтах
    task_s = "задача"
    task_s2 = "задачи"
    task_pl = "задач"

    # как реализовать веса и очки приоритетов: цифры или словесные выражения?
    priority_digits = [int(i) for i in range(1, tasks_count + 1)]
    print(max(priority_digits))

    # согласование в принтах
    if tasks_count == 1 or tasks_count == 21 or tasks_count == 31:
        print(f'Значит {tasks_count} {task_s}, давай посмотрим с чего же начать...')
    elif tasks_count == 2 or tasks_count == 3 or tasks_count == 4:
        print(f'Значит {tasks_count} {task_s2}, давай посмотрим с чего же начать...')
    elif tasks_count == 22 or tasks_count == 23 or tasks_count == 24:
        print(f'Значит {tasks_count} {task_s2}, давай посмотрим с чего же начать...')
    else:
        print(f'Значит {tasks_count} {task_pl}, давай посмотрим с чего же начать...')

    time.sleep(3)
    print(f'Составляю список задач по степени важности')
    time.sleep(1)
    print(f'Итак...')

    while tasks_count > 0:
        a = random.randrange(tasks_count)
        print(f'{min(priority_digits)} - {tasks_name[a]}')
        tasks_count -= 1
        priority_digits.remove(priority_digits[0])
        tasks_name.remove(tasks_name[a])

    time.sleep(2)
    if tasks_count == 0:
        print("Приоритеты расставлены!", "Можно начинать с первого", sep='\n')


if __name__ == "__main__":
    main()

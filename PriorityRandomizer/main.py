import random
import time
import pymorphy2

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
    
    print(spell_check(tasks_count))

    # как реализовать веса и очки приоритетов: цифры или словесные выражения?
    priority_digits = [int(i) for i in range(1, tasks_count + 1)]
    

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


def spell_check(digit):
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse('Задача')[0]
    return f'Значит, {digit} {p.make_agree_with_number(digit).word}, давай посмотрим с чего же начать...'

        
if __name__ == "__main__":
    main()

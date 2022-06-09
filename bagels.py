import random

HINTS = ['Pico', 'Fermi', 'Bagels']
NUM_DIGITS = 3
MAX_GUESSES = 10


def check_num(lst: list, number: list) -> str:
    """Проверяем числа пользователя и добавляем результат в lst_hints"""
    lst_hints = []

    for i, num in enumerate(lst):
        if num in number:
            if num == number[i]:
                lst_hints.append(HINTS[1])
            else:
                lst_hints.append(HINTS[0])

    if len(lst_hints) == 0:
        return HINTS[2]

    return ' '.join(lst_hints)


def start_game(num: list) -> None:
    """Проверяем каждую попытку через функцию check_num"""
    flag = False
    for i in range(1, MAX_GUESSES + 1):
        guess = list(input(f'Попытка #{i}:\n'))
        if guess == num:
            print('Вы сделали это!')
            flag = True
            break
        print(check_num(guess, num))
    if not flag:
        print('Попытки закончились - Вы проиграли:(')


def main():
    """Основная функция"""
    # Описание игры
    print(f"<<Правила игры>>\n"
          f"Вам нужно угадать {NUM_DIGITS} числа за {MAX_GUESSES} попыток.\n"
          f"После каждой попытки будет сплывать подсказка:\n"
          f"{HINTS[0]} - если вы угадали правильную цифру на неправильном месте;\n"
          f"{HINTS[1]} - если в вашей догадке есть правильная цифра на правильном месте;\n"
          f"{HINTS[2]} - если в догадке не содержится правильных цифр;\n")

    while True:
        # случайно число, которое нужно угадать
        number = list(str(random.randint(100, 999)))
        # запускаеп попытки
        start_game(number)
        # будем продолжать играть?
        next_game = input('Вы хотите сыграть еще раз? (yes or no)')
        if next_game != 'yes':
            print('Спасибо за игру!')
            break


if __name__ == '__main__':
    main()

field = list(range(1, 10))
victorious = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def create_field():
    print("---------")
    for i in range(3):
        print("|", field[0 + i * 3], field[1 + i * 3], field[2 + i * 3], "|")
    print("---------")


def cell_selection(choice):
    while True:
        position = int(input(f"Выберите позицию для постановки {choice} "))
        if not (position in (range(1, 10))):
            print("Такой клетки нет 0_0. Попробуйте еще раз")
            continue
        if str(field[position - 1]) in 'X0':
            print("Клетка уже занята. Выберите другую")
            continue
        field[position - 1] = choice
        break


def who_winner():
    for number in victorious:
        if field[number[0] - 1] == field[number[1] - 1] == field[number[2] - 1]:
            return field[number[1] - 1]
    else:
        return False


def le_goooo():
    counter = 0
    while True:
        create_field()
        if counter % 2 == 0:
            cell_selection("X")
        else:
            cell_selection("0")
        if counter > 3:
            winner = who_winner()
            if winner:
                print(f"Победа за {winner}")
                break
        counter += 1
        if counter > 8:
            create_field()
            print("Это ничья. Все молодцы")
            break


le_goooo()

board = list(range(1, 10))


def main(board): #результат
    counter = 0
    win = False
    while not win:
        db(board)
        if counter % 2 == 0:
            ti("X")
        else:
            ti("O")
        counter += 1

        tmp = chkw(board)
        if tmp:
            print(tmp, "победил!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    db(board)


def db(board):  # рисуем доску
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def ti(pt):  # ходы
    valid = False
    while not valid:
        pa = input(f"Куда поставим {pt}? - ")
        try:
            pa = int(pa)
        except ValueError:
            print(
                "Некорректный ввод. Вам необходимо ввести число - координату на доске"
            )
            continue
        if 1 <= pa <= 9:
            if str(board[pa - 1]) not in "XO":
                board[pa - 1] = pt
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print(
                "Некорректный ввод. Вам необходимо ввести число - координату на доске"
            )


def chkw(board):  # проверка победителя
    win_coord = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]


main(board)

input("Нажмите Enter для выхода!")

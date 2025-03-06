# Из модуля inspect импортировать функцию getsource.

from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():

    game = Board()  # Создать игровое поле - объект класса Board.
    current_player = 'X'  # Первыми ходят крестики
    running = True  # Флаг продолжения игры. По умолчанию True
    game.display()  # Отрисовать поле в терминале.

    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                # Тут пользователь вводит координаты ячейки.
                # input дает str ==> преобразуем в int
                row = int(input('Введите номер строки: '))

                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца '
                      'заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue            
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца '
                      'заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:  # Если в блоке try исключения не возникло...
                break

        game.make_move(row, column, current_player)  # Сделать ход
        print('Ход сделан!')
        game.display()  # Перерисовать поле с учётом сделанного хода.

        if game.check_win(current_player):
            print(f'Вы победили {current_player}!')
            save_result(f'Победили {current_player}')
            running = False
        if game.is_board_full():
            print('Ничья!')
            save_result('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


def save_result(strng):
    # Открыть на запись файл example.txt
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(strng + '\n')
        # f.close() - а это уже не нужно, работаем в контекстном менеджере


if __name__ == '__main__':
    main()

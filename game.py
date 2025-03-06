# Из модуля inspect импортировать функцию getsource.

import pygame
from datetime import datetime as dt
from gameparts import Board
# from gameparts.exceptions import FieldIndexError, CellOccupiedError


pygame.init()  # Инициализация графической библиотеки

# Здесь определены разные константы, например
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики.
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
# Задать размер графического окна для игрового поля.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установить заголовок окна.
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом.
screen.fill(BG_COLOR)


# Функция, которая отвечает за отрисовку горизонтальных и вертикальных линий.
def draw_lines():
    # Горизонтальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # Вертикальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


# Функция, которая отвечает за отрисовку фигур
# (крестиков и ноликов) на доске.
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def save_result(strng):
    # Открыть на запись файл example.txt
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(strng + '\n')
        # f.close() - а это уже не нужно, работаем в контекстном менеджере


# В этой функции описана логика игры. Вам нужно её дополнить. По структуре
# тут всё то же самое, что было в вашем коде раньше.
# Но есть отличие - вместо метода display() используется
# новая функция draw_figures().
def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()

    # В цикле обрабатываются такие события, как
    # нажатие кнопок мыши и закрытие окна.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                # Сюда нужно дописать код:
                # если ячейка свободна,
                if game.board[clicked_row][clicked_col] == ' ':
                    # то сделать ход,
                    game.make_move(clicked_row, clicked_col, current_player)

                    # проверить на победу,
                    if game.check_win(current_player):
                        print(f'Вы победили {current_player}!')
                        res = dt.strftime(dt.now(), "%m/%d/%Y %H:%M:%S")
                        save_result(f'Победили {current_player} {res}')
                        running = False
                    # проверить на ничью,
                    elif game.is_board_full():
                        print('Ничья!')
                        res = dt.strftime(dt.now(), "%m/%d/%Y %H:%M:%S")
                        save_result(f'Ничья! {res}')
                        running = False

                    # сменить игрока.
                    current_player = 'O' if current_player == 'X' else 'X'

                    draw_figures(game.board)  # рисуем фигуры на доске

        # Обновить окно игры.
        pygame.display.update()

    # Деинициализирует все модули pygame, которые были инициализированы ранее.
    pygame.quit()


# def main_old():  # Старое исполнение с отрисовкой в терминале

#     game = Board()  # Создать игровое поле - объект класса Board.
#     current_player = 'X'  # Первыми ходят крестики
#     running = True  # Флаг продолжения игры. По умолчанию True
#     game.display()  # Отрисовать поле в терминале.

#     while running:
#         print(f'Ход делают {current_player}')
#         while True:
#             try:
#                 # Тут пользователь вводит координаты ячейки.
#                 # input дает str ==> преобразуем в int
#                 row = int(input('Введите номер строки: '))

#                 if row < 0 or row >= game.field_size:
#                     raise FieldIndexError
#                 column = int(input('Введите номер столбца: '))
#                 if column < 0 or column >= game.field_size:
#                     raise FieldIndexError
#                 if game.board[row][column] != ' ':
#                     # Вот тут выбрасывается новое исключение.
#                     raise CellOccupiedError
#             except FieldIndexError:
#                 print(
#                     'Значение должно быть неотрицательным и меньше '
#                     f'{game.field_size}.'
#                 )
#                 print('Пожалуйста, введите значения для строки и столбца '
#                       'заново.')
#                 # ...и цикл начинает свою работу сначала,
#                 # предоставляя пользователю ещё одну попытку ввести данные.
#                 continue
#             except CellOccupiedError:
#                 print('Ячейка занята')
#                 print('Введите другие координаты.')
#                 continue
#             except ValueError:
#                 print('Буквы вводить нельзя. Только числа.')
#                 print('Пожалуйста, введите значения для строки и столбца '
#                       'заново.')
#                 continue
#             except Exception as e:
#                 print(f'Возникла ошибка: {e}')
#             else:  # Если в блоке try исключения не возникло...
#                 break

#         game.make_move(row, column, current_player)  # Сделать ход
#         print('Ход сделан!')
#         game.display()  # Перерисовать поле с учётом сделанного хода.

#         if game.check_win(current_player):
#             print(f'Вы победили {current_player}!')
#             save_result(f'Победили {current_player}')
#             running = False
#         if game.is_board_full():
#             print('Ничья!')
#             save_result('Ничья!')
#             running = False

#         current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()

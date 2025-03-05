# Из модуля inspect импортировать функцию getsource.

from inspect import getsource

from gameparts import Board


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Отрисовать поле в терминале.
    game.display()
    # Разместить на поле символ по указанным координатам - сделать ход.
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()


def test_intro():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # print(type(game)) 
    # print(game.__class__)
    # print(dir(game))
    # print('__str__' in dir(game))
    # print(hasattr(game, '__str__'))
    print(game.__str__())
    # print(game.__class__.__dict__)
    # print(getsource(Board)) 
    print(Board.__doc__)


if __name__ == '__main__':
    # main()
    test_intro()

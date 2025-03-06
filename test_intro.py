'''Модуль для тестирования интроспекции на примере проекта Крестики-нолики'''

from inspect import getsource
from gameparts import Board


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
    print(getsource(Board))
    print(Board.__doc__)


if __name__ == '__main__':
    test_intro()

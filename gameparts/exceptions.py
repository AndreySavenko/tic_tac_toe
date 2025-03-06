# gameparts/exceptions.py

class FieldIndexError(IndexError):  # Имя класса придумывает разработчик,
    # но оно должно заканчиваться словом `Error.`

    def __str__(self):
        return 'Введено значение за границами игрового поля'


class CellOccupiedError(IndexError):  # Имя класса придумывает разработчик,
    # но оно должно заканчиваться словом `Error.`

    def __str__(self):
        return 'Это поле уже занято'

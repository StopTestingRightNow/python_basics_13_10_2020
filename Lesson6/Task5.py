"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print('Запуск отрисовки карандашем.')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print('Запуск отрисовки маркером.')


PenInstance = Pen()
PenInstance.draw()
PencilInstance = Pencil()
PencilInstance.draw()
HandleInstance = Handle()
HandleInstance.draw()

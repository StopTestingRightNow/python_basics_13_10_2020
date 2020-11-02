"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    colour = 'red'
    colours_dic = [('red', 'yellow', 'green'), (7, 2, 5)]

    def running(self):
        print(self.colour)
        time.sleep(self.colours_dic[1][self.colours_dic[0].index(self.colour)])
        self.colour = self.colours_dic[0][((self.colours_dic[0].index(self.colour)) + 1) % 3]


TrafficLightInstance = TrafficLight()
correct_sequence = ('red', 'yellow', 'green')
curr_index = correct_sequence.index(TrafficLightInstance.colour)

while True:
    TrafficLightInstance.running()
    if (correct_sequence.index(TrafficLightInstance.colour) - curr_index) % 3 == 1:
        curr_index = correct_sequence.index(TrafficLightInstance.colour)
    else:
        print("Wrong colour sequence")
        break


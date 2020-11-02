"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int = 0
    color: str = ''
    name: str = ''
    is_police: bool = False
    
    def go(self):
        self.speed += 30
        
    def stop(self):
        self.speed = 0
        
    def turn(self, direction):
        print(f'{self.name} goes {direction}')
        
    def show_speed(self):
        print(self.speed)
        

class TownCar(Car):
    name = 'Town Car'
        
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed limit exceeded')
    
    
class SportCar(Car):
    name = 'Sport Car'
    
    
class WorkCar(Car):
    name = 'Work Car'
        
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed limit exceeded')
    
    
class PoliceCar(Car):
    name = 'Police Car'
    is_police: bool = True


TownCarInstance = TownCar()
TownCarInstance.color = 'Mauve'
print(TownCarInstance.color)
TownCarInstance.go()
TownCarInstance.show_speed()
TownCarInstance.turn('NORTH')
TownCarInstance.speed += 60
TownCarInstance.show_speed()


WorkCarInstance = WorkCar()
WorkCarInstance.color = 'Yellow'
print(WorkCarInstance.color)
WorkCarInstance.go()
WorkCarInstance.show_speed()
WorkCarInstance.turn('NORTH')
WorkCarInstance.speed += 60
WorkCarInstance.show_speed()

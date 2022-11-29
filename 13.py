#13_1-2
class Animal():
    name = ""
    def __init__(self, newName):
        self.name = newName

    def eat(self):
        print('NumNum')

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def makeNoise(self):
        print(f'{self.name} говорит Гррр')

    def __init__(self):
        print('Родилось животное.')



class Cat(Animal):

    def __init__(self):
        print('Родился кот')

    def meow(self):
        print(f'Кошка {self.name} говорит мяу')



class Dog(Animal):

    def makeNoise(self):
        print(f'{self.name} говорит гав')

    def __init__(self):
        print('Родилась собака')



obj = Animal()
obj.name = 'Rich'
obj.makeNoise()
obj.eat()
print('====')
obj1 = Cat()
obj1.name = 'КОТЭЙКА'
obj1.meow()
obj1.eat()
print('====')
obj2 = Dog()
obj2.name = 'СОБАКЕН'
obj2.makeNoise()
obj2.eat()

13_3
class StringVar():
    text = ""

    def __init__(self, newText):
        self.text = newText

    def set(self, newText):
        self.text = newText
        print('Ошибка исправлена')

    def get(self):
        return self.text

myString = StringVar("Эх 7 числа на пары :(")

print(myString.get())
print("АААА в ПН выходной :) Поменяйте дату!")
myString.set(input("Вводите дату!\n"))
print(myString.get())



#13_4
class Point():
    pos_x = 0
    pos_y = 0

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def show_pos(self):
        print(f'(x = {self.pos_x} ; y = {self.pos_y})')

    def del_pos(self):
        self.pos_x = 0
        self.pos_y = 0

    def setPosX(self, x):
        self.pos_x = x

    def setPosY(self, y):
        self.pos_y = y

    def setPoint(self, x, y):
        self.pos_x = x
        self.pos_y = y


newPoint = Point(1, 1)
newPoint.show_pos()
newPoint.del_pos()
newPoint.show_pos()
newPoint.setPosX(10)
newPoint.show_pos()
newPoint.setPosY(10)
newPoint.show_pos()
newPoint.setPoint(-1, -1)
newPoint.show_pos()

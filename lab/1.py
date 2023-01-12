from tkinter import *
from random import randint

root = Tk()
background = Canvas(root, width=900, height=600, bg='#e6e6fa')
background.pack()


class Drop:
    def __init__(self, background, x, y, yspeed, length):
        self.x = x                                       #задаем всем каплям случайное местоположение по ширине
        self.y = y                                       #чтобы неровно падали задать случайное местоположение за пределами экрана
        self.yspeed = yspeed                             #скорость падения
        self.length = length                             #длина полос дождя
        self.background = background
        self.color = "#8a2be2"
        self.w=900                                       #длина
        self.h=600                                       #высота
        self.line = background.create_line(self.x, self.y, self.x, self.y+length, fill=self.color)

    def move(self):
        self.y += self.yspeed
        self.background.move(self.line, 0, self.yspeed)#падает сверху


        if self.y > self.h: #если у больше высоты то возвращаем назад=>бесконечный дождь
            self.background.move(self.line, 0, -(self.h+self.length))
            self.y -= self.h + self.length


def move_drops():
    for drop in drops:
        drop.move()

    root.after(10, move_drops)

drops = [Drop(background, x=randint(0, 900), y=randint(0, 700),
                  yspeed=randint(1, 15), length=randint(5, 25)) for i in range(400)]#массив где 400 элементов

move_drops()
root.mainloop()
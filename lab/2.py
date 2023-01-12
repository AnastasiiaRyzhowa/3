from tkinter import *


root = Tk()
width = 600
height = 600
bg = Canvas(root, width=600, height=600, bg="white")
bg.pack()
bg.create_rectangle(0, height//2, width, height, fill='#75bbfd')


class Ball:

    def __init__(self, c, x1, y1, x2, y2, radius, mass, color="white"):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.radius = radius
        self.c = c
        self.resistance = radius*0.2
        self.v = 5
        self.F_str = 0.03 * self.v * radius
        self.mass = mass
        self.Acceleration = (self.F_str / mass) * 50#ускорение
        self.ball = c.create_oval(self.x1 - self.radius, self.y1 - self.radius, self.x2 +
                                  self.radius, self.y2 + self.radius, fill=color)
        
    #движение частиц

    def move_ball(self):
        if bg.coords(self.ball)[3] < height//2:
            bg.move(self.ball, 0, self.v)
            bg.after(1000//60, self.move_ball)
        elif height//2 <= bg.coords(self.ball)[3] + self.F_str < height:
            bg.move(self.ball, 0, self.F_str)
            bg.after(1000//60, self.move_ball)
        else:
            bg.move(self.ball, 0, height + 1 - bg.coords(self.ball)[3])
            bg.after(1000//60, self.iter_1)

    def iter_1(self):
        if bg.coords(self.ball)[3] - self.Acceleration >= height - self.mass*0.2:
            bg.move(self.ball, 0, -self.Acceleration)
            bg.after(1000//60, self.iter_1)
        elif bg.coords(self.ball)[3] <= height:
            bg.after(1000//60, self.iter_2)

    def iter_2(self):
        if bg.coords(self.ball)[3] + self.Acceleration < height:
            bg.move(self.ball, 0, self.Acceleration)
            bg.after(1000//60, self.iter_2)
        else:
            bg.move(self.ball, 0, height + 1 - bg.coords(self.ball)[3])
            bg.after(1000//60, self.iter_3)

    def iter_3(self):
        if bg.coords(self.ball)[3] - self.Acceleration >= height - self.mass*0.1:
            bg.move(self.ball, 0, -self.Acceleration)
            bg.after(1000//60, self.iter_3)
        else:
            bg.after(1000//60, self.iter_stop)

    def iter_stop(self):
        if bg.coords(self.ball)[3] + self.Acceleration < height:
            bg.move(self.ball, 0, self.Acceleration)
            bg.after(1000//60, self.iter_stop)

        else:
            bg.move(self.ball, 0, height + 1 - bg.coords(self.ball)[3])# Конечная координата частицы равна height + 1


def esc(event):
    root.destroy()


r2 = 25
mass2 = 50
ball2 = Ball(bg, 200, 20, 200,
             20, r2, mass2, color="#463C52")
ball2.move_ball()

r1 =60
mass1 = 110
ball1 = Ball(bg, 100, 20, 100,
             20, r1, mass1, color="#8B776D")
ball1.move_ball()

r3 = 30
mass3 = 60
ball3 = Ball(bg, 300, 30, 300,
             20, r3, mass3, color="#9D94BA")
ball3.move_ball()

r6 = 15
mass6 = 35
ball6 = Ball(bg, 570, 20, 570,
             20, r6, mass6, color="#44426E")
ball6.move_ball() 

r4 = 36
mass4 = 75
ball4 = Ball(bg, 300, 20, 300,
             20, r4, mass4, color="#BEC4E1")
ball4.move_ball()

r5 = 15
mass5 = 10
ball5 = Ball(bg, 50, 40, 50,
             40, r5, mass5, color="#D1D5E8")
ball5.move_ball()

r5 = 35
mass5 = 10
ball5 = Ball(bg, 60, 40, 60,
             40, r5, mass5, color="#D1D5E5")
ball5.move_ball()





root.mainloop()
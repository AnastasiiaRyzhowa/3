from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("445x455")

#Кнопки
b1=Button(root,text=" ",font=('mono', 20, 'bold'), width=8, height=4, bg="SystemButtonFace",command=lambda: button_implement(b1))
b2=Button(root,text=" ",font=('mono', 20, 'bold'), width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b2))
b3=Button(root,text=" ",font=('mono', 20, 'bold'), width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b3))

b4=Button(root,text=" ",font=('mono', 20, 'bold'),width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b4))
b5=Button(root,text=" ",font=('mono', 20, 'bold'),width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b5))
b6=Button(root,text=" ",font=('mono', 20, 'bold'),width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b6))

b7=Button(root,text=" ",font=('mono', 20, 'bold'),width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b7))
b8=Button(root,text=" ",font=('mono', 20, 'bold'),width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b8))
b9=Button(root,text=" ",font=('mono', 20, 'bold'),width=8, height=4,bg="SystemButtonFace",command=lambda: button_implement(b9))


b1.grid(row=0,column=0)#клетка
b2.grid(row=0,column=1)
b3.grid (row=0,column=2)

b4.grid (row=1,column=0)
b5.grid (row=1,column=1)
b6.grid (row=1,column=2)

b7.grid (row=2,column=0)
b8.grid (row=2,column=1)
b9.grid (row=2,column=2)


def data():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked=True
    count=0


def button_status():    #отключает кнопки
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def search_winner():    #варианты выйгрыей
    global winner
    winner=False

    #победитель по x

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] =="X":
        b1.config(bg="#E23E57")
        b2.config(bg="#E23E57")
        b3.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] =="X":
        b4.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b6.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] =="X":
        b7.config(bg="#E23E57")
        b8.config(bg="#E23E57")
        b9.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] =="X":
        b1.config(bg="#E23E57")
        b4.config(bg="#E23E57")
        b7.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] =="X":
        b2.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b8.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] =="X":
        b3.config(bg="#E23E57")
        b6.config(bg="#E23E57")
        b9.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] =="X":
        b1.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b9.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] =="X":
        b3.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b7.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил X! Игра завершина!")
        button_status()

     #Проверяем О на выйгрыщ
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] =="O":
        b1.config(bg="#E23E57")
        b2.config(bg="#E23E57")
        b3.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] =="O":
        b4.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b6.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] =="O":
        b7.config(bg="#E23E57")
        b8.config(bg="#E23E57")
        b9.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] =="O":
        b1.config(bg="#E23E57")
        b4.config(bg="#E23E57")
        b7.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] =="O":
        b2.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b8.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] =="O":
        b3.config(bg="#E23E57")
        b6.config(bg="#E23E57")
        b9.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] =="O":
        b1.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b9.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] =="O":
        b3.config(bg="#E23E57")
        b5.config(bg="#E23E57")
        b7.config(bg="#E23E57")
        winner=True
        messagebox.showinfo("Победил О! Игра завершина!")
        button_status()


def button_implement(b):
    global clicked,count

    if b["text"] ==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        search_winner()

    elif b["text"] ==" " and clicked==False:
        b["text"]="O"
        clicked=True
        count+=1
        search_winner()


data()
root.mainloop ()
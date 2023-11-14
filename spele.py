from tkinter import*
from tkinter import messagebox
manslogs = Tk()
manslogs.title("TicTacToe")

def btnClick(button):
    global speletajsX, count
    if button["text"]==""and speletajsX==True:
        button["text"]="X"
        speletajsX=False
        count+=1
    

btn1= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn2= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn3= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn4= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn5= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn6= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn7= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn8= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn9= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))
btn10= Button(manslogs, text = " ", width = 6, height = 3, font = ("Helvica, 24"))

btn1.grid(row=0, column = 0)
btn2.grid(row=0, column = 1)
btn3.grid(row=0, column = 2)
btn4.grid(row=1, column = 0)
btn5.grid(row=1, column = 1)
btn6.grid(row=1, column = 2)
btn7.grid(row=2, column = 0)
btn8.grid(row=2, column = 1)
btn9.grid(row=2, column = 2)

manslogs.mainloop()



























manslogs.mainloop()
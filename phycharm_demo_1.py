from tkinter import *

class MyWindow:
    def __init__(self):
        self.window = Tk()
        self.lbl = Label(self.window,text="Simple calculator")
        self.lbl.place(x=75,y=75)

        self.lbl1 = Label(self.window,text="Number 1:",fg="blue")
        self.lbl1.place(x=80,y=100)
        self.num1_var = StringVar()
        self.txt1 = Entry(self.window, textvariable=self.num1_var, bd=3)
        self.txt1.place(x=150,y=100)

        self.lbl2 = Label(self.window, text="Number 2:", fg="orange")
        self.lbl2.place(x=80,y=150)
        self.num2_var = StringVar()
        self.txt2 = Entry(self.window, textvariable=self.num2_var, bd=3)
        self.txt2.place(x=150,y=150)

        self.btn1 = Button(self.window,text="Add",command=self.add)
        self.btn1.place(x=80,y=200)

        self.btn2 = Button(self.window,text="Subtract",command=self.sub)
        self.btn2.place(x=150,y=200)

        self.btn3 = Button(self.window,text="Multiply",command=self.mul)
        self.btn3.place(x=220,y=200)

        self.btn4 = Button(self.window,text="Divide",command=self.div)
        self.btn4.place(x=300,y=200)

        self.txt3 = Entry(self.window,text="This is an entry widget")
        self.txt3.place(x=100,y=250)

        self.window.geometry("500x400+10+20")
        self.window.title("Python project")
        self.window.mainloop()

    def add(self):
        self.txt3.delete(0,'end')
        num1 = int(self.num1_var.get())
        num2 = int(self.num2_var.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def sub(self):
        self.txt3.delete(0,'end')
        num1 = int(self.num1_var.get())
        num2 = int(self.num2_var.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def mul(self):
        self.txt3.delete(0,'end')
        num1 = int(self.num1_var.get())
        num2 = int(self.num2_var.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def div(self):
        self.txt3.delete(0,'end')
        num1 = int(self.num1_var.get())
        num2 = int(self.num2_var.get())
        if num2 != 0:
            result = num1 / num2
            self.txt3.insert(END, str(result))
        else:
            self.txt3.insert(END, "Error: Division by zero")

my_window = MyWindow()

import tkinter as tk
import math
import numpy
from tkinter.constants import E, END, SUNKEN, W

c = ""

class Calculator:
    def __init__(self) -> None:
        self.last_answer = 0

        self.root = tk.Tk()
        self.root.title("projectCalcula")
        self.root.resizable(0,0)
        self.e = tk.Entry(self.root, width=40, borderwidth=5, font=("CALIBRI",20), justify="right")
        self.e.grid(row=0, column=0,columnspan=5, padx=10, pady=50)
        self.label = tk.Label(self.root, text = "projectCalcula", bd=1, relief=SUNKEN, font="italic").grid(row=8, column=0, columnspan=7, sticky=W+E)

        self.bsin = tk.Button(self.root, text="sin", padx=20, pady=5, command=lambda:[self.button_click("sin("),self.duplicate("sin(")], bg = "light gray").grid(row=1,column=0,pady=5,padx=1)
        self.bcos = tk.Button(self.root, text="cos", padx=20, pady=5, command=lambda:[self.button_click("cos("),self.duplicate("cos(")],bg = "light gray").grid(row=1,column=1,pady=5)
        self.btan = tk.Button(self.root, text="tan", padx=20, pady=5, command=lambda:[self.button_click("tan("),self.duplicate("tan(")],bg = "light gray").grid(row=1,column=2,pady=5)
        self.blog = tk.Button(self.root, text="log", padx=21, pady=5, command=lambda:[self.button_click("log("),self.duplicate("log10(")],bg = "light gray").grid(row=1,column=3,pady=5)
        self.bleft = tk.Button(self.root, text="(", padx=28, pady=5, command=lambda:[self.button_click("("),self.duplicate("(")],bg = "light gray").grid(row=3,column=3,pady=5)
        self.bright = tk.Button(self.root, text=")", padx=28, pady=5,command=lambda:[self.button_click(")"),self.duplicate(")")],bg = "light gray").grid(row=3,column=4,pady=5)
        self.bsqrt = tk.Button(self.root, text="√", padx=25, pady=5, command=lambda:[self.button_click("√("),self.duplicate("sqrt(")],bg = "light gray").grid(row=3,column=2,pady=5)

        self.basin = tk.Button(self.root, text="asin", padx=17, pady=5, command=lambda:[self.button_click("arcsin("),self.duplicate("asin(")],bg = "light gray").grid(row=2,column=0,pady=5)
        self.bacos = tk.Button(self.root, text="acos", padx=17, pady=5, command=lambda:[self.button_click("arccos("),self.duplicate("acos(")],bg = "light gray").grid(row=2,column=1,pady=5)
        self.batan = tk.Button(self.root, text="atan", padx=17, pady=5, command=lambda:[self.button_click("arctan("),self.duplicate("atan(")],bg = "light gray").grid(row=2,column=2,pady=5)
        self.bln = tk.Button(self.root, text=" ln", padx=23, pady=5, command=lambda:[self.button_click("ln("),self.duplicate("ln(")],bg = "light gray").grid(row=1,column=4,pady=5)
        self.bpi = tk.Button(self.root, text="π", command=lambda:[self.button_click("pi"),self.duplicate(3.14)], padx=26, pady=5,bg = "light gray").grid(row=2,column=3,pady=5)
        self.bfac = tk.Button(self.root, text="!", command=lambda:[self.button_click("fact("),self.duplicate("fact(")], padx=27, pady=5,bg = "light gray").grid(row=2,column=4,pady=5)
        self.bsqr = tk.Button(self.root, text="x²", command=lambda:[self.button_click("^2"),self.duplicate("^2")], padx=24, pady=5,bg = "light gray").grid(row=3,column=1,pady=5)
        self.bcube = tk.Button(self.root, text="x³", command=lambda:[self.button_click("^3"),self.duplicate("^3")], padx=24, pady=5,bg = "light gray").grid(row=3,column=0,pady=5)

        self.bans = tk.Button(self.root, text="ANS",command=lambda:[self.button_click("ANS"),self.duplicate(self.last_answer)], padx=18, pady=10,bg = "light gray").grid(row=7,column=3,pady=5)
 

        self.b1 =tk.Button(self.root, text="1", padx=25, pady=10, command=lambda:[self.button_click(1),self.duplicate(1)],bg = "light gray").grid(row=6,column=0,pady=5)
        self.b2 =tk.Button(self.root, text="2", padx=25, pady=10, command=lambda:[self.button_click(2),self.duplicate(2)],bg = "light gray").grid(row=6,column=1,pady=5)
        self.b3 =tk.Button(self.root, text="3", padx=25, pady=10, command=lambda:[self.button_click(3),self.duplicate(3)],bg = "light gray").grid(row=6,column=2,pady=5)

        self.b4 =tk.Button(self.root, text="4", padx=25, pady=10, command=lambda:[self.button_click(4),self.duplicate(4)],bg = "light gray").grid(row=5,column=0,pady=5)
        self.b5 =tk.Button(self.root, text="5", padx=25, pady=10, command=lambda:[self.button_click(5),self.duplicate(5)],bg = "light gray").grid(row=5,column=1,pady=5)
        self.b6 =tk.Button(self.root, text="6", padx=25, pady=10, command=lambda:[self.button_click(6),self.duplicate(6)],bg = "light gray").grid(row=5,column=2,pady=5)

        self.b7 =tk.Button(self.root, text="7", padx=25, pady=10, command=lambda:[self.button_click(7),self.duplicate(7)],bg = "light gray").grid(row=4,column=0,pady=5)
        self.b8 =tk.Button(self.root, text="8", padx=25, pady=10, command=lambda:[self.button_click(8),self.duplicate(8)],bg = "light gray").grid(row=4,column=1,pady=5)
        self.b9 =tk.Button(self.root, text="9", padx=25, pady=10, command=lambda:[self.button_click(9),self.duplicate(9)],bg = "light gray").grid(row=4,column=2,pady=5)

        self.b0 =tk.Button(self.root, text="0", padx=82, pady=10, command=lambda:[self.button_click(0),self.duplicate(0)],bg = "light gray").grid(row=7,column=0,columnspan=2, pady=5,)
        self.bdeci =tk.Button(self.root, text=". ", padx=25, pady=10, command=lambda:[self.button_click("."),self.duplicate(".")],bg = "light gray").grid(row=7,column=2,pady=5)

        self.badd =tk.Button(self.root, text=" +", padx=24, pady=10, command=lambda:[self.button_click("+"),self.duplicate("+")],bg = "light gray").grid(row=6,column=3,pady=5)
        self.bminus =tk.Button(self.root, text="- ", padx=26, pady=10, command=lambda:[self.button_click("-"),self.duplicate("-")],bg = "light gray").grid(row=6,column=4,pady=5)
        self.btimes =tk.Button(self.root, text="x", padx=27, pady=10, command=lambda:[self.button_click("x"),self.duplicate("*")],bg = "light gray").grid(row=5,column=3,pady=5)
        self.bdivide =tk.Button(self.root, text=" ÷ ", padx=22, pady=10, command=lambda:[self.button_click("÷"),self.duplicate("/")],bg = "light gray").grid(row=5,column=4,pady=5)

        self.bdel =tk.Button(self.root, text="DEL", padx=20, pady=10, command=self.delete, bg = "orange", fg= "black").grid(row=4,column=3,pady=5)
        self.bclear =tk.Button(self.root, text="AC", padx=22, pady=10, command=self.ac,bg = "orange", fg= "black").grid(row=4,column=4,pady=5)
        self.bequal =tk.Button(self.root, text="=", padx=26, pady=10, command=self.evaluate, bg = "yellow").grid(row=7,column=4,pady=5)
        
		self.root.bind('<Return>', self.evaluate)

	def button_click(self,num):
		dis = self.e.get()
		x = self.e.index(INSERT)
		self.e.insert(x,str(num)) 

    def ac(self):
        pass

	def delete(self):
		global c
		c = list(self.e.get())
		x = self.e.index(INSERT) - 1
		self.e.delete(x, x+1)
        
    def duplicate(self,num):
        global c
        c = c+str(num)

    def evaluate(self):
        pass

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc =Calculator()
    calc.run()     

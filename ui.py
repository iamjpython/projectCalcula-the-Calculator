import tkinter as tk
from tkinter.constants import E, END, SUNKEN, W
from tkinter import *
import webbrowser
import tkinter.messagebox as message
from calculator import solve

c =  []

class Calculator:
	def __init__(self) -> None:

		self.last_answer = 0

		self.root = tk.Tk()
		self.root.title("projectCalcula")
		self.root.resizable(0,0)
		self.root.config(bg="#00061e")
		self.e = tk.Entry(self.root, width=50, borderwidth=5, font=60, justify="right")
		self.e.grid(row=0, column=0,columnspan=5, padx=10, pady=50)
		self.label = tk.Label(self.root, text = "projectCalcula - the Calculator", bd=1, relief=SUNKEN, font=("Palatino",16,"bold"), bg="#036a7d", fg="#00061e").grid(row=8, column=0, columnspan=7, sticky=W+E)

		self.menuinfo = tk.Menu(self.root)
		self.m1 = tk.Menu(self.menuinfo, tearoff=0)
		self.m1.add_command(label="Github Website", command=self.website)
		self.m1.add_command(label="Group Info", command=self.info)

		self.m2 = tk.Menu(self.menuinfo, tearoff=0)
		self.m2.add_command(label="Calculator Operation", command=self.operation)
		self.m2.add_command(label="Errors", command=self.error)

			
		self.root.config(menu=self.menuinfo)
		self.menuinfo.add_cascade(label="About Us", menu=self.m1)
		self.menuinfo.add_cascade(label="Instructions", menu=self.m2)


		self.bsin = tk.Button(self.root, text="sin", padx=22, pady=5, command=lambda:self.button_click("sin("), bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=1,column=0,pady=5)
		self.bcos = tk.Button(self.root, text="cos", padx=21, pady=5, command=lambda:self.button_click("cos("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=1,column=1,pady=5)
		self.btan = tk.Button(self.root, text="tan", padx=20, pady=5, command=lambda:self.button_click("tan("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=1,column=2,pady=5)
		self.blog = tk.Button(self.root, text="log", padx=22, pady=5, command=lambda:self.button_click("log("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=1,column=3,pady=5)
		self.bleft = tk.Button(self.root, text="(", padx=28, pady=5, command=lambda:self.button_click("("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=3,column=3,pady=5)
		self.bright = tk.Button(self.root, text=")", padx=28, pady=5,command=lambda:self.button_click(")"),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=3,column=4,pady=5)
		self.bsqrt = tk.Button(self.root, text="√", padx=25, pady=5, command=lambda:self.button_click("sqrt("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=3,column=2,pady=5)

		self.basin = tk.Button(self.root, text="asin", padx=18, pady=5, command=lambda:self.button_click("arcsin("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=2,column=0,pady=5)
		self.bacos = tk.Button(self.root, text="acos", padx=17, pady=5, command=lambda:self.button_click("arccos("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=2,column=1,pady=5)
		self.batan = tk.Button(self.root, text="atan", padx=17, pady=5, command=lambda:self.button_click("arctan("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=2,column=2,pady=5)
		self.bln = tk.Button(self.root, text=" ln", padx=23, pady=5, command=lambda:self.button_click("ln("),bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=1,column=4,pady=5)
		self.bpi = tk.Button(self.root, text="π", command=lambda:self.button_click("pi"), padx=26, pady=5,bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=2,column=3,pady=5)
		self.bfac = tk.Button(self.root, text="!", command=lambda:self.button_click("fact("), padx=29, pady=5,bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=2,column=4,pady=5)
		self.bsqr = tk.Button(self.root, text="x²", command=lambda:self.button_click("^2"), padx=25, pady=5,bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=3,column=1,pady=5)
		self.bcube = tk.Button(self.root, text="x³", command=lambda:self.button_click("^3"), padx=24, pady=5,bg = "#49b5d1", bd=3, font=("Tahoma",10,"bold")).grid(row=3,column=0,pady=5)

		self.bans = tk.Button(self.root, text="ANS",command=lambda:self.button_click(self.last_answer), padx=18, pady=10,bg = "#ffde59", bd=3, font=("Tahoma",10,"bold")).grid(row=7,column=3,pady=5)
 

		self.b1 =tk.Button(self.root, text="1", padx=21, pady=10, command=lambda:self.button_click(1),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=6,column=0,pady=5)
		self.b2 =tk.Button(self.root, text="2", padx=21, pady=10, command=lambda:self.button_click(2),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=6,column=1,pady=5)
		self.b3 =tk.Button(self.root, text="3", padx=21, pady=10, command=lambda:self.button_click(3),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=6,column=2,pady=5)

		self.b4 =tk.Button(self.root, text="4", padx=21, pady=10, command=lambda:self.button_click(4),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=5,column=0,pady=5)
		self.b5 =tk.Button(self.root, text="5", padx=21, pady=10, command=lambda:self.button_click(5),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=5,column=1,pady=5)
		self.b6 =tk.Button(self.root, text="6", padx=21, pady=10, command=lambda:self.button_click(6),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=5,column=2,pady=5)

		self.b7 =tk.Button(self.root, text="7", padx=21, pady=10, command=lambda:self.button_click(7),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=4,column=0,pady=5)
		self.b8 =tk.Button(self.root, text="8", padx=21, pady=10, command=lambda:self.button_click(8),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=4,column=1,pady=5)
		self.b9 =tk.Button(self.root, text="9", padx=21, pady=10, command=lambda:self.button_click(9),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=4,column=2,pady=5)

		self.b0 =tk.Button(self.root, text="0", padx=70, pady=10, command=lambda:self.button_click(0),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=7,column=0,columnspan=2, pady=5)
		self.bdeci =tk.Button(self.root, text=". ", padx=21, pady=10, command=lambda:self.button_click("."),bg = "#ffffff", bd=3, font=("Tahoma",10,"bold")).grid(row=7,column=2,pady=5)

		self.badd =tk.Button(self.root, text=" +", padx=24, pady=10, command=lambda:self.button_click("+"),bg = "#ffde59", bd=3, font=("Tahoma",10,"bold")).grid(row=6,column=3,pady=5)
		self.bminus =tk.Button(self.root, text="- ", padx=26, pady=10, command=lambda:self.button_click("-"),bg = "#ffde59", bd=3, font=("Tahoma",10,"bold")).grid(row=6,column=4,pady=5)
		self.btimes =tk.Button(self.root, text="x", padx=28, pady=10, command=lambda:self.button_click("*"),bg = "#ffde59", bd=3, font=("Tahoma",10,"bold")).grid(row=5,column=3,pady=5)
		self.bdivide =tk.Button(self.root, text=" ÷ ", padx=22, pady=10, command=lambda:self.button_click("/"),bg = "#ffde59", bd=3, font=("Tahoma",10,"bold")).grid(row=5,column=4,pady=5)

		self.bdel =tk.Button(self.root, text="DEL", padx=20, pady=10, command=self.delete, bg = "#ff5757", bd=3, font=("Tahoma",10,"bold")).grid(row=4,column=3,pady=5)
		self.bclear =tk.Button(self.root, text="AC", padx=22, pady=10, command=self.ac,bg = "#ff5757", bd=3, font=("Tahoma",10,"bold")).grid(row=4,column=4,pady=5)
		self.bequal =tk.Button(self.root, text="=", padx=25, pady=10, command=self.evaluate, bg = "#ffde59", bd=3, font=("Tahoma",10,"bold")).grid(row=7,column=4,pady=5)
		
		self.root.bind('<Return>', self.evaluate)

	def button_click(self,num):
		x = self.e.index(INSERT)
		self.e.insert(x,str(num))
		global c
		c = list(self.e.get()) 
		
	def ac(self):
		global c
		c = []
		self.e.delete(0,END)

	def delete(self):
		global c
		c = list(self.e.get())
		x = self.e.index(INSERT) - 1
		self.e.delete(x, x+1)
	
	def evaluate(self, event = None):
		global c
		c = ''.join(c)

		try:
			ans = solve(str(c))
		except (ZeroDivisionError, ValueError):
			ans = "MATH ERROR"
		except SyntaxError:
			ans = "SYNTAX ERROR"
		if type(ans) == float or type(ans) == int:
			self.last_answer = ans
		else:
			self.last_answer = self.last_answer
		ans = str(ans)

		self.e.delete(0, END)
		self.e.insert(0, ans)
		
	def website(self):
		webbrowser.open("https://github.com/iamjpython/projectCalcula-the-Calculator")
		
	def info(self):
		webbrowser.open("https://drive.google.com/file/d/130NINMu1o3pBUFLFn8aitAGaoUzv137i/view?fbclid=IwAR3YquwVuGA3S4n9B4LYTCo7zxYJb2A39rmwGDtgm2_7znGW9WI3WotXEVM")
	
	def operation(self):
		return message.showinfo("HOW TO USE CALCULATOR","\t\tprojectCalcula \n\n\nEnclose all parenthesis. \n\nCalculator functions uses radians.\n\nlog function is in base 10.\n\nAlways place an integer before the decimal. eg. 0.1 , sin(0.5)")
		
	def error(self):
		return message.showwarning("LIST OF ERRORS","\t      projectCalcula \n\n\n Math Error - can't be calculated mathematically. \n\n Syntax Error - input numbers or characters are invalid.")

	def run(self):
		self.root.mainloop()


if __name__ == "__main__":
	calc =Calculator()
	calc.run()

import tkinter as tk
import math
from tkinter.constants import E, END, SUNKEN, W
import webbrowser
import tkinter.messagebox as message
class Calculator:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("projectCalcula")
        self.root.resizable(0,0)
        self.e = tk.Entry(self.root, width=50, borderwidth=5, font=60, justify="right")
        self.e.grid(row=0, column=0,columnspan=5, padx=10, pady=50)
        self.label = tk.Label(self.root, text = "projectCalcula", bd=1, relief=SUNKEN, font="italic").grid(row=8, column=0, columnspan=7, sticky=W+E)

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


        self.bsin = tk.Button(self.root, text="sin", padx=20, pady=5,bg = "light gray")
        self.bcos = tk.Button(self.root, text="cos", padx=20, pady=5,bg = "light gray")
        self.btan = tk.Button(self.root, text="tan", padx=20, pady=5,bg = "light gray")
        self.blog = tk.Button(self.root, text="log", padx=21, pady=5,bg = "light gray")
        self.bleft = tk.Button(self.root, text="(", padx=28, pady=5,bg = "light gray", command=lambda:self.button_click("("))
        self.bright = tk.Button(self.root, text=")", padx=28, pady=5,bg = "light gray", command=lambda:self.button_click(")"))
        self.bsqrt = tk.Button(self.root, text="√", padx=25, pady=5,bg = "light gray")

        self.basin = tk.Button(self.root, text="asin", padx=17, pady=5,bg = "light gray")
        self.bacos = tk.Button(self.root, text="acos", padx=17, pady=5,bg = "light gray")
        self.batan = tk.Button(self.root, text="atan", padx=17, pady=5,bg = "light gray")
        self.bln = tk.Button(self.root, text=" ln", padx=23, pady=5,bg = "light gray")
        self.bpi = tk.Button(self.root, text="π", padx=26, pady=5,bg = "light gray")
        self.bfac = tk.Button(self.root, text="!", padx=27, pady=5,bg = "light gray")
        self.bsqr = tk.Button(self.root, text="x²", padx=24, pady=5,bg = "light gray")
        self.bcube = tk.Button(self.root, text="x³", padx=24, pady=5,bg = "light gray")

        self.bans = tk.Button(self.root, text="ANS",command=lambda:self.button_click(self.last_answer), padx=18, pady=10,bg = "light gray")
 
 
        self.bsin.bind("<Button-1>",self.sccalc)
        self.bsin.grid(row=1,column=0,pady=5)

        self.bcos.bind("<Button-1>",self.sccalc)
        self.bcos.grid(row=1,column=1,pady=5)

        self.btan.bind("<Button-1>",self.sccalc)
        self.btan.grid(row=1,column=2,pady=5)

        self.blog.bind("<Button-1>",self.sccalc)
        self.blog.grid(row=1,column=3,pady=5)

        self.bln.bind("<Button-1>",self.sccalc)
        self.bln.grid(row=1,column=4,pady=5)

        self.basin.bind("<Button-1>",self.sccalc)
        self.basin.grid(row=2,column=0,pady=5)

        self.bacos.bind("<Button-1>",self.sccalc)
        self.bacos.grid(row=2,column=1,pady=5)

        self.batan.bind("<Button-1>",self.sccalc)
        self.batan.grid(row=2,column=2,pady=5)

        self.bpi.bind("<Button-1>",self.sccalc)
        self.bpi.grid(row=2,column=3,pady=5)

        self.bfac.bind("<Button-1>",self.sccalc)
        self.bfac.grid(row=2,column=4,pady=5)

        self.bcube.bind("<Button-1>",self.sccalc)
        self.bcube.grid(row=3,column=0,pady=5)

        self.bsqr.bind("<Button-1>",self.sccalc)
        self.bsqr.grid(row=3,column=1,pady=5)

        self.bsqrt.bind("<Button-1>",self.sccalc)
        self.bsqrt.grid(row=3,column=2,pady=5)

        
        self.bleft.grid(row=3,column=3,pady=5)
        self.bright.grid(row=3,column=4,pady=5)
        

        self.bans.grid(row=7,column=3,pady=5)


        self.b1 =tk.Button(self.root, text="1", padx=25, pady=10, command=lambda:self.button_click(1),bg = "light gray").grid(row=6,column=0,pady=5)
        self.b2 =tk.Button(self.root, text="2", padx=25, pady=10, command=lambda:self.button_click(2),bg = "light gray").grid(row=6,column=1,pady=5)
        self.b3 =tk.Button(self.root, text="3", padx=25, pady=10, command=lambda:self.button_click(3),bg = "light gray").grid(row=6,column=2,pady=5)

        self.b4 =tk.Button(self.root, text="4", padx=25, pady=10, command=lambda:self.button_click(4),bg = "light gray").grid(row=5,column=0,pady=5)
        self.b5 =tk.Button(self.root, text="5", padx=25, pady=10, command=lambda:self.button_click(5),bg = "light gray").grid(row=5,column=1,pady=5)
        self.b6 =tk.Button(self.root, text="6", padx=25, pady=10, command=lambda:self.button_click(6),bg = "light gray").grid(row=5,column=2,pady=5)

        self.b7 =tk.Button(self.root, text="7", padx=25, pady=10, command=lambda:self.button_click(7),bg = "light gray").grid(row=4,column=0,pady=5)
        self.b8 =tk.Button(self.root, text="8", padx=25, pady=10, command=lambda:self.button_click(8),bg = "light gray").grid(row=4,column=1,pady=5)
        self.b9 =tk.Button(self.root, text="9", padx=25, pady=10, command=lambda:self.button_click(9),bg = "light gray").grid(row=4,column=2,pady=5)

        self.b0 =tk.Button(self.root, text="0", padx=72, pady=10, command=lambda:self.button_click(0),bg = "light gray").grid(row=7,column=0,columnspan=2, pady=5,)
        self.bdeci =tk.Button(self.root, text=". ", padx=25, pady=10, command=lambda:self.button_click("."),bg = "light gray").grid(row=7,column=2,pady=5)

        self.badd =tk.Button(self.root, text=" +", padx=24, pady=10, command=lambda:self.button_click("+"),bg = "light gray").grid(row=6,column=3,pady=5)
        self.bminus =tk.Button(self.root, text="- ", padx=26, pady=10, command=lambda:self.button_click("-"),bg = "light gray").grid(row=6,column=4,pady=5)
        self.btimes =tk.Button(self.root, text="x", padx=27, pady=10, command=lambda:self.button_click("*"),bg = "light gray").grid(row=5,column=3,pady=5)
        self.bdivide =tk.Button(self.root, text=" ÷ ", padx=22, pady=10, command=lambda:self.button_click("/"),bg = "light gray").grid(row=5,column=4,pady=5)

        self.bdel =tk.Button(self.root, text="DEL", padx=20, pady=10, command=self.delete, bg = "orange", fg= "black").grid(row=4,column=3,pady=5)
        self.bclear =tk.Button(self.root, text="AC", padx=22, pady=10, command=self.ac,bg = "orange", fg= "black").grid(row=4,column=4,pady=5)
        self.bequal =tk.Button(self.root, text="=", padx=26, pady=10, command=self.evaluate, bg = "yellow").grid(row=7,column=4,pady=5)

        self.last_answer = 0
     
    def button_click(self,num):
        dis = self.e.get()
        self.e.delete(0,END)
        self.e.insert(0,str(dis)+str(num)) 

    def ac(self):
        pass

    def delete(self):
        pass

    def evaluate(self):
        pass
            
    def sccalc(self,event):
        button = event.widget
        text = button["text"]
        try:
            num = float(self.e.get())
            if text == "sin":
                try:
                    input = num
                    ans = math.sin(input)
                except ValueError:
                    ans = "Syntax Error"

            elif text == "cos":
                try:
                    input = num
                    ans = math.cos(input)
                except ValueError:
                    ans ="Syntax Error"

            elif text == "tan":
                try:
                    input = num
                    ans = math.tan(input)
                except ValueError:
                    ans = "Syntax Error"

            elif text == "asin":
                try:
                    input = num
                    ans = math.asin(input)
                except ValueError:
                    ans = "Math Error"
                    
            elif text == "acos":
                try:
                    input = num
                    ans = math.acos(input)
                except ValueError:
                    ans = "Math Error"

            elif text == "atan":
                try:
                    input = num
                    ans = math.atan(input)
                except ValueError:
                    ans = "Math Error"
            
            elif text == " ln":
                try:
                    input = num
                    ans = math.log10(input)
                except ValueError:
                    ans = "Math Error"
                
            elif text == "log":
                try:
                    input = num
                    ans = math.log10(input)
                except ValueError:
                    ans = "Math Error"
            
            elif text == "!":
                try:
                    input = num
                    ans = math.factorial(input)
                except ValueError:
                    ans = "Math Error"
            
            elif text == "x²":
                try:
                    input = num
                    ans = math.pow(input, 2)
                except ValueError:
                    ans = "Syntax Error"

            elif text == "x³":
                try:
                    input = num
                    ans = math.pow(input, 3)
                except ValueError:
                    ans = "Syntax Error"

            elif text == "√":
                try:
                    input = num
                    ans = math.sqrt(input)
                except ValueError:
                    ans = "Math Error"

            elif text == "π":
                input = num
                ans = math.pi*input

        except ValueError:
            ans = "Input number (in radians) then function"

        if type(ans) == int:
            self.last_answer = ans
        else:
            self.last_answer = self.last_answer 
            
        self.e.delete(0, END)
        self.e.insert(END, ans)



    def website(self):
        webbrowser.open("https://github.com/iamjpython/projectCalcula-the-Calculator")
        
    def info(self):
        webbrowser.open("https://drive.google.com/file/d/1m-p92ps5IbUV6MtZ4-oiJv_hxQ-D0cKd/view?usp=sharing")
    
    def operation(self):
        return message.showinfo("HOW TO USE CALCULATOR","\t\t   projectCALCULA \n \n \n Leading zeroes results to error.\n When using trigometric functions - input number then click button. \n Calculator functions uses radians.\n log function is in base 10.")
        
    def error(self):
        return message.showwarning("LIST OF ERRORS","\t\t   project Calcula \n \n \n Input Errors - remove leading zeroes \n\t      math operations must be separated by numbers\n\n Math Error - can't be calculated, change number\n\n Syntax Error - input numbers characters incorrect \n\n Input number then function - enter number then function button \t\t\t                don't use parenthesis")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc =Calculator()
    calc.run()

from tkinter import *
root = Tk()
root.title("Calculator")

entry = Entry(root, width=45, borderwidth=5, font=60)
entry.grid(row=0, column=0,columnspan=5, padx=10, pady=30)

b1 = Button(root, text="1", padx=40, pady=10, command=lambda:button_click(1)).grid(row=3,column=2)
b2 = Button(root, text="2", padx=40, pady=10, command=lambda:button_click(2)).grid(row=3,column=1)
b3 = Button(root, text="3", padx=40, pady=10, command=lambda:button_click(3)).grid(row=3,column=0)

b4 = Button(root, text="4", padx=40, pady=10, command=lambda:button_click(4)).grid(row=2,column=2)
b5 = Button(root, text="5", padx=40, pady=10, command=lambda:button_click(5)).grid(row=2,column=1)
b6 = Button(root, text="6", padx=40, pady=10, command=lambda:button_click(6)).grid(row=2,column=0)

b7 = Button(root, text="7", padx=40, pady=10, command=lambda:button_click(7)).grid(row=1,column=2)
b8 = Button(root, text="8", padx=40, pady=10, command=lambda:button_click(8)).grid(row=1,column=1)
b9 = Button(root, text="9", padx=40, pady=10, command=lambda:button_click(9)).grid(row=1,column=0)

b0 = Button(root, text="0", padx=91, pady=10, command=lambda:button_click(0)).grid(row=4,column=0, columnspan=2)
bdeci = Button(root, text=".", padx=42, pady=10, command=lambda:button_click(0)).grid(row=4,column=2)

badd = Button(root, text="+ ", padx=42, pady=10, command=lambda:button_click("+")).grid(row=1,column=3)
bminus = Button(root, text="-", padx=45, pady=10, command=lambda:button_click("-")).grid(row=2,column=3)
btimes = Button(root, text="x", padx=45, pady=10, command=lambda:button_click("*")).grid(row=3,column=3)
bdivide = Button(root, text="  % ", padx=38, pady=10, command=lambda:button_click("/")).grid(row=4,column=3)

bdel = Button(root, text=" DEL ", padx=31, pady=10, command=lambda:button_click("del")).grid(row=1,column=4)
bclear = Button(root, text="AC", padx=36, pady=10, command=lambda:button_click("ac")).grid(row=2,column=4)
bequal = Button(root, text="=", padx=40, pady=33, command=lambda:button_click("=")).grid(row=3,column=4, rowspan=2)

root.mainloop()

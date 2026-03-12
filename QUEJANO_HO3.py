import tkinter as gela 

window = gela.Tk()
window.geometry("240x200")
window.resizable(True,True)
window.configure(bg="lightblue",cursor="arrow")

label = gela.Label(window, text = "CALCULATOR", bg = "lightblue")
label.grid(column = 0, row = 0, columnspan = 5)

num_1 = gela.Label(window, text = "Enter first number:")
num_1.grid(column = 0, row = 1, columnspan = 2, pady=5)

num_label = gela.Entry(window)
num_label.grid(column = 2, row = 1, columnspan = 1, pady=5, padx=5)

num_2 = gela.Label(window, text = "Enter 2nd number:")
num_2.grid(column = 0, row = 2, columnspan = 2, pady=5)

num_label2 = gela.Entry(window)
num_label2.grid(column = 2, row = 2, columnspan = 1, pady=5, padx=5)

def add():
    n1 = num_label.get()
    n2 = num_label2.get()
    result = int(n1) + int(n2)
    label.config(text = f"The sum of {n1} + {n2} is {result}")
    
def subtract():
    n1 = num_label.get()
    n2 = num_label2.get()
    result = int(n1) - int(n2) 
    label.config(text = f"The difference of {n1} - {n2} is {result}")

def multiply():
    n1 = num_label.get()
    n2 = num_label2.get()
    result = int(n1) * int(n2)
    label.config(text = f"The product of {n1} * {n2} is {result}")
def division():
    n1 = num_label.get()
    n2 = num_label2.get()
    result = int(n1) / int(n2)
    label.config(text = f"The quotient of {n1} / {n2} is {result}")

btn_add = gela.Button(window, text = "Add", command = add, relief = "sunken")
btn_add.grid(column = 1, row = 3, columnspan = 1)

btn_sub = gela.Button(window, text = "Subtract", command = subtract, relief = "sunken")
btn_sub.grid(column = 2, row = 3, columnspan = 1)

btn_mul = gela.Button(window, text = "Multiply", command = multiply, relief = "sunken")
btn_mul.grid(column = 1, row = 4, columnspan = 1)

btn_div = gela.Button(window, text = "Division", command = division, relief = "sunken")
btn_div.grid(column = 2, row =4, columnspan = 1)

window.mainloop()
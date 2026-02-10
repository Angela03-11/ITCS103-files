import tkinter as gela 

window = gela.Tk()

window.title("Angela's Profile")

window.geometry("600x600")

window.resizable(True, True)

window.configure(bg="skyblue", cursor="arrow")

card = gela.Frame(window, bg="white", padx=5, pady=20)
card.pack(pady=40)

label = gela.Label(card, text="♡Gelatin's Profile♡", font=("Bookman Old Style","30","bold"), bg="skyblue", anchor="center")
label.pack(padx=5, pady=20)

label = gela.Label(card, text="Name: Angela Nicole B. Quejano", font=("Times New Roman","15"), bg="skyblue")
label.pack(anchor="w", pady=10)

label = gela.Label(card, text="Age: 18", font=("Times New Roman","15"), bg="skyblue")
label.pack(anchor="w", pady=10)

label = gela.Label(card, text="Course: BSIT", font=("Times New Roman","15"), bg="skyblue")
label.pack(anchor="w", pady=10)

label = gela.Label(card, text="Birthday: March 11, 2007", font=("Times New Roman","15"), bg="skyblue")
label.pack(anchor="w", pady=10)

label = gela.Label(card, text="Motto: ", font=("Times New Roman","15"), bg="skyblue")
label.pack(anchor="w", pady=10)

label = gela.Label(card, text="♡Walang plan B kasi plan A pa lang nakakapagod na.(≧◡≦)♡", font=("Comic Sans MS","15","italic"), bg="skyblue")
label.pack(anchor="center", pady=10)

window.mainloop()
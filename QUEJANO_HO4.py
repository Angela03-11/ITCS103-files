import tkinter as gela 

window = gela.Tk()

window.title("Profile Builder")
window.geometry("550x250")
window.resizable(False, False)
window.configure(bg = "lightyellow", cursor = "heart")

# frame = gela.Frame(window)
# frame.place(x = 0, y = 0)

keme = gela.Toplevel(window)

label = gela.Label(window, text = "Profile Builder", bg = "lightyellow", font=("Poppins", 15, "bold"))
label.place(x = 220, y = 10)

fname_ent = gela.Entry(window)
fname_ent.place(x = 50, y = 60)

mname = gela.Entry(window)
mname.place(x = 220, y = 60)

lname = gela.Entry(window)
lname.place(x = 380, y = 60)

byear = gela.Entry(window)
byear.place(x = 50, y = 130)

f_label = gela.Label(window, text = "First Name", bg = "lightyellow", font =("Arial", 10, "italic"))
f_label.place(x = 75, y = 90)

m_label = gela.Label(window, text = "Middle Name", bg = "lightyellow", font =("Arial", 10, "italic"))
m_label.place(x = 240 , y = 90)

l_label = gela.Label(window, text = "Last Name", bg = "lightyellow", font =("Arial", 10, "italic"))
l_label.place(x = 405, y = 90)

b_label = gela.Label(window, text = "Birth Year", bg = "lightyellow", font =("Arial", 10, "italic"))
b_label.place(x = 75, y = 160)

age = gela.Label(window, text = "Computing Age...", bg = "lightyellow", font = ("Poppins", 15, "italic"))
age.place(x = 270, y = 130)

gender = gela.Label(window, text = "Gender", bg = "lightyellow", font = ("Arial", 10, "italic"))
gender.place(x = 80, y = 190)


def click():
    female == 1
    label.configure(text = "You are a Female")

    male == 0
    label.configure(text = "You are a Male")
    
    age = byear.get()

gender = gela.IntVar(window)
female = gela.Radiobutton(text = "Female", bg = "lightyellow", variable = gender, value = 1)
female.place(x = 230, y = 190)

male = gela.Radiobutton(text = "Male", bg = "lightyellow", variable = gender, value = 0)
male.place(x = 300, y = 190)


btn = gela.Button(window, text = "Submit", bg = "lightyellow", relief = "sunken", activebackground = "red", activeforeground = "white")
btn.place(x = 250, y = 215)

window.mainloop()
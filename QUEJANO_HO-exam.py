import tkinter as gela

window = gela.Tk()
window.title("Quejano_HO-exam")
window.geometry("400x200")
window.resizable(False, False)
window.configure(bg = "lightblue", cursor = "heart")

toplabel = gela.Label(window, text = "Welcome!", bg = "lightblue", font = ("Poppins", 20, "bold"))
toplabel.place(x = 140, y = 15)

def register():
    if btn:
        keme = gela.Toplevel(window)
        keme.geometry("250x200")
        keme.configure(bg = "lightblue", cursor = "heart")
    
        reg_uname = gela.Label(keme, text ="Username:", bg = "lightblue", font = ("Poppins", 10))
        reg_uname.place(x = 5, y = 20)

        reg_pass = gela.Label(keme, text = "Password:", bg = "lightblue", font = ("Poppins", 10))
        reg_pass.place(x = 5, y = 60)

        reg_ent = gela.Entry(keme)
        reg_ent.place(x = 80 ,y = 20)

        reg_ent2 = gela.Entry(keme)
        reg_ent2.place(x = 80 ,y = 60)

        pass_btn = gela.IntVar()
        pass_btn = gela.Checkbutton(keme, text = "See Password", variable = pass_btn, bg = "lightblue", font = ("Poppins", 10))
        pass_btn.place(x = 100 ,y = 90)

        regs_btn = gela.Button(keme, text = "Register", bg = "lightblue", font = ("Poppins", 15, "bold"))
        regs_btn.place(x = 75, y = 130) 

    btn.bind("<Return>", register)

def login():
    if btn_log:
        keme2 = gela.Toplevel(window)
        keme2.geometry("250x200")
        keme2.configure(bg = "lightblue", cursor = "heart")
    
        log_uname = gela.Label(keme2, text ="Username:", bg = "lightblue", font = ("Poppins", 10))
        log_uname.place(x = 5, y = 20)

        log_pass = gela.Label(keme2, text = "Password:", bg = "lightblue", font = ("Poppins", 10))
        log_pass.place(x = 5, y = 60)

        log_ent = gela.Entry(keme2)
        log_ent.place(x = 80 ,y = 20)

        log_ent = gela.Entry(keme2)
        log_ent.place(x = 80 ,y = 60)

        pass_btn2 = gela.IntVar()
        pass_btn2 = gela.Checkbutton(keme2, text = "See Password", variable = pass_btn2, bg = "lightblue", font = ("Poppins", 10))
        pass_btn2.place(x = 100 ,y = 90)

        log_btn = gela.Button(keme2, text = "Login", bg = "lightblue", font = ("Poppins", 15, "bold"))
        log_btn.place(x = 75, y = 130) 

    btn_log.bind("<Return>", login)


btn = gela.Button(window, text = "REGISTER", bg = "blue", command = register, relief = "solid", font = ("Poppins", 20, "bold"))
btn.place(x = 125, y = 60)

btn_log = gela.Button(window, text = "LOGIN", bg = "green", relief = "solid", font = ("Poppins", 20, "bold"))
btn_log.place(x = 150, y = 120)




window.mainloop()
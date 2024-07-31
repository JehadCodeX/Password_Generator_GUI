from tkinter import *
import random


def copy_password():
    window.clipboard_clear()

    window.clipboard_append(password_display_label.cget("text"))


def update_password_length(value):
    password_length_display_label.config(text=f"Password Length: {value}")


def generate():
    characters = []
    if lower_letter.get() == 1:
        characters.extend(Lower_Case_Letter)
    if upper_letter.get() == 1:
        characters.extend(Upper_Case_Letter)
    if num_var.get() == 1:
        characters.extend(Numbers)
    if symbol_var.get() == 1:
        characters.extend(S_C)
    password_length = password_length_scale.get()

    if not characters or password_length == 0:
        generate_v = "Select options and length"
    else:
        generate_v = ''.join(random.choice(characters) for _ in range(password_length))

    password_display_label.config(text=generate_v)


Upper_Case_Letter = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z",
                     "X", "C", "V", "B", "N", "M"]
Lower_Case_Letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]
Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
S_C = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "'", "\"",
       ",", ".", "<", ">", "/", "?", "\\", "|", "`", "~"]

window = Tk()
lower_letter = IntVar()
upper_letter = IntVar()
num_var = IntVar()
symbol_var = IntVar()

window.geometry("600x400")
window.config(background="#E0F7FA")

password_display_label = Label(window, text="                              ", font=("arial", 30, "bold"), fg="#004D40",
                               bg="#00796B", relief=SUNKEN, bd=10)
password_length_scale = Scale(window, from_=0, to=50, orient=HORIZONTAL, length=300, showvalue=0, fg="#004D40",
                              bg="#00796B", troughcolor="#004D40", command=update_password_length)
LowerCase_button = Checkbutton(window, text="Lower Case", onvalue=1, offvalue=0, variable=lower_letter, indicatoron=0,
                               bg="#E0F7FA", fg="#004D40", selectcolor="#00796B")
UpperCase_button = Checkbutton(window, text="Upper Case", onvalue=1, offvalue=0, variable=upper_letter, indicatoron=0,
                               bg="#E0F7FA", fg="#004D40", selectcolor="#00796B")
num_button = Checkbutton(window, text="Numbers", onvalue=1, offvalue=0, variable=num_var, indicatoron=0, bg="#E0F7FA",
                         fg="#004D40", selectcolor="#00796B")
symbol_button = Checkbutton(window, text="Symbols", onvalue=1, offvalue=0, variable=symbol_var, indicatoron=0,
                            bg="#E0F7FA", fg="#004D40", selectcolor="#00796B")
generate_button = Button(window, text="Generate", bg="#E0F7FA", fg="#004D40", command=generate)
password_length_display_label = Label(window, text="Password_Length: 0", bg="#E0F7FA", fg="#004D40")
copy_button = Button(window, text="Copy", bg="#E0F7FA", fg="#004D40", command=copy_password)

password_display_label.pack(pady=10)
copy_button.pack(pady=10)
password_length_scale.pack(pady=10)
password_length_display_label.pack(pady=5)
LowerCase_button.pack(pady=5)
UpperCase_button.pack(pady=5)
num_button.pack(pady=5)
symbol_button.pack(pady=5)
generate_button.pack(pady=10)

window.mainloop()

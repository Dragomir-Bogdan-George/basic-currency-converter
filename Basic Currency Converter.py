import tkinter
from tkinter import *

starting_currency = ""
final_currency = ""
output_money = 0


def from_ron():
    global starting_currency
    starting_currency = "RON"

    text_box_button_from.delete(1.0, END)
    text_box_button_from.insert(INSERT, "From RON")


def from_euro():
    global starting_currency
    starting_currency = "EURO"

    text_box_button_from.delete(1.0, END)
    text_box_button_from.insert(INSERT, "From EURO")


def from_usd():
    global starting_currency
    starting_currency = "USD"

    text_box_button_from.delete(1.0, END)
    text_box_button_from.insert(INSERT, "From USD")


def to_ron():
    global final_currency
    final_currency = "RON"

    text_box_button_to.delete(1.0, END)
    text_box_button_to.insert(INSERT, "To RON")


def to_euro():
    global final_currency
    final_currency = "EURO"

    text_box_button_to.delete(1.0, END)
    text_box_button_to.insert(INSERT, "To EURO")


def to_usd():
    global final_currency
    final_currency = "USD"

    text_box_button_to.delete(1.0, END)
    text_box_button_to.insert(INSERT, "To USD")


def show_text_label():
    global output_money

    conversion_label.pack()
    conversion_final_value.pack(pady=17)
    input_money = currency_text_box.get()
    conversion_final_value.delete(1.0, END)

    if starting_currency == "RON" and final_currency == "RON":
        output_money = input_money
    elif starting_currency == "RON" and final_currency == "EURO":
        output_money = float(input_money) / 4.8734
    elif starting_currency == "RON" and final_currency == "USD":
        output_money = float(input_money) / 4.8739

    if starting_currency == "EURO" and final_currency == "EURO":
        output_money = input_money
    elif starting_currency == "EURO" and final_currency == "RON":
        output_money = float(input_money) * 4.8734
    elif starting_currency == "EURO" and final_currency == "USD":
        output_money = float(input_money) * 0.9999

    if starting_currency == "USD" and final_currency == "USD":
        output_money = input_money
    elif starting_currency == "USD" and final_currency == "RON":
        output_money = float(input_money) * 4.8739
    elif starting_currency == "USD" and final_currency == "EURO":
        output_money = float(input_money) * 1.00344

    conversion_final_value.tag_configure("text_center", justify="center")
    conversion_final_value.insert(INSERT, input_money + " " + starting_currency + " = " + str(output_money) + " " +
                                  final_currency)
    conversion_final_value.tag_add("text_center", 1.0, "end")


window_space = Tk()
window_space.geometry("890x650+500+200")
window_space.title("Currency Convertor")
window_space.config(bg="#808080")
window_space.resizable(width=False, height=False)
window_space.iconphoto(False, tkinter.PhotoImage(file="dollar_image_icon.png"))

frame = Frame(window_space, width=860, height=620)
frame.place(x=14, y=10)

label_currency_from = Label(frame, text="Select the currency to convert from", font=("Courier", 30))
label_currency_from.pack()
frame.pack_propagate(False)

ron_button_from = Button(
    frame,
    text="RON",
    font=("Courier", 30),
    bg="#00FF00",
    padx=10,
    pady=5,
    width=5,
    command=from_ron

)
ron_button_from.place(x=5, y=50)

euro_button_from = Button(
    frame,
    text="EURO",
    font=("Courier", 30),
    bg="#C5B4E3",
    padx=10,
    pady=5,
    width=5,
    command=from_euro
)
euro_button_from.place(x=360, y=50)

usd_button_from = Button(
    frame,
    text="USD",
    font=("Courier", 30),
    bg="#add8e6",
    padx=10,
    pady=5,
    width=5,
    command=from_usd
)
usd_button_from.place(x=707, y=50)

label_currency_to = Label(frame, text="Select the currency to convert to", font=("Courier", 30))
label_currency_to.pack(pady=100)

ron_button_to = Button(
    frame,
    text="RON",
    font=("Courier", 30),
    bg="#00FF00",
    padx=10,
    pady=5,
    width=5,
    command=to_ron
)
ron_button_to.place(x=5, y=200)

euro_button_to = Button(
    frame,
    text="EURO",
    font=("Courier", 30),
    bg="#C5B4E3",
    padx=10,
    pady=5,
    width=5,
    command=to_euro
)
euro_button_to.place(x=360, y=200)

usd_button_to = Button(
    frame,
    text="USD",
    font=("Courier", 30),
    bg="#add8e6",
    padx=10,
    pady=5,
    width=5,
    command=to_usd
)
usd_button_to.place(x=707, y=200)

label_currency_value = Label(frame, text="Introduce the amount of money", font=("Courier", 30))
label_currency_value.pack()

currency_text_box = Entry(
    frame,
    font=("Courier", 20),
    bg="#ffcccb"
)
currency_text_box.pack()

convert_button = Button(
    frame,
    text="Convert",
    font=("Courier", 20),
    bg="#FFFFE0",
    command=show_text_label
)
convert_button.pack()

text_box_button_from = Text(frame, width=20, height=1, bg="#fed8b1")
text_box_button_from.pack(side=LEFT)

text_box_button_to = Text(frame, width=20, height=1, bg="#fed8b1")
text_box_button_to.pack(side=RIGHT)

label_value = Label(frame, text="The conversion is", font=("Courier", 30))

conversion_label = Label(frame, text="The conversion is", font=("Courier", 30))
conversion_final_value = Text(frame, width=40, height=3, bg="#D3D3D3", font=("Courier", 15))

window_space.mainloop()

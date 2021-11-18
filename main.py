from tkinter import *
import pandas
import random

# read dict from csv
to_learn = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")

current_card = None

def get_random_dict():
    return random.choice(to_learn)

def next_card():
    global  current_card
    current_card = get_random_dict()
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

# print(get_random_dict())
# print(get_random_dict())

BACKGROUND_COLOR = "#B1DDC6"

# create the ui
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")

canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command =next_card)
known_button.grid(row=1, column=1)
next_card()
window.mainloop()

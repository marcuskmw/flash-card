from tkinter import *
import pandas
import random

# read dict from csv
to_learn = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")

current_card = None
flip_timer= None
# current_image = None
BACKGROUND_COLOR = "#B1DDC6"
TIME_WAIT = 3000


def get_random_dict():
    return random.choice(to_learn)


def next_card():
    global current_card
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = get_random_dict()
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer= window.after(TIME_WAIT, flip)
    # flip_card()


# def show_frech_card():
#     canvas.itemconfig(card_title, text="French")
#     canvas.itemconfig(card_word, text=current_card["French"])


def flip():
    # global current_card  // why no need to set global here???
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# create the ui
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

current_image = card_front_img
canvas_image = canvas.create_image(400, 263, image=current_image)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                        command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
known_button.grid(row=1, column=1)
next_card()

window.mainloop()

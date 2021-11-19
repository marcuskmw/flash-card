import tkinter.messagebox
from tkinter import *
import pandas
import random

PROGRESS_FILE_PATH = "./data/words_to_learn.csv"
DATA_FILE_PATH = "./data/french_words.csv"
BACKGROUND_COLOR = "#B1DDC6"

to_learn = None

current_card = None
flip_timer = None
TIME_WAIT = 3000


def load_data():
    global to_learn
    try:
        # load previous progress
        to_learn = pandas.read_csv(PROGRESS_FILE_PATH).to_dict(orient="records")
    except (FileNotFoundError, pandas.errors.EmptyDataError) as e:
        # load the flash data
        to_learn = pandas.read_csv(DATA_FILE_PATH).to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    if len(to_learn) == 0:
        print("no more card")
        tkinter.messagebox.showinfo(title="Congratulation", message = "You have learn all the word!  We will reset "
                                                                      "the database for the full set of data")
        load_data()
        next_card()
    else:
        current_card = random.choice(to_learn)
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        flip_timer = window.after(TIME_WAIT, flip)

def on_known_button_click():
    # remove card from the list
    to_learn.remove(current_card)

    # save to csv
    pandas.DataFrame.from_dict(to_learn).to_csv(PROGRESS_FILE_PATH, index=False)
    next_card()  # flip to next card


def on_unknown_button_click():
    next_card()  # flip to next card


def flip():
    # global current_card  // why no need to set global here???
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


load_data()
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
                        command=on_unknown_button_click)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=on_known_button_click)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

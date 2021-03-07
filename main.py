from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------ GENERATE WORD -----------------------------------------#
data = pandas.read_csv('data/german_words.csv')
data_dict = data.to_dict(orient='records')
random_word = {}


def generate_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)

    random_word = random.choice(data_dict)
    german_word = random_word['German']
    english_word = random_word['English']
    try:
        with open("data/known_words.txt", "r") as known_words_file:
            list_of_words = known_words_file.readlines()
            while english_word in list_of_words:
                random_word = random.choice(data_dict)
                german_word = random_word['German']

    except FileNotFoundError:
        f = open("data/known_words.txt", "w")
        f.close()
    else:
        canvas.itemconfig(lang, text='German', fill="black")
        canvas.itemconfig(word, text=german_word, fill="black")
        canvas.itemconfig(canvas_front, image=front_image)
        flip_timer = window.after(3000, flip_card)


def is_known():
    global random_word
    english_word = random_word['English']
    with open("data/known_words.txt", "a") as known_words_file:
        known_words_file.write(english_word + "\n")
    generate_word()

# --------------------------------- FLIP THE CARD --------------------------------------#


def flip_card():
    global random_word
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=random_word['English'], fill="white")
    canvas.itemconfig(canvas_front, image=back_image)


# ----------------------------------- UI SETUP -----------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
canvas_front = canvas.create_image(400, 263, image=front_image)

# language
lang = canvas.create_text(400, 150, text="Welcome to", font=("Times New Roman", 40, "italic"))

# word
word = canvas.create_text(400, 263, text="Flashy", font=("Times New Roman", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# wrong_button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

# right_button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# to show the random word as soon as we open the app
# comment it to see the default placeholders
generate_word()

window.mainloop()

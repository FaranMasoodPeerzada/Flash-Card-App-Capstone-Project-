from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

current_card={}
to_learn={}
try:
    data= pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
def is_known():
    to_learn.remove(current_card)
    data= pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(card_title,text="French", fill='black')
    canvas.itemconfig(card_word,text=current_card['French'], fill='black')
    flip_timer=window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(card_background, image=card_back )

    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')



window= Tk()
window.title('Flashy')
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card )

canvas= Canvas(width=800, height=526)
card_front=PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150, text="title", font=('Ariel',40,'italic'))
card_word=canvas.create_text(400,263, text="word", font=('Ariel',50,'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)

#Buttons
cross_image=PhotoImage(file="wrong.png")
unknown_button=Button(image=cross_image, highlightthickness=0, command=next_card)
#unknown_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)
unknown_button.grid(column=0,row=1)


tick_image=PhotoImage(file="right.png")
known_button=Button(image=tick_image, highlightthickness=0, command=is_known)
#unknown_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)
known_button.grid(column=1,row=1)
next_card()

# Reading data file





window.mainloop()

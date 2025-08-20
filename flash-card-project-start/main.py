import csv
from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
active_pair = ()
task_id = None
#----------------------------------------------DATA----------------------------------------#
try:
    with open("./words_saved.csv",mode="r",newline='') as file:
        csv_reader = csv.reader(file)
        word_list = [tuple(row) for row in csv_reader]
except FileNotFoundError:
    data_frame = pandas.read_csv("./data/french_words.csv")
    word_list = [(value.French, value.English) for (key, value) in data_frame.iterrows()]


print(word_list)
print(len(word_list))

#----------------------------------------------CANCEL_SCHEDULED_TASK-----------------------#

def cancel_task():
    global task_id
    if task_id:
        window.after_cancel(task_id)

#----------------------------------------------NEW CARD -----------------------------------#

def new_card():
    global card_image, active_pair,task_id
    cancel_task()
    card_image = PhotoImage(file="./images/card_front.png")
    canvas.itemconfig(card_img,image=card_image)
    canvas.itemconfig(card_title,text="French",fill="black")
    word_pair = random.choice(word_list)
    active_pair = word_pair
    canvas.itemconfig(card_word,text=f"{word_pair[0]}",fill="black")
    task_id = window.after(3000,flip_card,word_pair[1])




#----------------------------------------------FLIP CARD ----------------------------------#

def flip_card(english_word):
    global card_image
    card_image = PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(card_img,image=card_image)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=english_word,fill="white")

#----------------------------------------------SAVE WORDS ------------------------------

def save():
    print(active_pair)
    french_word = active_pair[0]
    english_word = active_pair[1]
    word_list.remove(active_pair)
    print(word_list)
    print(len(word_list))
    new_row = (french_word,english_word)
    with open("./words_saved.csv","a",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row)


#---------------------------------------------COMBINED FUNCTION-------------------------
def combined_function():
    save()
    new_card()


#----------------------------------------------UI -----------------------------------------#

window = Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#Canvas card front UI
canvas= Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="./images/card_front.png")
card_img = canvas.create_image(400,263,image = card_image)
card_title = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"),fill="black")
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"),fill="black")
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")

#Defining Buttons and labels
wrong = Button(image=wrong_image, highlightthickness=0,command=new_card)
right = Button(image=right_image,highlightthickness=0,command=combined_function)

#Tkinter layout
canvas.grid(row=0,column=0,columnspan=2)
wrong.grid(row=1,column=0)
right.grid(row=1,column=1)

new_card()

window.mainloop()
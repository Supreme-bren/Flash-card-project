from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

#----------------------------------------------DATA----------------------------------------#
data_frame = pandas.read_csv("./data/french_words.csv")
word_list  = {key:value for (key,value) in data_frame.iterrows()}
print(data_frame)
print(word_list)


#----------------------------------------------UI -----------------------------------------#
window = Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#Canvas card front UI
canvas= Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263,image = card_image)
canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"),fill="black")
canvas.create_text(400,263,text="touvre",font=("Ariel",60,"bold"),fill="black")
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")

#Defining Buttons and labels
wrong = Button(image=wrong_image, highlightthickness=0)
right = Button(image=right_image,highlightthickness=0)

#Tkinter layout
canvas.grid(row=0,column=0,columnspan=2)
wrong.grid(row=1,column=0)
right.grid(row=1,column=1)


window.mainloop()
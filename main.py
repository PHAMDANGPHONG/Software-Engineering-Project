from tkinter import *
from tkinter import messagebox
from pygame import mixer
from gtts import gTTS
import pandas
import random
import os

# Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_WINDOW_BG_COLOR = "#B1DDC6"
WORD_FONT = ("Ariel", 60, "bold")
LANGUAGE_FONT = ("Ariel", 40, "italic")
SELECT_LANGUAGE_FONT = ("Ariel", 26, "italic", "bold", "underline")
SCORE_FONT = ("Ariel", 20, "italic", "bold",)
LANGUAGES_SELECTION_FONT = ("Ariel", 18, "italic")
FLIP_TIME = 2500  # Milliseconds
BACK_FONT_COLOR = "white"
FRONT_FONT_COLOR = "black"


# File Paths:
#ENGLISH_TO_LEARN = "data/English_to_learn.csv"


FAMILY_IMAGE = "images/"
HUMANBODY_IMANGE = "images/"
PERSONALITY_IMAGE = "images/"
APPEARANCE_IMAGE = "images/"
EMOTIONS_IMAGE = "images/"

front_country_name = "USA"
back_country_name = "VIETNAM"

# Messages:
SELECT_LANGUAGE_TEXT = ""
NO_MORE_CARDS_MESSAGE = ("")
CONTINUE_MESSAGE = ""
CONFIRM_RESET_MESSAGE = ""
CONFIRM_EXIT_MESSAGE = ""

current_card = {}  # Current Card Dictionary

# Starting Audio
mixer.init()
text_to_speech = gTTS(text="Welcome", lang="en", tld="us")
text_to_speech.save("audio/output.mp3")
click = mixer.Sound("audio/mouse_click_effect.wav")
click.set_volume(0.2)


def human_body():
    

def appearance():


def personality():
    

def emotions():


def family():
    



def flip_card():
    """Flip the card and shows the translation passed as input"""
    


def next_card():
    """Generates and shows a new card, then calls the flip_card function after a given time"""
    

def remove_known_word():
    """Remove words that user marks as known from the words_to_learn file"""
    

def reset_data():
    """"Reset the data to the original (full) data set"""
    

def no_more_cards():
    """Reset the data and close window (called when there is only 1 card left)"""
    


def ask_user_continue():
    """Ask the user if they want to continue from the progress of the last session"""
    


def on_closing():
    """"Ask the user if they actually meant to close the app"""
    


# Read data and convert into a dictionary
data = pandas.read_csv(initial_data_path)
to_learn = data.to_dict(orient="records")

# ---------------------- UI Setup ----------------------------- #
root = Tk()
root.title("Flashcard App")
root.config(bg=BACKGROUND_COLOR, padx=40, pady=50)
root.geometry("+300+50")
flip_timer = root.after(FLIP_TIME, func=flip_card)  # Flip timer

# Images
icon = PhotoImage(file="images/icon_png.png")
root.iconphoto(False, icon)
card_front = PhotoImage(file="images/card_front.png")  # Cards
card_back = PhotoImage(file="images/card_back.png")

right_img = PhotoImage(file="images/right.png")  # Right - Wrong Buttons
wrong_img = PhotoImage(file="images/wrong.png")



# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)  # Card Img
word = canvas.create_text(400, 263, text="Word", fill="black", font=WORD_FONT)  # Word Text
language = canvas.create_text(400, 150, text=front_language, font=LANGUAGE_FONT)  # Language Text
pronunciation = canvas.create_text(400, 340, text="/pronunciation/", font=LANGUAGE_FONT)  # IPA Phonetic Transcription
flag = canvas.create_image(150, 100, image=front_card_flag)  # Flag Img
score = canvas.create_text(670, 60, text="", fill="black", font=SCORE_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons:
unknown_button = Button(image=wrong_img, highlightthickness=0, bd=7, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_img, highlightthickness=0, bd=7, command=remove_known_word)
known_button.grid(row=1, column=1)

# Bind the closing button to the function on_closing to ask the user if he wants to exit
root.protocol("WM_DELETE_WINDOW", on_closing)

# Hide the Root Window until the user chooses a language
root.withdraw()

# --------------------- Select Language Window -------------------------- #

language_window.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

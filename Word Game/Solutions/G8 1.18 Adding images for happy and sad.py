
#Task 1: Play the game and try to win one time and lose one time.
#Task 2: Add sad emoji image when the game is lost.

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import random
from pathlib import Path

class Word(toga.App):

    valid_alphabet = set("abcdefghijklmnopqrstuvwxyz") #define a set with all the alphabets
    file_path = "english_words.txt"
    with open(file_path, "r") as file:
        all_words=[line.strip() for line in file]

    title_style1=Pack(text_align="center",font_size=20,font_weight="bold", color="blue")
    title_style2=Pack(text_align="center",font_size=20,font_weight="bold", color="red")

    def startup(self):
        self.secret_word = ""

        label1 = toga.Label("Word Game", style=Word.title_style1)
        button1 = toga.Button("Play Word Game",on_press=self.start_new_game)
        button2 = toga.Button("Start game with own word",on_press=self.enter_own_word)

        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(label1)
        main_box.add(button1)
        main_box.add(button2)

        self.main_window = toga.MainWindow(title="Simple Window")
        self.main_window.content=main_box
        self.main_window.show()


    def get_word(self):
        random_item = random.choice(Word.all_words)
        return random_item

    def start_new_game(self,widget):
        if widget.text == "Play Word Game" or widget.text == "Start a New Game":
            self.secret_word = self.get_word() # get a random word

        print(self.secret_word)

        self.secret_letters = set(self.secret_word.lower())
        self.used_letters = []
        self.lives = 7
        self.correct_letters = set()
        self.revealed_word = ["_"] * len(self.secret_word)
        self.game_state()


    def game_state(self):
        box = toga.Box(style=Pack(direction=COLUMN))

        #heading
        box.add(toga.Label("Guess a Letter!"))
        box.add(toga.Label("Word: " + " ".join(self.revealed_word)))

        #adding a textInput and validating the input
        input_txt = toga.TextInput(on_change=self.process_letter)
        box.add(input_txt)

        # used letters + lives
        box.add(toga.Label("Used Letters: " + " ".join(self.used_letters)))
        box.add(toga.Label("Lives: " + str(self.lives)))

        #buttons
        box.add(toga.Button("Start a New Game", on_press=self.start_new_game))
        box.add(toga.Button("Start game with own word", on_press=self.enter_own_word))

        self.main_window.content = box
        input_txt.focus()

    def process_letter(self, widget): #function to check if only letters are entered
        lowercase = widget.value.lower() #convert all the letters to lowercase
        if lowercase in Word.valid_alphabet: #if it is present in the alphabet list defined by user
            if lowercase in self.secret_letters: #if secrete_letter is in word, replace underscore with letter
                self.correct_letters = self.correct_letters.union(widget.value)
                for i in range(len(self.secret_word)): #iterates through each character in secret word
                    if self.secret_word[i].upper() in self.correct_letters or self.secret_word[i].lower() in self.correct_letters: #checks if a letter is already guessed by user
                        self.revealed_word[i] = self.secret_word[i] #if yes then underscore is replaced with letter

            elif lowercase not in self.used_letters:
                self.lives = self.lives - 1 #decrease lives by 1
                self.used_letters.append(lowercase)  #adding the letter user has enetered
            else:
                print('Already Used, type another letter')

        else:
            print('Not a valid alphabet')

        if self.lives == 0: #check if game is over
            self.end_game(victory=False) #call the function with victory set to false which means user has not won
        elif "_" not in self.revealed_word: #if there is no _
            self.end_game(victory=True) #call the function with vistory set to true
        else:
            self.game_state()


    def end_game(self, victory): #define function to end the game
        box = toga.Box(style=Pack(direction=COLUMN)) #create a new box

        if victory: #if user has won
            box.add(toga.Label("You won! :)", style=Word.title_style1))
            img_path = "happy.png"
        else:
            box.add(toga.Label("You lost! :(", style=Word.title_style2))
            img_path = "sad.png"


        box.add(toga.Label("The word was: " + self.secret_word))
        box.add(toga.Button("Start a New Game", on_press=self.start_new_game))
        box.add(toga.Button("Start game with own word", on_press=self.enter_own_word))
        box.add(toga.ImageView(image=img_path))

        self.main_window.content = box
        self.main_window.show()

    def enter_own_word(self,widget): #define function to allow user to enter the word
        box = toga.Box(style=Pack(direction=COLUMN))
        box.add(toga.Label("Enter your secret word:"))
        input_txt2 = toga.TextInput(placeholder="Enter Your Word Here", on_change=self.update_secret_word_handler)
        box.add(input_txt2)
        box.add(toga.Button("Start Game", on_press=self.start_new_game))
        self.main_window.content = box
        self.main_window.show()
        input_txt2.focus()


    def update_secret_word_handler(self, widget): #define function to update the secret_word
        self.secret_word = widget.value

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()


#Task: Add code in the function get_word to get random word from the list of words

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import random

class Word(toga.App):

    valid_alphabet = set("abcdefghijklmnopqrstuvwxyzABCD") #define a set with all the alphabets
    all_words=["hello", "python", "except", "acquire", "temperature"]
    title_style=Pack(text_align="center",font_size=20,font_weight="bold", color="blue")

    def startup(self):
        label1 = toga.Label("Word Game", style=Word.title_style)
        button1 = toga.Button("Play Word Game",on_press=self.start_new_game)
        button2 = toga.Button("Start game with own word",on_press=self.enter_own_word)

        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(label1)
        main_box.add(button1)
        main_box.add(button2)

        self.main_window = toga.MainWindow(title="Simple Window")
        self.main_window.content=main_box
        self.main_window.show()


    def get_word(self):    #Task: Get a random word from the list of words


    def start_new_game(self,widget):
        self.secret_word = self.get_word()  # calling get_word function
        print(self.secret_word)

        self.secret_letters = set(self.secret_word)
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
            if lowercase in self.secret_letters: #if letter is in word, replace underscore with letter
                self.correct_letters = self.correct_letters.union(widget.value)
            else:
                pass
        else:
            print('Not a valid alphabet')

        self.game_state() #continue game as usual

    def enter_own_word(self,widget):
        print("second button clicked")

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

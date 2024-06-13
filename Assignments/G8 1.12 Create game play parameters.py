#Task: Map the "Start a new game" button to "start_new_game" function

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import random

class Word(toga.App):

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


    def get_word(self):
        random_item = random.choice(Word.all_words)
        return random_item

    def start_new_game(self,widget):
        self.secret_word = self.get_word()
        print(self.secret_word)

        self.secret_letters = set(self.secret_word) #unique set of secret_letters from secret word
        self.used_letters = [] #start with empty bucket of used letter
        self.lives = 7  # start with 7 lives
        self.correct_letters = set()  #start with empty set of correct letters
        self.revealed_word = ["_"] * len(self.secret_word)  #start with no revealed letters, all blanks
        self.game_state() #calling the function to start the game

    #Game State at every iteration
    def game_state(self):
        box = toga.Box(style=Pack(direction=COLUMN))

        #heading
        box.add(toga.Label("Guess a Letter!"))
        box.add(toga.Label("Word: " + " ".join(self.revealed_word)))

        # used letters + lives
        box.add(toga.Label("Used Letters: " + " ".join(self.used_letters)))
        box.add(toga.Label("Lives: " + str(self.lives)))

        #buttons
        box.add(toga.Button("Start a New Game", on_press=))
        box.add(toga.Button("Start game with own word", on_press=self.enter_own_word))

        self.main_window.content = box

    def enter_own_word(self,widget):
        print("second button clicked")

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)# Write your code here :-)

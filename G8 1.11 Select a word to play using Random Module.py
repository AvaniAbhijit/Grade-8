# Task: Run the program, click on button "Play Word Game" and note down the random word which is printed on the console.
# Do the above task 3 to 4 times.

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import random

class Word(toga.App):

    all_words = ["hello", "python", "except", "acquire", "temperature"]
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

    def get_word(self): #defining function to pick a random word
        print("All Words: ", Word.all_words)
        random_item = random.choice(Word.all_words) #using random function to pick a random word from the list
        return random_item #return the picked word

    def start_new_game(self,widget):
        self.secret_word = self.get_word() # get a random word
        print("selected word: ", self.secret_word) #print the random word

    def enter_own_word(self,widget):
        print("second button clicked")

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

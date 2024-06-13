#Task: Perform list operations: access the first element by print(all_words[0]) etc. Read the data on the console

import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class Word(toga.App):

    all_words= ["hello", "python", "except", "acquire", "temperature"] #defining variable to store all the words
    print(all_words)
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

    def start_new_game(self,widget):
        print("Button is clicked")

    def enter_own_word(self,widget):
        print("second button clicked")

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)# Write your code here :-)

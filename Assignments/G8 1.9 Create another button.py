#Task 1: Create another button "Start game with own word" below the first button
#Task 2: Create another function to print "Give me the word" when the above button is pressed

import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class Word(toga.App):
    title_style=Pack(text_align="center",font_size=20,font_weight="bold", color=("blue"))


    def startup(self):
        label1 = toga.Label("Word Game", style=Word.title_style)
        button1 = toga.Button("Play Word Game",on_press=self.start_new_game)

        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(label1)
        main_box.add(button1)

        self.main_window = toga.MainWindow(title="Simple Window")
        self.main_window.content=main_box
        self.main_window.show()

    def start_new_game(self,widget):
        print("Button is clicked")


app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

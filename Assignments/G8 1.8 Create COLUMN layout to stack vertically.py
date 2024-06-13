#Task: Create another label "All IPL players name" and adjust it in between the first label and the button

import toga
from toga.style import Pack
from toga.style.pack import COLUMN #importing column

class Word(toga.App):
    title_style=Pack(text_align="center",font_size=20,font_weight="bold")
    def startup(self):
        label = toga.Label("Word Game", style=Word.title_style)
        button = toga.Button("Play Word Game",on_press=self.start_new_game)

        main_box = toga.Box(style=Pack(direction=COLUMN))#setting the direction of adding elements as column to display elements vertically
        main_box.add(label)
        main_box.add(button)

        self.main_window = toga.MainWindow(title="Simple Window")
        self.main_window.content=main_box
        self.main_window.show()

    def start_new_game(self,widget):
        print("Button is clicked")

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

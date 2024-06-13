#Task 1: Change the text size to 30.
#Task 2: Change the alignment from center to something else

import toga
from toga.style import Pack

class Word(toga.App):
    title_style=Pack(text_align="center",font_size=20,font_weight="bold")
    def startup(self):
        label = toga.Label("Word Game", style=Word.title_style)

        self.main_window = toga.MainWindow(title="Simple Window")
        #adding label to window
        self.main_window.content=label
        self.main_window.show()

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

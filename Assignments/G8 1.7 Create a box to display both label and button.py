#Task: Try adding one more label and a button to the window.

import toga
from toga.style import Pack

class Word(toga.App):
    title_style=Pack(text_align="center",font_size=20,font_weight="bold")

    def startup(self):
        label = toga.Label("Word Game", style=Word.title_style)
        button = toga.Button("Play Word Game",on_press=self.start_new_game)

        main_box = toga.Box() #creating a box, default ROW layout
        main_box.add(label) #adding label inside main_box
        main_box.add(button) #adding button inside main_box

        self.main_window = toga.MainWindow(title="Simple Window")
        self.main_window.content=main_box #changing the content to main_box
        self.main_window.show()

    def start_new_game(self,widget):
        print("Button is clicked")

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

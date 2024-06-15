#Task 1: Comment lines 14 and 20 to view the label (Why does this happen?)
#Task 2: Try creating another button and run the code

import toga
from toga.style import Pack

class Word(toga.App):
    title_style=Pack(text_align="center",font_size=20,font_weight="bold")

    def startup(self):
        label = toga.Label("Word Game", style=Word.title_style)

        #create a button and call start_new_game method when clicked
        button=toga.Button("Play Word Game",on_press=self.start_new_game)
        self.main_window = toga.MainWindow(title="Simple Window")

        #adding Label on screen. But, not visible
        self.main_window.content=label
        #adding button on screen
        self.main_window.content=button

        self.main_window.show()

    def start_new_game(self,widget): #widget will accept the button that triggered the event
        print("Button is clicked")

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

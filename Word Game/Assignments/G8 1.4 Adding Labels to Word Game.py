#Task: Change the label to "My first game design"

import toga

class Word(toga.App):
    def startup(self):
        label = toga.Label("Hello Toga") #creating a label
        self.main_window = toga.MainWindow(title="Simple Window")
        self.main_window.content=label #adding label on window
        self.main_window.show()

app = Word('Simple Toga App', 'org.example.simpletoga')
app.main_loop()# Write your code here :-)

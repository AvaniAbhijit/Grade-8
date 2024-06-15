#Task: Run the program and see the output

import toga

class Word(toga.App): #create a class named word
    def startup(self): #create a function to create window and add components
        self.main_window = toga.MainWindow(title="Simple Window") #create a window
        self.main_window.show() #display the window

#This line starts running the Word application
app = Word('Simple Toga App', 'o')
app.main_loop()# Write your code here :-)

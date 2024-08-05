# task1: create a toga Box to display options below the selection option label in display_selected_option()
# task2 : Create a dropdown with Options as - Select an option, Option 1, Option 2, Option 3, Option 4
# task3: Let the on_change event handler call a function called - check_answer()

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import firebase_admin
from firebase_admin import credentials, db
import random

# Initialize Firebase Admin SDK
cred = credentials.Certificate('quiz-app.json')  # Replace with your service account key file
firebase_admin.initialize_app(cred,
                              {'databaseURL': 'https://quiz-app-4f392-default-rtdb.firebaseio.com/'})

class LoginApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='QuizApp')

        self.username_input = toga.TextInput(placeholder='Username')
        self.password_input = toga.PasswordInput(placeholder='Password')
        self.login_button = toga.Button('Login',on_press=self.login)
        self.status_label = toga.Label(' ', style=Pack(padding=10))

        self.new_username_input = toga.TextInput(placeholder='New Username')
        self.new_password_input = toga.PasswordInput(placeholder='New Password')
        self.register_button = toga.Button('Register',on_press=self.register)

        login_box = toga.Box(style=Pack(padding=10))
        login_box.add(self.username_input)
        login_box.add(self.password_input)
        login_box.add(self.login_button)

        register_box = toga.Box(style=Pack(padding=10))
        register_box.add(self.new_username_input)
        register_box.add(self.new_password_input)
        register_box.add(self.register_button)

        content_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        content_box.add(login_box)
        content_box.add(register_box)
        content_box.add(self.status_label)

        self.main_window.content = content_box
        self.main_window.show()

    def login(self, widget):
        username = self.username_input.value.strip()
        password = self.password_input.value.strip()

        # Construct the user ID from the username (assuming usernames are unique)
        user_id = username

        try:
            # Retrieve user credentials from Firebase Realtime Database
            user_password_ref = db.reference('users/'+user_id)
            stored_password = user_password_ref.get()

            if stored_password:
                if stored_password == password:
                    #self.main_window.info_dialog('Login Successful', 'Welcome, {}!'.format(username))
                    self.show_quiz(username)
                    return
                else:
                    self.main_window.error_dialog('Login Failed', 'Invalid password')
                    print("Incorrect password for user:", username)
            else:
                self.main_window.error_dialog('Login Failed', 'Invalid username')
                print("User not found:", username)
        except Exception as e:
            print("Error fetching user data:", e)

    def register(self, widget):
        new_username = self.new_username_input.value.strip()
        new_password = self.new_password_input.value.strip()

        # Construct the user ID from the new username
        user_id = new_username

        try:
            # Check if the user already exists
            user_ref = db.reference('users/'+user_id)
            if user_ref.get():
                self.main_window.error_dialog('Registration Failed', 'Username already exists.')
                return

            # If the user doesn't exist, register the new user
            user_ref.set(new_password)
            self.main_window.info_dialog('Registration Successful', 'Welcome, {}!'.format(new_username))
        except Exception as e:
            print("Error registering user:", e)

    def show_quiz(self,username):
        box1 = toga.Box(style=Pack(direction=COLUMN, padding = 10))

        message_label = toga.Label(f'Welcome to the Quiz {username}!', style=Pack(padding=10))
        selection = toga.Selection(items=["Select a subject", "Maths", "Physics", "Computer Science", "General Knowledge"], on_change=self.display_selected_option) #call function when user selects an option
        selection.value = "Select a subject"

        # Create a button to close the new window
        close_button = toga.Button("Close")
        box1.add(message_label)
        box1.add(selection)
        box1.add(close_button)

        self.selected_label = toga.Label('Selected option: ')
        box1.add(self.selected_label)

        self.main_window.content = box1
        
    def display_selected_option(self, widget): #function to identify the selected option
        selected_option = widget.value #get the value
        self.selected_label.text = f"Selected option: {selected_option}" #display it
        

        #create a box and add the options dropdown to it

        # specify the box name within add() to add it to the main window and uncomment the below line
        #self.main_window.content.add()

    def check_answer():
        pass
    
def main():
    return LoginApp('fbconnect', 'fbconn')

if __name__ == '__main__':
    app = main()
    app.main_loop()

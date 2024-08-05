# task 1: Create a label in the new window to display the selected option
# task 2: Add on_change callback function as display_selected_option for the selection widget
# task 3: In display_selected_option, fetch the value of the selected option and display it in the label created.

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import firebase_admin
from firebase_admin import credentials, db

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
                    print("Incorrect password for user:", username)
            else:
                print("User not found:", username)
        except Exception as e:
            print("Error fetching user data:", e)

        # If no matching user found or error occurred, show error message
        self.main_window.error_dialog('Login Failed', 'Invalid username or password')

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
        selection = toga.Selection(items=["Select a subject", "Maths", "Physics", "Computer Science", "General Knowledge"]) #call function when user selects an option
        selection.value = "Select a subject"

        # Create a button to close the new window
        close_button = toga.Button("Close")
        box1.add(message_label)
        box1.add(selection)
        box1.add(close_button)

        #Create a label to display the selected option and add it to the box
        
        self.main_window.content = box1
        

    def display_selected_option(self, widget): #function to identify the selected option
        # get the value of the widget
        # display it in the label created above. 
    
app = LoginApp('fbconnect', 'fbconn')
app.main_loop()

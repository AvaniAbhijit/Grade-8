# task 1: Observe the register() function and complete the login() function on line 47,48,55,56,61
# task 2: take care of the error message on line 67.
# task 3: Reset the values of new_username and new_password after the user is registered on line 95

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
        #retrieve the username / password entered in the login input
        username =
        password =
        
        # Construct the user ID from the username (assuming usernames are unique)
        user_id = 'users/' + username

        try:
            # Retrieve user credentials from Firebase Realtime Database
            user_password_ref = 
            stored_password = 
            

            if stored_password:
                #check if the stored password is same as user entered password
                if ___________:
                    self.main_window.info_dialog('Login Successful', f'Welcome, {username}!')
                    return
                else:
                    self.main_window.error_dialog("Login Fail", f"Incorrect password for {username}")
            else:
                # display an error dialog that the user is not found.
        except Exception as e:
            print("Error fetching user data:", e)

        # If no matching user found or error occurred, show error message
        self.main_window.error_dialog('Login Failed', 'Invalid username or password')

    def register(self, widget):
        new_username = self.new_username_input.value.strip()
        new_password = self.new_password_input.value.strip()

        # Construct the user ID from the new username
        user_id = 'users/' + new_username

        try:
            # Check if the user already exists
            user_ref = db.reference(user_id)
            if user_ref.get():
                self.main_window.error_dialog('Registration Failed', 'Username already exists.')
                return

            # If the user doesn't exist, register the new user
            user_ref.set(new_password)
            self.main_window.info_dialog('Registration Successful', 'Welcome, {}!'.format(new_username))
        except Exception as e:
            print("Error registering user:", e)
            
        #reset the username and password to blanks.

app = LoginApp('fbconnect', 'fbconn')
app.main_loop()


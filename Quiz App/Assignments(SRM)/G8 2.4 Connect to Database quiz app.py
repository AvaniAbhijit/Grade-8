#task 1: Download the service account key JSON file
#task 2: replace the JSON file name within the quotes on line 13
#task 3: Replace the URL link of the firebase in place of URL string on line 14

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
# Replace with your service account key file
cred = credentials.Certificate('json file')
firebase_admin.initialize_app(cred,{'databaseURL': 'URL'})

class LoginApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='QuizApp')

        self.username_input = toga.TextInput(placeholder='Username')
        self.password_input = toga.PasswordInput(placeholder='Password')
        self.login_button = toga.Button('Login')

        self.new_username_input = toga.TextInput(placeholder='New Username')
        self.new_password_input = toga.PasswordInput(placeholder='New Password')
        self.register_button = toga.Button('Register')

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

app = LoginApp('fbconnect', 'fbconn')
app.main_loop()


#task 1: Run and see the output. Recall the widgets that you see on the window.
#task 2: Create Login and Password TextInputs above Register inputs.
#task 3: Add the login components to a toga box
#task 4: Add the login Box to Content Box
#task 5: Add Main Box to main window content.

import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class LoginApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='QuizApp')

        # Create UI components for login


        # Create UI components for registration
        self.new_username_input = toga.TextInput(placeholder='New Username')
        self.new_password_input = toga.PasswordInput(placeholder='New Password')
        self.register_button = toga.Button('Register')

        # Add login components to toga Box


        # Add registration components to toga Box
        register_box = toga.Box(style=Pack(padding=10))
        register_box.add(self.new_username_input)
        register_box.add(self.new_password_input)
        register_box.add(self.register_button)

        content_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Add login and registration components to main Box
        content_box.add(register_box)

        # Add UI components to main window
        self.main_window.content = content_box

        # Show the main window
        self.main_window.show()

app = LoginApp('fbconnect', 'fbconn')
app.main_loop()

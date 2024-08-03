import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class LoginApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='QuizApp')

        # Create UI components for login
        self.username_input = toga.TextInput(placeholder='Username')
        self.password_input = toga.PasswordInput(placeholder='Password')
        self.login_button = toga.Button('Login')
        
        # Create UI components for registration
        self.new_username_input = toga.TextInput(placeholder='New Username')
        self.new_password_input = toga.PasswordInput(placeholder='New Password')
        self.register_button = toga.Button('Register')

        # Add login components to toga Box
        login_box = toga.Box(style=Pack(padding=10))
        login_box.add(self.username_input)
        login_box.add(self.password_input)
        login_box.add(self.login_button)

        # Add registration components to toga Box
        register_box = toga.Box(style=Pack(padding=10))
        register_box.add(self.new_username_input)
        register_box.add(self.new_password_input)
        register_box.add(self.register_button)

        content_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        # Add login and registration components to main Box
        content_box.add(login_box)
        content_box.add(register_box)
        
        # Add UI components to main window
        self.main_window.content = content_box

        # Show the main window
        self.main_window.show()

app = LoginApp('fbconnect', 'fbconn')
app.main_loop()

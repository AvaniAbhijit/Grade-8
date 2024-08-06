# Run the program and see the output. what do you see?
# Once the first question is answered, it showed the next question
# Only first option got updated for the 2nd question.
# after answering the 2nd question, the box of questions disappeared.
# task1: Update the other options for the 2nd question

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
        self.score = 0
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

        # Add a button to close the new window
        close_button = toga.Button("Close")
        box1.add(message_label)
        box1.add(selection)
        box1.add(close_button)

        
        self.main_window.content = box1
        

    def display_selected_option(self, widget): #function to identify the selected option
        selected_option = widget.value #get the value

        if selected_option == 'Maths':
            ques_str='Maths'
        elif selected_option == 'Physics':
            ques_str = 'Phy'
        elif selected_option == 'Computer Science':
            ques_str = 'CS'
        else:
            ques_str= 'GK'

        ques_ref = db.reference(ques_str)
        self.ques = random.sample(list(ques_ref.get().items()),2)
        self.current_index = 0    
        self.box2 = toga.Box(style=Pack(direction=COLUMN, padding = 10))
        self.ques_label = toga.Label('Question: '+ self.ques[self.current_index][0], style=Pack(padding=10))
        self.box2.add(self.ques_label)
        self.option1=toga.Label('Option 1: ' + str(self.ques[self.current_index][1]['op1']), style=Pack(padding=10))
        self.box2.add(self.option1)
        self.option2=toga.Label('Option 2: ' + str(self.ques[self.current_index][1]['op2']), style=Pack(padding=10))
        self.box2.add(self.option2)
        self.option3=toga.Label('Option 3: ' + str(self.ques[self.current_index][1]['op3']), style=Pack(padding=10))
        self.box2.add(self.option3)
        self.option4=toga.Label('Option 4: ' + str(self.ques[self.current_index][1]['op4']), style=Pack(padding=10))
        self.box2.add(self.option4)

        self.select = toga.Selection(items=["Select an option", "option : 1","option : 2","option : 3","option : 4"],on_change=self.check_answer)
        self.select.value = "Select an option"
        self.box2.add(self.select)          

        self.main_window.content.add(self.box2)

    def check_answer(self, widget):
        
        #increment the current index to fetch the next question        
        self.current_index += 1

        # if the current index if not 2, fetch the next question
        if self.current_index < len(self.ques):
            # Update the question label with the next question
            self.ques_label.text = 'Question: ' + self.ques[self.current_index][0]

            # Update options for the next question
            self.option1.text = 'Option 1: ' + str(self.ques[self.current_index][1]['op1'])
            

        # if the current index is 2, then allow to select the next category            
        else:
            # Remove the questions box from the window
            self.main_window.content.remove(self.box2)
        
    
app = LoginApp('fbconnect', 'fbconn')
app.main_loop()

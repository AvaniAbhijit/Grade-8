# task 1: create your styles for title and score. Assign these styles to title and score.
# task 2: Associate close_win() function with close button by on_press event handler on it

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
    button_style = Pack(padding=(0, 5), font_size=10, text_align="center")
    text_style=Pack(font_size=10, padding=5)
    text_style1=Pack(font_weight="bold", font_size=10, padding=5)
    
    def startup(self):
        self.main_window = toga.MainWindow(title='QuizApp')

        label1 = toga.Label("Ready for QUIZ")
        
        self.username_input = toga.TextInput(placeholder='Username', style=LoginApp.text_style)
        self.password_input = toga.PasswordInput(placeholder='Password', style=LoginApp.text_style)
        self.login_button = toga.Button('Login',on_press=self.login, style=LoginApp.button_style)
        
        self.new_username_input = toga.TextInput(placeholder='New Username', style=LoginApp.text_style)
        self.new_password_input = toga.PasswordInput(placeholder='New Password', style=LoginApp.text_style)
        self.register_button = toga.Button('Register',on_press=self.register, style=LoginApp.button_style)

        login_box = toga.Box(style=Pack(padding=10))
        login_box.add(self.username_input)
        login_box.add(self.password_input)
        login_box.add(self.login_button)

        register_box = toga.Box(style=Pack(padding=10))
        register_box.add(self.new_username_input)
        register_box.add(self.new_password_input)
        register_box.add(self.register_button)

        content_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        content_box.add(label1)
        content_box.add(login_box)
        content_box.add(register_box)
        
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

        message_label = toga.Label(f'Welcome to the Quiz {username}!')
        selection = toga.Selection(items=["Select a subject", "Maths", "Physics", "Computer Science", "General Knowledge"],
                                   on_change=self.display_selected_option, style=LoginApp.text_style) #call function when user selects an option
        selection.value = "Select a subject"

        # Add a button to close the new window
        close_button = toga.Button("Close", style=LoginApp.button_style)
        box1.add(message_label)

        # Display score
        self.score_label = toga.Label(f'Score: {self.score}')
        box1.add(self.score_label)
        
        box1.add(selection)
        box1.add(close_button)
        
        self.main_window.content = box1
    
    def close_win(self, widget):
        self.main_window.close()

    def display_selected_option(self, widget): #function to identify the selected option
        selected_option = widget.value #get the value
        #self.selected_label.text = f"Selected option: {selected_option}" #display it
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
        self.ques_label = toga.Label('Question: '+ self.ques[self.current_index][0], style=LoginApp.text_style1)
        self.box2.add(self.ques_label)
        self.option1=toga.Label('Option 1: ' + str(self.ques[self.current_index][1]['op1']), style=LoginApp.text_style)
        self.box2.add(self.option1)
        self.option2=toga.Label('Option 2: ' + str(self.ques[self.current_index][1]['op2']), style=LoginApp.text_style)
        self.box2.add(self.option2)
        self.option3=toga.Label('Option 3: ' + str(self.ques[self.current_index][1]['op3']), style=LoginApp.text_style)
        self.box2.add(self.option3)
        self.option4=toga.Label('Option 4: ' + str(self.ques[self.current_index][1]['op4']), style=LoginApp.text_style)
        self.box2.add(self.option4)

        self.select = toga.Selection(items=["Select an option", "option : 1","option : 2","option : 3","option : 4"],
                                     on_change=self.check_answer , style=LoginApp.text_style1)
        self.select.value = "Select an option"
        self.box2.add(self.select)
        
        self.score_label.text = f'Score: {self.score}'

        self.main_window.content.add(self.box2)

    def check_answer(self, widget):
        selected_index = widget.value.split()[2]  # example - ['o','p','1']
        if int(selected_index) == self.ques[self.current_index][1]['ans']:
            self.score +=1
            self.score_label.text = f'Score: {self.score}'
                
        self.current_index += 1
        if self.current_index < len(self.ques):
            # Update the question label with the next question
            self.ques_label.text = 'Question: ' + self.ques[self.current_index][0]
            self.option1.text = 'Option 1: ' + str(self.ques[self.current_index][1]['op1'])
            self.option2.text = 'Option 2: ' + str(self.ques[self.current_index][1]['op2'])
            self.option3.text = 'Option 3: ' + str(self.ques[self.current_index][1]['op3'])
            self.option4.text = 'Option 4: ' + str(self.ques[self.current_index][1]['op4'])           
        
        else:
            self.main_window.content.remove(self.box2)
        
    
app = LoginApp('fbconnect', 'fbconn')
app.main_loop()

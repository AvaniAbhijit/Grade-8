#task 1: Understand the add_data() function and fetch_data() function.
#task 2: Add 2 more users to the database using add_data
#task 3: Print data in fetch_data() and see the result. 

import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate('quiz_key.json')  # Replace with your service account key file
firebase_admin.initialize_app(cred,
                              {'databaseURL': 'https://quiz-6a3fe-default-rtdb.asia-southeast1.firebasedatabase.app/User'})

# Function to add data to Firebase
def add_data(name, email):
    ref = db.reference('/users')  # Reference to the 'users' node in your Firebase Realtime Database
    new_user_ref = ref.push()  # Create a new child node under 'users'
    new_user_ref.set({
        'name': name,
        'email': email
    })

# Function to fetch data from Firebase
def fetch_data():
    ref = db.reference('/users')  # Reference to the 'users' node in your Firebase Realtime Database
    data = ref.get()
    

# Add data to Firebase
add_data('John','john@example.com')

# Fetch data from Firebase
fetch_data()

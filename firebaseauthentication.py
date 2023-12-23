import pyrebase
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

#Get Firebase config from Firebase portal while creating project
firebase_config_str = os.getenv('FIREBASE_CONFIG')

# Parse the JSON string into a Python dictionary
firebase_config = json.loads(firebase_config_str)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


def registration():
    email = input("Enter email: ")
    password = input("Enter password: ")
    register = auth.create_user_with_email_and_password(email, password)
    print(register)
    print("Successfully created account")

registration()
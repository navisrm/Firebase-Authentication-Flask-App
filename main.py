import pyrebase
import json
from requests.exceptions import HTTPError
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

#Get Firebase config from Firebase portal while creating project
firebase_config_str = os.getenv('FIREBASE_CONFIG')
email_ = os.getenv("email")
password_ = os.getenv("password")

# Parse the JSON string into a Python dictionary
firebase_config = json.loads(firebase_config_str)

firebase = pyrebase.initialize_app(firebase_config)

# Get a reference to the auth service
auth = firebase.auth()

email = email_
password = password_

def create_user(email, password):
    #Create the user
    user = auth.create_user_with_email_and_password(email, password)
    print(user['idToken'])
    link = auth.send_email_verification(user['idToken'])
    print(link)

def login(email, password):

    # Login:
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)

    except Exception as e:
        print(json.loads(e.args[1])['error']['message'])


def send_reset_password_link(email):
    #Send pass reset email:
    reset_pass = auth.send_password_reset_email(email)
    print(reset_pass)

def verify_password_reset_code(email, new_password):
    reset_code = auth.verify_password_reset_code(email, new_password)
    print(reset_code)


# create_user(email, password)
# login(email, password)
send_reset_password_link(email)
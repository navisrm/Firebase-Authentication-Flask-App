from flask import Flask, render_template, request, redirect, session
import traceback
import pyrebase
import json
from functools import wraps
from dotenv import load_dotenv
import os
from utils import send_email

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Load environment variables from .env file
load_dotenv()

#Get Firebase config from Firebase portal while creating project
firebase_config_str = os.getenv('FIREBASE_CONFIG')

# Parse the JSON string into a Python dictionary
firebase_config = json.loads(firebase_config_str)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return render_template('login.html')
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # Use Firebase Authentication for user registration
            user = auth.create_user_with_email_and_password(
                email=email,
                password=password
            )
            user_idtoken = user['idToken']

            # Send email verification
            auth.send_email_verification(user_idtoken)

            # Render a success page if registration is successful
            return render_template('register_success.html', email=email)

        except Exception as e:
            # Handle registration failure
            # Extract and display the error message from the Firebase response
            error_message = json.loads(e.args[1])['error']['errors'][0]['message']
            return render_template('register.html', error=error_message)

    # Render the registration page for GET requests
    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            # Use Firebase Authentication for user login
            user = auth.sign_in_with_email_and_password(email, password)

            user_idtoken = user['idToken']

            # Check if the user's email is verified
            email_verified = auth.get_account_info(user_idtoken)['users'][0]['emailVerified']

            # If email is verified, store user_id in session and redirect to dashboard
            if email_verified:
                session['user_id'] = user['localId']
                return redirect('/dashboard')
            else:
                # If email is not verified, display an error message
                return render_template('login.html', error='Email not verified. Check your inbox.')

        except Exception as e:
            # Handle login failure
            # Extract and display the error message from the Firebase response
            error_message = json.loads(e.args[1])['error']['errors'][0]['message']
            return render_template('login.html', error=error_message)

    # Render the login page for GET requests
    return render_template('login.html')



@app.route('/logout', methods=['GET'])
def logout():
    # Clear the user_id from the session
    session.pop('user_id', None)

    # Redirect to the login page after logout
    return render_template('logout.html')

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    # If the user is authenticated, render the dashboard
    print(session['user_id'])
    return render_template('dashboard.html')


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Extract email from the form data
        email = request.form.get('email')

        # Validate if email is provided
        if not email:
            # If email is not provided, render the forgot_password page with an error message
            return render_template('forgot_password.html', error='Error. Please enter a valid email')

        try:
            # Send reset email using Firebase Authentication
            auth.send_password_reset_email(email)

            # Render the login page with a success message
            return render_template('login.html', info='An email with instructions to reset your password has been sent.')

        except Exception as e:
            # Handle any exceptions during the password reset process
            error_message = json.loads(e.args[1])['error']['message']
            return render_template('forgot_password.html', error=error_message)

    # Render the forgot_password page for GET requests
    return render_template('forgot_password.html')






if __name__ == '__main__':
    app.run(debug=True)
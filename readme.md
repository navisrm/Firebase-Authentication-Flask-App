# Firebase-Authentication-Flask-App

This project is a user authentication application built on the Python Flask framework, leveraging Firebase for secure and scalable user management. The application incorporates essential features for user authentication, ensuring a seamless and secure user experience.

## Project Highlights:
### Technology Stack:

**Backend Framework:** Python Flask

**Authentication Service:** Firebase
### Features:

**User Registration:**
Users can sign up for the application, providing their email and password.
Firebase Authentication services handle the user registration process.

**Email Verification:**
After registration, users receive a verification email to confirm their email address.
Email verification is an essential step to enhance security and ensure valid user accounts.

**User Sign-In:**
Registered users can securely sign in using their email and password.
Firebase handles the authentication process, verifying user credentials.

**User Sign-Out:**
Users can log out of their accounts to end their session securely.


## Firebase Setup

1. Create a new project on the [Firebase Console](https://console.firebase.google.com/).
2. In the project settings, navigate to "Service accounts" and generate a new private key. Save the downloaded JSON file in the project root.
3. Register your app for the "web" platform on the Firebase Console. Obtain the configuration for the web project, and save it in a `.env` file in the project root.

## Execution

1. Create a virtual environment for the project:

   ```bash
   python -m venv venv

2. Activate virtual env

   ```bash
   source venv\Scripts\activate

4. Install requirements

   ```bash
   pip install -r requirements.txt

6. Run application

   ```bash
   python app.py


### To Do:

- Add profile where user can provide firstname, lastname
- add payment integration for monthly subscription
- create requirements.txt file. Firebaseadmin and someunnecessary packages must be removed

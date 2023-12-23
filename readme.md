# Firebase-Authentication-Flask-App

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

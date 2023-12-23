import firebase_admin
from firebase_admin import credentials, auth


cred = credentials.Certificate('service-account-key.json')
firebase_admin.initialize_app(cred)

def print_user_records():
    try:
        # List all users
        users = auth.list_users()

        # Print user details
        for user in users.users:
            print(f"User UID: {user.uid}")
            print(f"Display Name: {user.display_name}")
            print(f"Email: {user.email}")
            print(f"Email Verified: {user.email_verified}")
            print(f"Phone Number: {user.phone_number}")
            print(f"Disabled: {user.disabled}")
            print("----")
            

    except auth.AuthError as e:
        print(f"Error listing users: {e}")

# Call the function to print user records
print_user_records()
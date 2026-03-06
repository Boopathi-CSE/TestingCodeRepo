from auth import AuthService
from session_manager import SessionManager
import time

auth_service = AuthService()
session_manager = SessionManager()


def show_menu():
    print("\n==== Secure Notes ====")
    print("1. Login")
    print("2. View Notes")
    print("3. Logout")
    print("0. Exit")


def main():

    session_id = None

    while True:

        show_menu()
        choice = input("Select option: ")

        if choice == "1":

            username = input("Username: ")
            password = input("Password: ")

            if auth_service.login(username, password):

                session_id = session_manager.create_session(username)
                print("Login successful.")

            else:
                print("Invalid credentials")

        elif choice == "2":

            if not session_id:
                print("Please login first.")
                continue

            if not session_manager.is_session_active(session_id):
                print("Session expired. Please login again.")
                session_id = None
                continue

            print("\nYour Notes:")
            print("- Finish AI project")
            print("- Prepare presentation")
            print("- Review system logs")

        elif choice == "3":

            if session_id:
                session_manager.end_session(session_id)
                session_id = None
                print("Logged out.")
            else:
                print("No active session")

        elif choice == "0":

            print("Goodbye")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
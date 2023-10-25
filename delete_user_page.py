# GROUP 8

# Imports the tkinter library for GUI development
import tkinter as tk

# Imports messagebox, load_user_data_from_csv, username_arr, password_arr, save_user_data_to_csv
from tkinter import messagebox
from user_registration_data import load_user_data_from_csv, username_arr, password_arr, save_user_data_to_csv

# Creates a class named DeleteUserPage that inherits from tk.Frame
# Allows users to be deleted making number of registered users to go below 10 so that more users can register (Makes the GUI more convenient!)
class DeleteUserPage(tk.Frame):
    def __init__(self, master, controller):
        # Initializes the DeleteUserPage class
        tk.Frame.__init__(self, master)

        # Stores a reference to the controller (GUI) that manages this page
        self.controller = controller

        # Calls the setup_ui method to create and configure the UI elements
        self.setup_ui()

    # Method to create and configure the UI elements
    def setup_ui(self):
        # Creates a label widget displaying "Delete My User" with a specific font
        self.deleteUser_label = tk.Label(self, text="Delete My User", font=("Arial", 30))
        self.deleteUser_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

        # Creates a label widget displaying a message with a specific font
        self.toDeleteMessage_label = tk.Label(self, text="Enter your username and password to delete your user:", font=("Arial", 13))
        self.toDeleteMessage_label.grid(row=1, column=0, columnspan=2, sticky="news", pady=10)

        # Creates a label widget displaying "Username:" with a specific font
        self.username_label = tk.Label(self, text="Username:", font=("Arial", 16))
        self.username_label.grid(row=2, column=0, pady = 10)

        # Creates an entry widget for entering the username with a specific font
        self.usernameDelete_entry = tk.Entry(self, font=("Arial", 14))
        self.usernameDelete_entry.grid(row=2, column=1)

        # Creates a label widget displaying "Password:" with a specific font
        self.password_label = tk.Label(self, text="Password:", font=("Arial", 16))
        self.password_label.grid(row=3, column=0)

        # Creates an entry widget for entering the password with a specific font and password mask
        self.passwordDelete_entry = tk.Entry(self, show="*", font=("Arial", 14))
        self.passwordDelete_entry.grid(row=3, column=1)

        # Creates and configures buttons
        # Create a "Delete my User" button with specific text, font, and a command to perform deleteUser_check to check if user exists
        self.delete_button = tk.Button(self, text="Delete my User", font=("Arial", 13), command=self.deleteUser_check)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Creates a "Back to Welcome Page" button with specific text, font, and a command to go to the welcome page
        self.back_button = tk.Button(self, text="Back to Welcome Page", font=("Arial", 13), command=self.go_to_welcome_page)
        self.back_button.grid(row=5, column=0, columnspan=2)
    
    # Method to perform user deletion check
    def deleteUser_check(self):
        # Collects the entered username and password from the entry widgets
        entered_username = self.usernameDelete_entry.get()
        entered_password = self.passwordDelete_entry.get()

        # Checks if either the username or password field is empty
        if not entered_username or not entered_password:
            # Display an error message using a messagebox if string is empty
            messagebox.showerror("Error", "Username and/or password cannot be empty.")
            return

        # Load user data from the CSV file to check if entered username and password exists in the user registration csv
        load_user_data_from_csv()

        # Checks if the entered username and password exist in the CSV file
        user_found = False
        #Pairs together usernames and passwords in username and password arrays
        for username, password in zip(username_arr, password_arr):
            #Checks if the pairing of entered username and password matches values in the user registration csv file
            #This allows for no incorrect entry of one's username to someone else's password
            if entered_username == username and entered_password == password:
                # If a match is found, remove the user from the lists
                username_arr.remove(username)
                password_arr.remove(password)
                save_user_data_to_csv()  # Save the updated user data to the CSV file
                user_found = True
                break

        if user_found:
            # Display a success message using a messagebox
            messagebox.showinfo("Success", "User deleted successfully.")
            # Optionally, you can clear the entry fields here:
            self.usernameDelete_entry.delete(0, tk.END)
            self.passwordDelete_entry.delete(0, tk.END)
        else:
            # Display an error message using a messagebox
            messagebox.showerror("Error", "Username and/or Password cannot be found")

    # Method to navigate to the welcome page
    def go_to_welcome_page(self):
        self.controller.show_welcome_page()

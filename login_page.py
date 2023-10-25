# GROUP 8
#
# Imports the tkinter library for GUI development
import tkinter as tk

# Imports username_arr, password_arr, load_user_data_from_csv, and save_user_data_to_csv from the user_data module
from user_registration_data import username_arr, password_arr, load_user_data_from_csv, save_user_data_to_csv

# Imports the messagebox module for displaying pop-up messages
from tkinter import messagebox

# Imports the PacemakerGUI class
from DCM_Interface import PacemakerGUI

# Create a class named LoginPage that inherits from tk.Frame
class LoginPage(tk.Frame):
    def __init__(self, master, controller): #master is the parent widget and controller is the GUI
        # Initializes the LoginPage class
        tk.Frame.__init__(self, master)

        # Stores a reference to the controller (GUI) that manages this page
        self.controller = controller

        # Creates a label widget displaying "Login" with a specific font
        self.login_label = tk.Label(self, text="Login", font=("Arial", 30))
        # Places widgets using the grid layout manager
        self.login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

        # Creates a label widget displaying "Username:" with a specific font
        self.username_label = tk.Label(self, text="Username:", font=("Arial", 16))
        # Places widgets using the grid layout manager
        self.username_label.grid(row=1, column=0, pady=10)

        # Creates an entry widget for entering the username with a specific font
        self.username_entry = tk.Entry(self, font=("Arial", 14))
        # Places widgets using the grid layout manager
        self.username_entry.grid(row=1, column=1)

        # Creates a label widget displaying "Password:" with a specific font
        self.password_label = tk.Label(self, text="Password:", font=("Arial", 16))
        # Places widgets using the grid layout manager
        self.password_label.grid(row=2, column=0)

        # Creates an entry widget for entering the password with a specific font and password mask
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 14))
        # Places widgets using the grid layout manager
        self.password_entry.grid(row=2, column=1)

        # Creates and configure buttons
        # Creates a "Login" button with specific text, font, and a command to perform login_check which checks if login conditions are met
        self.login_button = tk.Button(self, text="Login", font=("Arial", 13), command=self.login_check)
        # Places widgets using the grid layout manager
        self.login_button.grid(row=3, column=0, columnspan=2, pady=30)

        # Create a "Back to Welcome Page" button with specific text, font, and a command to go back to the welcome page
        self.back_button = tk.Button(self, text="Back to Welcome Page", font=("Arial", 13), command=self.go_to_welcome_page)
        self.back_button.grid(row=4, column=0, columnspan=2)

    # Method to perform login check
    def login_check(self):
        # Collects the entered username and password from the entry widgets
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        # Checks if either the username or password field is empty
        if not entered_username or not entered_password:
            # Displays an error message using a messagebox if empty string is entered
            messagebox.showerror("Error", "Username and/or password cannot be empty.")
            return

        # Load user data from the CSV file to check if the user that is trying to login exists
        load_user_data_from_csv()

        # Check if the entered username and password match any user's credentials
        user_found = False
        #Pairs together usernames and passwords in username and password arrays
        for username, password in zip(username_arr, password_arr):
            #Checks if the pairing of entered username and password matches values in the user registration csv file
            #This allows for no incorrect entry of one's username to someone else's password
            if entered_username == username and entered_password == password:
                # If a match is found, it sets the current user
                self.controller.current_user = entered_username

                # Displays a success message
                messagebox.showinfo("Success", "Login Successful!")

                # Clears the username and password entry fields
                self.username_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')

                if entered_username in self.controller.user_frames:
                    # If the user's frame already exists, simply shows it
                    DCM_Interface = self.controller.user_frames[entered_username]
                    self.controller.container.pack_forget()  # Hides the login page container
                    DCM_Interface.pack(fill="both", expand=True)  # Packs the PacemakerGUI inside its container

                else:
                    # Create an instance of the PacemakerGUI
                    DCM_Interface = PacemakerGUI(self.controller.container, self.controller, entered_username)
                    #Adds the instance to the frames dictionary
                    self.controller.user_frames[entered_username] = DCM_Interface
                    #Diplays the interface using all available space
                    DCM_Interface.pack(fill="both", expand=True)

                # Hide the login page
                self.pack_forget()

                user_found = True
                break

        if not user_found:
            # If no matching user is found, show an error message
            messagebox.showerror("Error", "Invalid username or password.")


    # Method to navigate to the welcome page
    def go_to_welcome_page(self):
        self.controller.show_welcome_page()

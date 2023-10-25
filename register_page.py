# GROUP 8

import os
import csv # Imports csv to allow for reading and writing csv files
# Imports the tkinter library for GUI development
import tkinter as tk

# Imports messagebox, username_arr, password_arr, save_user_data_to_csv, and load_user_data_from_csv from the user_registration_data module
from tkinter import messagebox #Allows for message boxes to be displayed
from user_registration_data import username_arr, password_arr, save_user_data_to_csv, load_user_data_from_csv

# Imports the PacemakerGUI class from the DCM_Interface module
from DCM_Interface import PacemakerGUI

# Creates a class named RegisterPage that inherits from tk.Frame
class RegisterPage(tk.Frame):
    def __init__(self, master, controller):
        # Initialize the RegisterPage class
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.setup_ui() #Set up the GUI

    def setup_ui(self):
        # Creates labels and entry boxes for the registration page to allow for username and password entry
        self.register_label = tk.Label(self, text="Registration", font=("Arial", 30))
        self.usernameReg_label = tk.Label(self, text="Username:", font=("Arial", 16))
        self.usernameReg_entry = tk.Entry(self, font=("Arial", 14))
        self.passwordReg_label = tk.Label(self, text="Password:", font=("Arial", 16))
        self.passwordReg_entry = tk.Entry(self, show="*", font=("Arial", 14))

        # Displays above widgets to certain area of the interface
        # 'news' represents north, east, west, south so news centers the label in the cell
        self.register_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20) 
        self.usernameReg_label.grid(row=1, column=0)
        self.usernameReg_entry.grid(row=1, column=1)
        self.passwordReg_label.grid(row=2, column=0)
        self.passwordReg_entry.grid(row=2, column=1)

        # Register Button which calls for the registration condition checker when clicked
        self.userRegister_button = tk.Button(self, text="Register", font=("Arial", 13), command=self.registration_check)
        # Back Button which calls for go_to_welcome_page function that takes users back to the home page when clicked
        self.back_button = tk.Button(self, text="Back to Welcome Page", font=("Arial", 13), command=self.go_to_welcome_page)

        # Displays Register button and back button on the screen
        self.userRegister_button.grid(row=4, column=0, columnspan=2, pady=30)
        self.back_button.grid(row=5, column=0, columnspan=2)

    # Checks if certain conditions are met for the user to successfully register
    def registration_check(self):
        entered_username = self.usernameReg_entry.get()
        entered_password = self.passwordReg_entry.get()

        # Checks for empty string in one or both of the input boxes
        if not entered_username or not entered_password:
            messagebox.showerror("Error", "Username and/or password cannot be empty.")
            return

        # Loads user registration data for further condition checks (shown below)
        load_user_data_from_csv()

        # Checks if the entered username is already registed since duplicate usernames are not allowed
        if entered_username in username_arr:
            messagebox.showerror("Error", "Username already taken.")
            return

        # Ensures a maximum of only 10 users are allowed to be registered at once
        if len(username_arr) >= 10:
            messagebox.showerror("Error", "Maximum number of users (10) reached.")
            return

        # If the entered username and password matches all the conditions it needs to, user registers successfully:
        messagebox.showinfo("Success", "You have been successfully registered!")
        # Add the new username and password to the lists
        username_arr.append(entered_username)
        password_arr.append(entered_password)

        # Update and save user data to the CSV file
        save_user_data_to_csv()

        # Create and initialize the parameter CSV file for the user 
        # Each user has their own csv file to save their specific DCM parameter values
        parameter_file_path = f"{entered_username}_data.csv" # Create csv file is named with the registered username in it's title
        if not os.path.exists(parameter_file_path):
            # The file doesn't exist, so it is created and initialized it with default values
            with open(parameter_file_path, mode='w', newline='') as parameter_file:

                # Headings for each parameter in the csv file
                fieldnames = [
                "LowerRateLimit_AOO", "UpperRateLimit_AOO", "AtrialAmp_AOO", "AtrialPulseWidth_AOO",
                "LowerRateLimit_VOO", "UpperRateLimit_VOO", "VentrAmp_VOO", "VentrPulseWidth_VOO",
                "LowerRateLimit_AAI", "UpperRateLimit_AAI", "AtrialAmp_AAI", "AtrialPulseWidth_AAI",
                "AtrialSens_AAI", "ARP_AAI", "PVARP_AAI", "Hyster_AAI", "RS_AAI",
                "LowerRateLimit_VVI", "UpperRateLimit_VVI", "VentrAmp_VVI", "VentrPulseWidth_VVI",
                "VentrSens_VVI", "VRP_VVI", "Hyster_VVI", "RS_VVI"
            ]
                # Sets default values to each DCM parameter
                writer = csv.DictWriter(parameter_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({
                    #AOO Parameters
                    "LowerRateLimit_AOO": 60,
                    "UpperRateLimit_AOO": 90,
                    "AtrialAmp_AOO": 0,
                    "AtrialPulseWidth_AOO": 1.8,

                    #VOO Parameters
                    "LowerRateLimit_VOO": 60,
                    "UpperRateLimit_VOO": 90,
                    "VentrAmp_VOO": 0,
                    "VentrPulseWidth_VOO": 1.8,

                    #AAI Parameters
                    "LowerRateLimit_AAI": 60,
                    "UpperRateLimit_AAI": 90,
                    "AtrialAmp_AAI": 0,
                    "AtrialPulseWidth_AAI": 1.8,
                    "AtrialSens_AAI": 0.5,
                    "ARP_AAI": 300,
                    "PVARP_AAI": 350,
                    "Hyster_AAI": 0,
                    "RS_AAI": 0,

                    #VVI Parameters
                    "LowerRateLimit_VVI": 60,
                    "UpperRateLimit_VVI": 90,
                    "VentrAmp_VVI": 0,
                    "VentrPulseWidth_VVI": 1.8,
                    "VentrSens_VVI": 0.5,
                    "VRP_VVI": 300,
                    "Hyster_VVI": 0,
                    "RS_VVI": 0
                })

        # Creates a user-specific PacemakerGUI
        DCM_Interface = PacemakerGUI(self.controller.container, self.controller, entered_username)

        # Stores the user's PacemakerGUI
        self.controller.user_pages[entered_username] = DCM_Interface

        # Hides the RegisterPage
        self.pack_forget()

        # Shows the user's unique PacemakerGUI
        DCM_Interface.pack(fill="both", expand=True)
        # Brings the DCM_Interface to the very front of the display
        DCM_Interface.tkraise()

    # Method to navigate to the welcome page
    def go_to_welcome_page(self):
        self.controller.show_welcome_page()
# GROUP 8

# Imports the tkinter library for GUI development
import tkinter as tk

# Imports the messagebox module for displaying pop-up messages
from tkinter import messagebox

# Imports the LoginPage, RegisterPage, and DeleteUserPage classes from their respective modules
from login_page import LoginPage
from register_page import RegisterPage
from delete_user_page import DeleteUserPage

# Creates a class named WelcomePage that inherits from tk.Frame
class WelcomePage(tk.Frame):
    def __init__(self, master, controller):
        # Initializes the WelcomePage class
        tk.Frame.__init__(self, master) #master is the widget that contains the frame

        # Stores a reference to the controller (GUI) that manages this page
        self.controller = controller

        # Packs the WelcomePage frame, filling both horizontally and vertically
        self.pack(fill=tk.BOTH, expand=True)

        # Creates a frame (center_frame) within the WelcomePage frame to center the content
        center_frame = tk.Frame(self)
        center_frame.pack(expand=True)

        # Creates a label widget displaying "Welcome" with Arial font and certain sizing
        welcome_label = tk.Label(center_frame, text="Welcome!", font=('Arial', 30))
        welcome_label.pack(pady=40)

        # Creates a frame (button_frame) to hold buttons horizontally
        button_frame = tk.Frame(center_frame)
        button_frame.pack()

        # Creates a "Login" button with specific text, font, and a command to go to the login page
        login_button = tk.Button(button_frame, text="Login", font=('Arial', 16), command=self.go_to_login)
        login_button.grid(row=0, column=0, padx=10)

        # Creates a "Register" button with specific text, font, and a command to go to the register page
        register_button = tk.Button(button_frame, text="Register", font=('Arial', 16), command=self.go_to_register)
        register_button.grid(row=0, column=1, padx=10)

        # Creates a "Delete My User" button with specific text, font, and a command to go to the delete user page
        delete_button = tk.Button(button_frame, text="Delete My User", font=('Arial', 16), command=self.go_to_delete_user)
        delete_button.grid(row=0, column=2, padx=10)

    # Method to navigate to the login page
    def go_to_login(self):
        self.controller.show_login_page()

    # Method to navigate to the register page
    def go_to_register(self):
        self.controller.show_register_page()

    # Method to navigate to the delete user page
    def go_to_delete_user(self):
        self.controller.show_delete_user_page()

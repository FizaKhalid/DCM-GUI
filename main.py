# GROUP 8

# Import the tkinter library for GUI development
import tkinter as tk

# Imports the different pages (WelcomePage, LoginPage, RegisterPage, DeleteUserPage) from their respective modules
from welcome_page import WelcomePage
from login_page import LoginPage
from register_page import RegisterPage
from delete_user_page import DeleteUserPage

# Create the main application class GUI, which inherits from tk.Tk
class GUI(tk.Tk): #Inheriting the Tk class from tk (tkinter)
    def __init__(self): #special method that gets called when an object of the class is created (it initializes the object's attributes and can perform other setup tasks)
        super().__init__() #allows the GUI class to have all the settings and features of the standard tk.Tk window (ensures GUI has all the necessary setup that tk.Tk has)

        # Set the title and initial window dimensions
        self.title("DCM")
        self.geometry('500x500')
        self.configure(bg='#333333')

        # Create a container frame to hold different pages
        self.container = tk.Frame(self)
        #Displays it on the screeen while filling all available space
        self.container.pack(fill="both", expand=True)

        # Dictionary to store different frames
        self.frames = {}
        # Create a dictionary to store user-specific pages
        self.user_frames = {}  
        # Create a dictionary to store user-specific UserPage instances
        self.user_pages = {}

        # Iterates through each necessary page class and creates an instance, storing it in the frames dictionary 
        for F in (WelcomePage, LoginPage, RegisterPage, DeleteUserPage):
            frame = F(self.container, self)
            self.frames[F] = frame

        self.current_frame = None  # Initializes the current_frame attribute

        # Initially displays the WelcomePage
        self.show_welcome_page()

    # Welcome page display
    def show_welcome_page(self):
        # Hides the current frame if it exists
        if self.current_frame:
            self.current_frame.pack_forget() 
        
        # Sets the current frame to the WelcomePage and displays it
        self.current_frame = self.frames[WelcomePage]
        frame = self.current_frame
        frame.pack(fill="both", expand=True)
        frame.tkraise() # Brings the current frame to the front (i.e. over the display)

    # Login page display
    def show_login_page(self):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame if it exists
        
        # Sets the current frame to the LoginPage and displays it
        self.current_frame = self.frames[LoginPage]
        frame = self.current_frame
        frame.pack()
        frame.tkraise() # Brings the current frame to the front (i.e. over the display)

    # Register page display
    def show_register_page(self):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hides the current frame if it exists
        
        # Sets the current frame to the RegisterPage and displays it
        self.current_frame = self.frames[RegisterPage]
        frame = self.current_frame
        frame.pack()
        frame.tkraise() # Brings the current frame to the front (i.e. over the display)

    # Delete User page display
    def show_delete_user_page(self):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hides the current frame if it exists
        
        # Sets the current frame to the DeleteUserPage and displays it
        self.current_frame = self.frames[DeleteUserPage]
        frame = self.current_frame
        frame.pack()
        frame.tkraise() # Brings the current frame to the front (i.e. over the display)

# Entry point for the application
if __name__ == "__main__":
    app = GUI()
    app.mainloop()

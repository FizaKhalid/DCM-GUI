# GROUP 8

# Import the CSV module for reading and writing CSV files
import csv

# Initializes two empty lists to store usernames and passwords
username_arr = []
password_arr = []

# Specifies the CSV file name to store user data
csv_file = 'user_registration_data.csv'  # CSV file to store user data

# Function to save user data to the CSV file
def save_user_data_to_csv():

    # Opens the CSV file in write mode, creating it if it doesn't exist, and ensuring no extra newline characters are added
    with open(csv_file, mode='w', newline='') as csvfile:
        # Defines the fieldnames for the CSV file
        fieldnames = ['Username', 'Password']
        # Creates a CSV DictWriter object with fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Writes the header row to the CSV file
        writer.writeheader()
        # Iterates over the username and password lists and write each pair to the CSV file
        for username, password in zip(username_arr, password_arr):
            writer.writerow({'Username': username, 'Password': password})

# Function to load user data from the CSV file
def load_user_data_from_csv():
    # Accesses the global username_arr and password_arr variables to modify them
    global username_arr
    global password_arr

    try:
        # Tries to open the CSV file in read mode
        with open(csv_file, mode='r') as csvfile:
            # Creates a CSV DictReader object to read the CSV file
            reader = csv.DictReader(csvfile)
            # Iterates over the rows in the CSV file
            for row in reader:
                # Appends the 'Username' and 'Password' values from each row to the respective lists
                username_arr.append(row['Username'])
                password_arr.append(row['Password'])

    except FileNotFoundError:
        # Handles the case where the file doesn't exist yet (no user data)
        pass

# GROUP 8

import os
import tkinter as tk # Imports the tkinter library for GUI development
from tkinter import ttk
from tkinter import IntVar, DoubleVar  # Import IntVar and DoubleVar
from tkinter import messagebox
import csv # Imports csv to allow for reading and writing csv files

#Creates the actual pacemaker interface
class PacemakerGUI(tk.Frame):
    #Creates parameters for user-specific data storage
    def __init__(self, parent, controller, entered_username):
        tk.Frame.__init__(self, parent)
        #Arguments initialization
        self.controller = controller
        self.username = entered_username
        self.parent = parent

        #AOO Parameter type Initialization
        self.lowerRateLimit_AOO = IntVar()
        self.upperRateLimit_AOO = IntVar()
        self.atrialAmp_AOO = DoubleVar()
        self.atrialPulseWidth_AOO = DoubleVar()
        
        #VOO Parameter type Initialization
        self.lowerRateLimit_VOO = IntVar()
        self.upperRateLimit_VOO = IntVar()
        self.ventrAmp_VOO = DoubleVar()
        self.ventrPulseWidth_VOO = DoubleVar()
        
        #AAI Parameter type Initialization
        self.lowerRateLimit_AAI = IntVar()
        self.upperRateLimit_AAI = IntVar()
        self.atrialAmp_AAI = DoubleVar()  
        self.atrialPulseWidth_AAI = DoubleVar()
        self.atrialSens_AAI = DoubleVar()
        self.ARP_AAI = IntVar()
        self.PVARP_AAI = IntVar()
        self.hyster_AAI = IntVar()
        self.RS_AAI = IntVar() #RS refers to Rate Smoothing
        
        #VVI Parameter type Initialization
        self.lowerRateLimit_VVI = IntVar()
        self.upperRateLimit_VVI = IntVar()
        self.ventrAmp_VVI = DoubleVar()    
        self.ventrPulseWidth_VVI = DoubleVar()
        self.ventrSens_VVI = DoubleVar()
        self.VRP_VVI = IntVar()
        self.hyster_VVI = IntVar()
        self.RS_VVI = IntVar() #RS refers to Rate Smoothing

        # Creates the notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)

        # Creates a tkinter style
        style = ttk.Style()

        # Configures the font size for tabs
        style.configure("TNotebook.Tab", font=("Arial", 20, "bold")) 

        # Creates tabs each pacing mode and serial communication
        self.tab_AOO = ttk.Frame(self.notebook)
        self.tab_VOO = ttk.Frame(self.notebook)
        self.tab_AAI = ttk.Frame(self.notebook)
        self.tab_VVI = ttk.Frame(self.notebook)
        self.tab_Ser_Conn = ttk.Frame(self.notebook) 

        # Add tabs to the notebook
        self.notebook.add(self.tab_AOO, text="  AOO  ")
        self.notebook.add(self.tab_VOO, text="  VOO  ")
        self.notebook.add(self.tab_AAI, text="  AAI  ")
        self.notebook.add(self.tab_VVI, text="  VVI  ")
        self.notebook.add(self.tab_Ser_Conn, text="  Egram Data  ")

        #Creates Configure settings button for each pacing mode and displays them to the interface using grid manager
        self.AOO_settings_button = tk.Button(self.tab_AOO, text="Configure AOO Mode Settings", font=("Arial", 15), command=self.AOO_InterfaceConfig)
        self.AOO_settings_button.grid(column=4, row=12, columnspan=5, padx=800, pady=332)
        self.VOO_settings_button = tk.Button(self.tab_VOO, text="Configure VOO Mode Settings", font=("Arial", 15), command=self.VOO_InterfaceConfig)
        self.VOO_settings_button.grid(column=4, row=12, columnspan=5, padx=752, pady=332)
        self.AAI_settings_button = tk.Button(self.tab_AAI, text="Configure AAI Mode Settings", font=("Arial", 15), command=self.AAI_InterfaceConfig)
        self.AAI_settings_button.grid(column=4, row=11, columnspan=5, padx=800)
        self.VVI_settings_button = tk.Button(self.tab_VVI, text="Configure VVI Mode Settings", font=("Arial", 15), command=self.VVI_InterfaceConfig)
        self.VVI_settings_button.grid(column=4, row=12, columnspan=5, padx=752, pady=67)

        #self.logout_button = tk.Button(self.tab_AOO, text="Logout", font=('Arial', 16), command=lambda: self.go_to_welcome_page).grid(column=1, row=8, padx=20, pady=20, sticky="e")
        
        #Creates temporary connection status labels to display in each pacing mode
        self.connection_label_AOO = tk.Label(self.tab_AOO, text="Status: No DCM connection detected", font=('Arial', 16)).grid(column=3, row=0, columnspan=5, padx=80)
        self.connection_label_VOO = tk.Label(self.tab_VOO, text="Status: No DCM connection detected", font=('Arial', 16)).grid(column=3, row=0, columnspan=5, padx=100)
        self.connection_label_AAI = tk.Label(self.tab_AAI, text="Status: No DCM connection detected", font=('Arial', 16)).grid(column=3, row=0, columnspan=5, padx=100)
        self.connection_label_VVI = tk.Label(self.tab_VVI, text="Status: No DCM connection detected", font=('Arial', 16)).grid(column=3, row=0, columnspan=5, padx=100)

        # Creates the Combobox widget to allow for a drop down menu
        ser_conn_dropdown = ttk.Combobox(self.tab_Ser_Conn, values=["No Connection"])
        ser_conn_dropdown.pack()  # Adjust the row and column as needed

        # Sets an initial value for future configuration
        ser_conn_dropdown.set("No Connection")

        # Creatse a Welcome label at the top of the page which welcomes the specific user using their username
        welcome_label = tk.Label(self, text=f"Welcome, {self.username}!", font=('Arial', 25))
        welcome_label.pack(fill="both", expand=False, padx=20)

        # Packs the notebook
        self.notebook.pack(fill="both", expand=True)

        # Loads user-specific parameters from the CSV file
        parameter_file_path = f"{entered_username}_data.csv"
        if os.path.exists(parameter_file_path):
            with open(parameter_file_path, mode='r', newline='') as parameter_file:
                reader = csv.DictReader(parameter_file)
                # Sets previously initialized variables to collect values based on their respective fieldnames in the csv file
                for row in reader:
                    #AOO Parameters
                    self.lowerRateLimit_AOO.set(int(row["LowerRateLimit_AOO"]))
                    self.upperRateLimit_AOO.set(int(row["UpperRateLimit_AOO"]))
                    self.atrialAmp_AOO.set(float(row["AtrialAmp_AOO"]))
                    self.atrialPulseWidth_AOO.set(float(row["AtrialPulseWidth_AOO"]))

                    #VOO Parameters
                    self.lowerRateLimit_VOO.set(int(row["LowerRateLimit_VOO"]))
                    self.upperRateLimit_VOO.set(int(row["UpperRateLimit_VOO"]))
                    self.ventrAmp_VOO.set(float(row["VentrAmp_VOO"]))
                    self.ventrPulseWidth_VOO.set(float(row["VentrPulseWidth_VOO"]))

                    #AAI Parameters   
                    self.lowerRateLimit_AAI.set(int(row["LowerRateLimit_AAI"]))
                    self.upperRateLimit_AAI.set(int(row["UpperRateLimit_AAI"]))
                    self.atrialAmp_AAI.set(float(row["AtrialAmp_AAI"]))
                    self.atrialPulseWidth_AAI.set(float(row["AtrialPulseWidth_AAI"]))
                    self.atrialSens_AAI.set(float(row["AtrialSens_AAI"]))
                    self.ARP_AAI.set(int(row["ARP_AAI"]))
                    self.PVARP_AAI.set(int(row["PVARP_AAI"]))
                    self.hyster_AAI.set(int(row["Hyster_AAI"]))
                    self.RS_AAI.set(int(row["RS_AAI"]))  

                    #VVI Parameters
                    self.lowerRateLimit_VVI.set(int(row["LowerRateLimit_VVI"]))
                    self.upperRateLimit_VVI.set(int(row["UpperRateLimit_VVI"]))
                    self.ventrAmp_VVI.set(float(row["VentrAmp_VVI"]))
                    self.ventrPulseWidth_VVI.set(float(row["VentrPulseWidth_VVI"]))       
                    self.ventrSens_VVI.set(float(row["VentrSens_VVI"]))
                    self.VRP_VVI.set(int(row["VRP_VVI"]))
                    self.hyster_VVI.set(int(row["Hyster_VVI"]))
                    self.RS_VVI.set(int(row["RS_VVI"]))  

        #Calls for the creation of all pacing modes
        self.create_AOO_tab()
        self.create_VOO_tab()
        self.create_AAI_tab()
        self.create_VVI_tab()

    #Creates a constantly modified AOO page
    def create_AOO_tab(self):
        
        # Sets and displays labels, values, and units for AOO's necessary parameters

        lowerRateLabel_AOO = ttk.Label(self.tab_AOO, text="Lower Rate Limit:", font=("Arial", 15)).grid(column=1, row=1, padx=20, pady=20, sticky="e")
        # Collects the Lower rate value to modify the current variable
        lowerRateValue_AOO = ttk.Label(self.tab_AOO, text=self.lowerRateLimit_AOO.get(), font=("Arial", 15)).grid(column=2, row=1, padx=20, pady=20)
        lowerRateUnit_AOO = ttk.Label(self.tab_AOO, text="ppm", font=("Arial", 15)).grid(column=3, row=1, padx=20, pady=20, sticky="w")

        upperRateLabel_AOO = ttk.Label(self.tab_AOO, text="Upper Rate Limit:", font=("Arial", 15)).grid(column=1, row=2, padx=20, pady=20, sticky="e")
        # Collects the Upper rate value to modify the current variable
        upperRateValue_AOO = ttk.Label(self.tab_AOO, text=self.upperRateLimit_AOO.get(), font=("Arial", 15)).grid(column=2, row=2, padx=20, pady=20)
        upperRateUnit_AOO = ttk.Label(self.tab_AOO, text="ppm", font=("Arial", 15)).grid(column=3, row=2, padx=20, pady=20, sticky="w")

        atrialAmpLabel_AOO = ttk.Label(self.tab_AOO, text="Atrial Amplitude:", font=("Arial", 15)).grid(column=1, row=3, padx=20, pady=20, sticky="e")
        # Collects the Atrial Amplitude value to modify the current variable
        atrialAmpValue_AOO = ttk.Label(self.tab_AOO, text=self.atrialAmp_AOO.get(), font=("Arial", 15)).grid(column=2, row=3, padx=20, pady=20)
        atrialAmpUnit_AOO = ttk.Label(self.tab_AOO, text="V", font=("Arial", 15)).grid(column=3, row=3, padx=20, pady=20, sticky="w")

        atrialPulseLabel_AOO = ttk.Label(self.tab_AOO, text="Atrial Pulse Width:", font=("Arial", 15)).grid(column=1, row=4, padx=20, pady=20, sticky="e")
        # Collects the Atrial Pulse Width value to modify the current variable
        atrialPulseValue_AOO = ttk.Label(self.tab_AOO, text=self.atrialPulseWidth_AOO.get(), font=("Arial", 15)).grid(column=2, row=4, padx=20, pady=20)
        atrialPulseUnit_AOO = ttk.Label(self.tab_AOO, text="ms", font=("Arial", 15)).grid(column=3, row=4, padx=20, pady=20, sticky="w")

    #Creates a constantly modified VOO page
    def create_VOO_tab(self):

        # Sets and displays labels, values, and units for VOO's necessary parameters

        lowerRateLabel_VOO = ttk.Label(self.tab_VOO, text="Lower Rate Limit:", font=("Arial", 15)).grid(column=1, row=1, padx=20, pady=20, sticky="e")
        # Collects the Lower rate value to modify the current variable
        lowerRateValue_VOO = ttk.Label(self.tab_VOO, text=self.lowerRateLimit_VOO.get(), font=("Arial", 15)).grid(column=2, row=1, padx=20, pady=20)
        lowerRateUnit_VOO = ttk.Label(self.tab_VOO, text="ppm", font=("Arial", 15)).grid(column=3, row=1, padx=20, pady=20, sticky="w")

        upperRateLabel_VOO = ttk.Label(self.tab_VOO, text="Upper Rate Limit:", font=("Arial", 15)).grid(column=1, row=2, padx=20, pady=20, sticky="e")
        # Collects the Upper rate value to modify the current variable
        upperRateValue_VOO = ttk.Label(self.tab_VOO, text=self.upperRateLimit_VOO.get(), font=("Arial", 15)).grid(column=2, row=2, padx=20, pady=20)
        upperRateUnit_VOO = ttk.Label(self.tab_VOO, text="ppm", font=("Arial", 15)).grid(column=3, row=2, padx=20, pady=20, sticky="w")

        ventrAmpLabel_VOO = ttk.Label(self.tab_VOO, text="Ventricular Amplitude:", font=("Arial", 15)).grid(column=1, row=3, padx=20, pady=20, sticky="e")
        # Collects the Ventricular Amplitude value to modify the current variable
        ventrAmpValue_VOO = ttk.Label(self.tab_VOO, text=self.ventrAmp_VOO.get(), font=("Arial", 15)).grid(column=2, row=3, padx=20, pady=20)
        ventrAmpUnit_VOO = ttk.Label(self.tab_VOO, text="V", font=("Arial", 15)).grid(column=3, row=3, padx=20, pady=20, sticky="w")

        ventrPulseLabel_VOO = ttk.Label(self.tab_VOO, text="Ventricular Pulse Width:", font=("Arial", 15)).grid(column=1, row=4, padx=20, pady=20, sticky="e")
        # Collects the Ventricular Pulse Width value to modify the current variable
        ventrPulseValue_VOO = ttk.Label(self.tab_VOO, text=self.ventrPulseWidth_VOO.get(), font=("Arial", 15)).grid(column=2, row=4, padx=20, pady=20)
        ventrPulseUnit_VOO = ttk.Label(self.tab_VOO, text="ms", font=("Arial", 15)).grid(column=3, row=4, padx=20, pady=20, sticky="w")

    def create_AAI_tab(self):

        # Sets and displays labels, values, and units for AAI's necessary parameters

        lowerRateLabel_AAI = ttk.Label(self.tab_AAI, text="Lower Rate Limit:", font=("Arial", 15)).grid(column=1, row=1, padx=20, pady=20, sticky="e")
        # Collects the Lower rate value to modify the current variable
        lowerRateValue_AAI = ttk.Label(self.tab_AAI, text=self.lowerRateLimit_AAI.get(), font=("Arial", 15)).grid(column=2, row=1, padx=20, pady=20)
        lowerRateUnit_AAI = ttk.Label(self.tab_AAI, text="ppm", font=("Arial", 15)).grid(column=3, row=1, padx=20, pady=20, sticky="w")

        upperRateLabel_AAI = ttk.Label(self.tab_AAI, text="Upper Rate Limit:", font=("Arial", 15)).grid(column=1, row=2, padx=20, pady=20, sticky="e")
        # Collects the Upper rate value to modify the current variable
        upperRateValue_AAI = ttk.Label(self.tab_AAI, text=self.upperRateLimit_AAI.get(), font=("Arial", 15)).grid(column=2, row=2, padx=20, pady=20)
        upperRateUnit_AAI = ttk.Label(self.tab_AAI, text="ppm", font=("Arial", 15)).grid(column=3, row=2, padx=20, pady=20, sticky="w")

        atrialAmpLabel_AAI = ttk.Label(self.tab_AAI, text="Atrial Amplitude:", font=("Arial", 15)).grid(column=1, row=3, padx=20, pady=20, sticky="e")
        # Collects the Atrial Amplitude value to modify the current variable
        atrialAmpValue_AAI = ttk.Label(self.tab_AAI, text=self.atrialAmp_AAI.get(), font=("Arial", 15)).grid(column=2, row=3, padx=20, pady=20)
        atrialAmpUnit_AAI = ttk.Label(self.tab_AAI, text="V", font=("Arial", 15)).grid(column=3, row=3, padx=20, pady=20, sticky="w")

        atrialPulseLabel_AAI = ttk.Label(self.tab_AAI, text="Atrial Pulse Width:", font=("Arial", 15)).grid(column=1, row=4, padx=20, pady=20, sticky="e")
        # Collects the Atrial Pulse Width value to modify the current variable
        atrialPulseValue_AAI = ttk.Label(self.tab_AAI, text=self.atrialPulseWidth_AAI.get(), font=("Arial", 15)).grid(column=2, row=4, padx=20, pady=20)
        atrialPulseUnit_AAI = ttk.Label(self.tab_AAI, text="ms", font=("Arial", 15)).grid(column=3, row=4, padx=20, pady=20, sticky="w")
    
        atrialSensLabel_AAI = ttk.Label(self.tab_AAI, text="Atrial Sensitivity:", font=("Arial", 15)).grid(column=1, row=5, padx=20, pady=20, sticky="e")
        # Collects the Atrial Sensitive value to modify the current variable
        atrialSensValue_AAI = ttk.Label(self.tab_AAI, text=self.atrialSens_AAI.get(), font=("Arial", 15)).grid(column=2, row=5, padx=20, pady=20)
        atrialSensUnit_AAI = ttk.Label(self.tab_AAI, text="mV", font=("Arial", 15)).grid(column=3, row=5, padx=20, pady=20, sticky="w")

        ARPLabel_AAI = ttk.Label(self.tab_AAI, text="ARP:", font=("Arial", 15)).grid(column=1, row=6, padx=20, pady=20, sticky="e")
        # Collects the ARP value to modify the current variable
        ARPValue_AAI = ttk.Label(self.tab_AAI, text=self.ARP_AAI.get(), font=("Arial", 15)).grid(column=2, row=6, padx=20, pady=20)
        ARPUnit_AAI = ttk.Label(self.tab_AAI, text="ms", font=("Arial", 15)).grid(column=3, row=6, padx=20, pady=20, sticky="w")

        PVARPLabel_AAI = ttk.Label(self.tab_AAI, text="PVARP:", font=("Arial", 15)).grid(column=1, row=7, padx=20, pady=20, sticky="e")
        # Collects the PVARP value to modify the current variable
        PVARPValue_AAI = ttk.Label(self.tab_AAI, text=self.PVARP_AAI.get(), font=("Arial", 15)).grid(column=2, row=7, padx=20, pady=20)
        PVARPUnit_AAI = ttk.Label(self.tab_AAI, text="ms", font=("Arial", 15)).grid(column=3, row=7, padx=20, pady=20, sticky="w")

        hysterLabel_AAI = ttk.Label(self.tab_AAI, text="Hysteresis:", font=("Arial", 15)).grid(column=1, row=8, padx=20, pady=20, sticky="e")
        # Collects the Hysteresis value to modify the current variable
        hysterValue_AAI = ttk.Label(self.tab_AAI, text=self.hyster_AAI.get(), font=("Arial", 15)).grid(column=2, row=8, padx=20, pady=20)
        hysterUnit_AAI = ttk.Label(self.tab_AAI, text="ms", font=("Arial", 15)).grid(column=3, row=8, padx=20, pady=20, sticky="w")

        RSLabel_AAI = ttk.Label(self.tab_AAI, text="Rate Smoothing:", font=("Arial", 15)).grid(column=1, row=9, padx=20, pady=20, sticky="e")
        # Collects the Rate Smoothing value to modify the current variable
        RSValue_AAI = ttk.Label(self.tab_AAI, text=self.RS_AAI.get(), font=("Arial", 15)).grid(column=2, row=9, padx=20, pady=20)
        RSUnit_AAI = ttk.Label(self.tab_AAI, text="%", font=("Arial", 15)).grid(column=3, row=9, padx=20, pady=20, sticky="w")


    def create_VVI_tab(self):

        # Sets and displays labels, values, and units for VVI's necessary parameters

        lowerRateLabel_VVI = ttk.Label(self.tab_VVI, text="Lower Rate Limit:", font=("Arial", 15)).grid(column=1, row=1, padx=20, pady=20, sticky="e")
        # Collects the Lower rate value to modify the current variable
        lowerRateValue_VVI = ttk.Label(self.tab_VVI, text=self.lowerRateLimit_VVI.get(), font=("Arial", 15)).grid(column=2, row=1, padx=20, pady=20)
        lowerRateUnit_VVI = ttk.Label(self.tab_VVI, text="ppm", font=("Arial", 15)).grid(column=3, row=1, padx=20, pady=20, sticky="w")

        upperRateLabel_VVI = ttk.Label(self.tab_VVI, text="Upper Rate Limit:", font=("Arial", 15)).grid(column=1, row=2, padx=20, pady=20, sticky="e")
        # Collects the Upper rate value to modify the current variable
        upperRateValue_VVI = ttk.Label(self.tab_VVI, text=self.upperRateLimit_VVI.get(), font=("Arial", 15)).grid(column=2, row=2, padx=20, pady=20)
        upperRateUnit_VVI = ttk.Label(self.tab_VVI, text="ppm", font=("Arial", 15)).grid(column=3, row=2, padx=20, pady=20, sticky="w")

        ventrAmpLabel_VVI = ttk.Label(self.tab_VVI, text="Ventricular Amplitude:", font=("Arial", 15)).grid(column=1, row=3, padx=20, pady=20, sticky="e")
        # Collects the Ventricular Amplitude value to modify the current variable
        ventrAmpValue_VVI = ttk.Label(self.tab_VVI, text=self.ventrAmp_VVI.get(), font=("Arial", 15)).grid(column=2, row=3, padx=20, pady=20)
        ventrAmpUnit_VVI = ttk.Label(self.tab_VVI, text="V", font=("Arial", 15)).grid(column=3, row=3, padx=20, pady=20, sticky="w")

        ventrPulseLabel_VVI = ttk.Label(self.tab_VVI, text="Ventricular Pulse Width:", font=("Arial", 15)).grid(column=1, row=4, padx=20, pady=20, sticky="e")
        # Collects the Ventricular Pulse Width value to modify the current variable
        ventrPulseValue_VVI = ttk.Label(self.tab_VVI, text=self.ventrPulseWidth_VVI.get(), font=("Arial", 15)).grid(column=2, row=4, padx=20, pady=20)
        ventrPulseUnit_VVI = ttk.Label(self.tab_VVI, text="ms", font=("Arial", 15)).grid(column=3, row=4, padx=20, pady=20, sticky="w")
    
        ventrSensLabel_VVI = ttk.Label(self.tab_VVI, text="Ventricular Sensitivity:", font=("Arial", 15)).grid(column=1, row=5, padx=20, pady=20, sticky="e")
        # Collects the Ventricular Sensitive value to modify the current variable
        ventrSensValue_VVI = ttk.Label(self.tab_VVI, text=self.ventrSens_VVI.get(), font=("Arial", 15)).grid(column=2, row=5, padx=20, pady=20)
        ventrSensUnit_VVI = ttk.Label(self.tab_VVI, text="mV", font=("Arial", 15)).grid(column=3, row=5, padx=20, pady=20, sticky="w")

        VRPLabel_VVI = ttk.Label(self.tab_VVI, text="VRP:", font=("Arial", 15)).grid(column=1, row=6, padx=20, pady=20, sticky="e")
        # Collects the VRP value to modify the current variable
        VRPValue_VVI = ttk.Label(self.tab_VVI, text=self.VRP_VVI.get(), font=("Arial", 15)).grid(column=2, row=6, padx=20, pady=20)
        VRPUnit_VVI = ttk.Label(self.tab_VVI, text="ms", font=("Arial", 15)).grid(column=3, row=6, padx=20, pady=20, sticky="w")

        hysterLabel_VVI = ttk.Label(self.tab_VVI, text="Hysteresis:", font=("Arial", 15)).grid(column=1, row=7, padx=20, pady=20, sticky="e")
        # Collects the Hysteresis value to modify the current variable
        hysterValue_VVI = ttk.Label(self.tab_VVI, text=self.hyster_VVI.get(), font=("Arial", 15)).grid(column=2, row=7, padx=20, pady=20)
        hysterUnit_VVI = ttk.Label(self.tab_VVI, text="ms", font=("Arial", 15)).grid(column=3, row=7, padx=20, pady=20, sticky="w")

        RSLabel_VVI = ttk.Label(self.tab_VVI, text="Rate Smoothing:", font=("Arial", 15)).grid(column=1, row=8, padx=20, pady=20, sticky="e")
        # Collects the Rate Smoothing value to modify the current variable
        RSValue_VVI = ttk.Label(self.tab_VVI, text=self.RS_VVI.get(), font=("Arial", 15)).grid(column=2, row=8, padx=20, pady=20)
        RSUnit_VVI = ttk.Label(self.tab_VVI, text="%", font=("Arial", 15)).grid(column=3, row=8, padx=20, pady=20, sticky="w")

    # Saves the modified or un-modified values and updates the parameter values with them in the user-specific DCM csv file
    def save_settings(self):
        # Save the mode settings to the 'username'_data.csv file
        settings = {

            # AOO Parameters
            "LowerRateLimit_AOO": self.lowerRateLimit_AOO.get(),
            "UpperRateLimit_AOO": self.upperRateLimit_AOO.get(),
            "AtrialAmp_AOO": self.atrialAmp_AOO.get(),
            "AtrialPulseWidth_AOO": self.atrialPulseWidth_AOO.get(),

            # VOO Parameters
            "LowerRateLimit_VOO": self.lowerRateLimit_VOO.get(),
            "UpperRateLimit_VOO": self.upperRateLimit_VOO.get(),
            "VentrAmp_VOO": self.ventrAmp_VOO.get(),
            "VentrPulseWidth_VOO": self.ventrPulseWidth_VOO.get(),

            # AAI Parameters
            "LowerRateLimit_AAI": self.lowerRateLimit_AAI.get(),
            "UpperRateLimit_AAI": self.upperRateLimit_AAI.get(),
            "AtrialAmp_AAI": self.atrialAmp_AAI.get(),
            "AtrialPulseWidth_AAI": self.atrialPulseWidth_AAI.get(),
            "AtrialSens_AAI": self.atrialSens_AAI.get(),
            "ARP_AAI": self.ARP_AAI.get(),
            "PVARP_AAI": self.PVARP_AAI.get(),
            "Hyster_AAI": self.hyster_AAI.get(),
            "RS_AAI": self.RS_AAI.get(),

            # VVI Parameters
            "LowerRateLimit_VVI": self.lowerRateLimit_VVI.get(),
            "UpperRateLimit_VVI": self.upperRateLimit_VVI.get(),
            "VentrAmp_VVI": self.ventrAmp_VVI.get(),
            "VentrPulseWidth_VVI": self.ventrPulseWidth_VVI.get(),
            "VentrSens_VVI": self.ventrSens_VVI.get(),
            "VRP_VVI": self.VRP_VVI.get(),
            "Hyster_VVI": self.hyster_VVI.get(),
            "RS_VVI": self.RS_VVI.get()
        }

        # Writes the updated values under their respective field names in the user-specific DCM csv file
        parameter_file_path = f"{self.username}_data.csv"

        with open(parameter_file_path, mode='w', newline='') as file:
            fieldnames = [
                "LowerRateLimit_AOO", "UpperRateLimit_AOO", "AtrialAmp_AOO", "AtrialPulseWidth_AOO",
                "LowerRateLimit_VOO", "UpperRateLimit_VOO", "VentrAmp_VOO", "VentrPulseWidth_VOO",
                "LowerRateLimit_AAI", "UpperRateLimit_AAI", "AtrialAmp_AAI", "AtrialPulseWidth_AAI",
                "AtrialSens_AAI", "ARP_AAI", "PVARP_AAI", "Hyster_AAI", "RS_AAI",
                "LowerRateLimit_VVI", "UpperRateLimit_VVI", "VentrAmp_VVI", "VentrPulseWidth_VVI",
                "VentrSens_VVI", "VRP_VVI", "Hyster_VVI", "RS_VVI"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(settings)


    # Loads the values from the user-specific file to allow for display
    def load_settings(self):
        # Load the settings from the user-specific CSV file if it exists
        parameter_file_path = f"{self.username}_data.csv"
        if os.path.exists(parameter_file_path):
            with open(parameter_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                settings = next(reader, None)

                if settings is not None:
                    # AOO Parameters
                    self.lowerRateLimit_AOO.set(int(settings["LowerRateLimit_AOO"]))
                    self.upperRateLimit_AOO.set(int(settings["UpperRateLimit_AOO"]))
                    self.atrialAmp_AOO.set(float(settings["AtrialAmp_AOO"]))
                    self.atrialPulseWidth_AOO.set(float(settings["AtrialPulseWidth_AOO"]))

                    # VOO Parameters
                    self.lowerRateLimit_VOO.set(int(settings["LowerRateLimit_VOO"]))
                    self.upperRateLimit_VOO.set(int(settings["UpperRateLimit_VOO"]))
                    self.ventrAmp_VOO.set(float(settings["VentrAmp_VOO"]))
                    self.ventrPulseWidth_VOO.set(float(settings["VentrPulseWidth_VOO"]))

                    # AAI Parameters
                    self.lowerRateLimit_AAI.set(int(settings["LowerRateLimit_AAI"]))
                    self.upperRateLimit_AAI.set(int(settings["UpperRateLimit_AAI"]))
                    self.atrialAmp_AAI.set(float(settings["AtrialAmp_AAI"]))
                    self.atrialPulseWidth_AAI.set(float(settings["AtrialPulseWidth_AAI"]))
                    self.atrialSens_AAI.set(float(settings["AtrialSens_AAI"]))
                    self.ARP_AAI.set(int(settings["ARP_AAI"]))
                    self.PVARP_AAI.set(int(settings["PVARP_AAI"]))
                    self.hyster_AAI.set(int(settings["Hyster_AAI"]))
                    self.RS_AAI.set(int(settings["RS_AAI"]))

                    # VVI Parameters
                    self.lowerRateLimit_VVI.set(int(settings["LowerRateLimit_VVI"]))
                    self.upperRateLimit_VVI.set(int(settings["UpperRateLimit_VVI"]))
                    self.ventrAmp_VVI.set(float(settings["VentrAmp_VVI"]))
                    self.ventrPulseWidth_VVI.set(float(settings["VentrPulseWidth_VVI"]))
                    self.ventrSens_VVI.set(float(settings["VentrSens_VVI"]))
                    self.VRP_VVI.set(int(settings["VRP_VVI"]))
                    self.hyster_VVI.set(int(settings["Hyster_VVI"]))
                    self.RS_VVI.set(int(settings["RS_VVI"]))


    # Sets up entry boxes and adjusts parameter values if user decides to click the "Configure AOO mode settings" button
    def AOO_InterfaceConfig(self):
        # Config menu to edit parameters for the AOO Pacemaker mode

        #Removes the "Configure AOO mode settings" button
        self.AOO_settings_button.destroy()

        # Validates all entries to only allow numbers or "." entries
        reg = self.tab_AOO.register(self.validateInput)

        #Creates Input boxes for each AOO parameter and saves them to their respective parameters for parameter condition checking in AOO_ConfigConfirm

        self.lowerRateInput_AOO = ttk.Entry(self.tab_AOO, textvariable=self.lowerRateLimit_AOO, font=("Arial", 13), justify='center')
        self.lowerRateInput_AOO.grid(column=2, row=1, padx=20, pady=20)
        self.lowerRateInput_AOO.config(validate="key", validatecommand=(reg, "%P")) # %P is a special substitution string that represents the value of the widget after the edit

        self.upperRateInput_AOO = ttk.Entry(self.tab_AOO, textvariable=self.upperRateLimit_AOO, font=("Arial", 13), justify='center')
        self.upperRateInput_AOO.grid(column=2, row=2, padx=20, pady=20)
        self.upperRateInput_AOO.config(validate="key", validatecommand=(reg, "%P"))

        self.atrialAmpInput_AOO = ttk.Entry(self.tab_AOO, textvariable=self.atrialAmp_AOO, font=("Arial", 13), justify='center')
        self.atrialAmpInput_AOO.grid(column=2, row=3, padx=20, pady=20)
        self.atrialAmpInput_AOO.config(validate="key", validatecommand=(reg, "%P"))

        self.atrialPulseInput_AOO = ttk.Entry(self.tab_AOO, textvariable=self.atrialPulseWidth_AOO, font=("Arial", 13), justify='center')
        self.atrialPulseInput_AOO.grid(column=2, row=4, padx=20, pady=20)
        self.atrialPulseInput_AOO.config(validate="key", validatecommand=(reg, "%P"))

        # Creates a "Confirm Changes" button that called for the AOO_ConfigConfirm function to check if the entered parameters pass certain conditions
        self.confirmButton_AOO = tk.Button(self.tab_AOO, text="Confirm Changes", font=("Arial", 15), bg="white", command=self.AOO_ConfigConfirm)
        self.confirmButton_AOO.grid(column=4, row=12, columnspan=5, padx=800, pady=332)

    # Sets up entry boxes and adjusts parameter values if user decides to click the "Configure VOO mode settings" button
    def VOO_InterfaceConfig(self):
        # Config menu to edit parameters for the VOO Pacemaker mode

        #Removes the "Configure VOO mode settings" button
        self.VOO_settings_button.destroy()

        # Validates all entries to only allow numbers or "." entries
        reg = self.tab_VOO.register(self.validateInput)

        #Creates Input boxes for each VOO parameter and saves them to their respective parameters for parameter condition checking in VOO_ConfigConfirm

        self.lowerRateInput_VOO = ttk.Entry(self.tab_VOO, textvariable=self.lowerRateLimit_VOO, font=("Arial", 13), justify='center')
        self.lowerRateInput_VOO.grid(column=2, row=1, padx=20, pady=20)
        self.lowerRateInput_VOO.config(validate="key", validatecommand=(reg, "%P")) # %P is a special substitution string that represents the value of the widget after the edit

        self.upperRateInput_VOO = ttk.Entry(self.tab_VOO, textvariable=self.upperRateLimit_VOO, font=("Arial", 13), justify='center')
        self.upperRateInput_VOO.grid(column=2, row=2, padx=20, pady=20)
        self.upperRateInput_VOO.config(validate="key", validatecommand=(reg, "%P"))

        self.ventrAmpInput_VOO = ttk.Entry(self.tab_VOO, textvariable=self.ventrAmp_VOO, font=("Arial", 13), justify='center')
        self.ventrAmpInput_VOO.grid(column=2, row=3, padx=20, pady=20)
        self.ventrAmpInput_VOO.config(validate="key", validatecommand=(reg, "%P"))

        self.ventrPulseInput_VOO = ttk.Entry(self.tab_VOO, textvariable=self.ventrPulseWidth_VOO, font=("Arial", 13), justify='center')
        self.ventrPulseInput_VOO.grid(column=2, row=4, padx=20, pady=20)
        self.ventrPulseInput_VOO.config(validate="key", validatecommand=(reg, "%P"))

        # Creates a "Confirm Changes" button that called for the VOO_ConfigConfirm function to check if the entered parameters pass certain conditions
        self.confirmButton_VOO = tk.Button(self.tab_VOO, text="Confirm Changes", font=("Arial", 15), bg="white", command=self.VOO_ConfigConfirm)
        self.confirmButton_VOO.grid(column=4, row=12, columnspan=5, padx=752, pady=332)

    # Sets up entry boxes and adjusts parameter values if user decides to click the "Configure AAI mode settings" button
    def AAI_InterfaceConfig(self):
        # Config menu to edit parameters for the AAI Pacemaker mode

        #Removes the "Configure AAI mode settings" button
        self.AAI_settings_button.destroy()
        
        # Validates all entries to only allow numbers or "." entries
        reg = self.tab_AAI.register(self.validateInput)

        #Creates Input boxes for each AAI parameter and saves them to their respective parameters for parameter condition checking in AAI_ConfigConfirm

        self.lowerRateInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.lowerRateLimit_AAI, font=("Arial", 13), justify='center')
        self.lowerRateInput_AAI.grid(column=2, row=1, padx=20, pady=20)
        self.lowerRateInput_AAI.config(validate="key", validatecommand=(reg, "%P")) # %P is a special substitution string that represents the value of the widget after the edit

        self.upperRateInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.upperRateLimit_AAI, font=("Arial", 13), justify='center')
        self.upperRateInput_AAI.grid(column=2, row=2, padx=20, pady=20)
        self.upperRateInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        self.atrialAmpInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.atrialAmp_AAI, font=("Arial", 13), justify='center')
        self.atrialAmpInput_AAI.grid(column=2, row=3, padx=20, pady=20)
        self.atrialAmpInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        self.atrialPulseInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.atrialPulseWidth_AAI, font=("Arial", 13), justify='center')
        self.atrialPulseInput_AAI.grid(column=2, row=4, padx=20, pady=20)
        self.atrialPulseInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        self.atrialSensInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.atrialSens_AAI, font=("Arial", 13), justify='center')
        self.atrialSensInput_AAI.grid(column=2, row=5, padx=20, pady=20)
        self.atrialSensInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        self.ARPInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.ARP_AAI, font=("Arial", 13), justify='center')
        self.ARPInput_AAI.grid(column=2, row=6, padx=20, pady=20)
        self.ARPInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        self.PVARPInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.PVARP_AAI, font=("Arial", 13), justify='center')
        self.PVARPInput_AAI.grid(column=2, row=7, padx=20, pady=20)
        self.PVARPInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        self.hysterInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.hyster_AAI, font=("Arial", 13), justify='center')
        self.hysterInput_AAI.grid(column=2, row=8, padx=20, pady=20)
        self.hysterInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        self.RSInput_AAI = ttk.Entry(self.tab_AAI, textvariable=self.RS_AAI, font=("Arial", 13), justify='center')
        self.RSInput_AAI.grid(column=2, row=9, padx=20, pady=20)
        self.RSInput_AAI.config(validate="key", validatecommand=(reg, "%P"))

        # Creates a "Confirm Changes" button that called for the AAI_ConfigConfirm function to check if the entered parameters pass certain conditions
        self.confirmButton_AAI = tk.Button(self.tab_AAI, text="Confirm Changes", font=("Arial", 15), bg="white", command=self.AAI_ConfigConfirm)
        self.confirmButton_AAI.grid(column=4, row=11, columnspan=5, padx=800)

    # Sets up entry boxes and adjusts parameter values if user decides to click the "Configure VVI mode settings" button
    def VVI_InterfaceConfig(self):
        # Config menu to edit parameters for the VVI Pacemaker mode

        #Removes the "Configure VVI mode settings" button
        self.VVI_settings_button.destroy()

        # Validates all entries to only allow numbers or "." entries
        reg = self.tab_VVI.register(self.validateInput)

        #Creates Input boxes for each VVI parameter and saves them to their respective parameters for parameter condition checking in VVI_ConfigConfirm

        self.lowerRateInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.lowerRateLimit_VVI, font=("Arial", 13), justify='center')
        self.lowerRateInput_VVI.grid(column=2, row=1, padx=20, pady=20)
        self.lowerRateInput_VVI.config(validate="key", validatecommand=(reg, "%P")) # %P is a special substitution string that represents the value of the widget after the edit

        self.upperRateInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.upperRateLimit_VVI, font=("Arial", 13), justify='center')
        self.upperRateInput_VVI.grid(column=2, row=2, padx=20, pady=20)
        self.upperRateInput_VVI.config(validate="key", validatecommand=(reg, "%P"))

        self.ventrAmpInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.ventrAmp_VVI, font=("Arial", 13), justify='center')
        self.ventrAmpInput_VVI.grid(column=2, row=3, padx=20, pady=20)
        self.ventrAmpInput_VVI.config(validate="key", validatecommand=(reg, "%P")) 

        self.ventrPulseInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.ventrPulseWidth_VVI, font=("Arial", 13), justify='center')
        self.ventrPulseInput_VVI.grid(column=2, row=4, padx=20, pady=20)
        self.ventrPulseInput_VVI.config(validate="key", validatecommand=(reg, "%P"))

        self.ventrSensInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.ventrSens_VVI, font=("Arial", 13), justify='center')
        self.ventrSensInput_VVI.grid(column=2, row=5, padx=20, pady=20)
        self.ventrSensInput_VVI.config(validate="key", validatecommand=(reg, "%P"))

        self.VRPInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.VRP_VVI, font=("Arial", 13), justify='center')
        self.VRPInput_VVI.grid(column=2, row=6, padx=20, pady=20)
        self.VRPInput_VVI.config(validate="key", validatecommand=(reg, "%P"))

        self.hysterInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.hyster_VVI, font=("Arial", 13), justify='center')
        self.hysterInput_VVI.grid(column=2, row=7, padx=20, pady=20)
        self.hysterInput_VVI.config(validate="key", validatecommand=(reg, "%P"))

        self.RSInput_VVI = ttk.Entry(self.tab_VVI, textvariable=self.RS_VVI, font=("Arial", 13), justify='center')
        self.RSInput_VVI.grid(column=2, row=8, padx=20, pady=20)
        self.RSInput_VVI.config(validate="key", validatecommand=(reg, "%P"))

        # Creates a "Confirm Changes" button that called for the VVI_ConfigConfirm function to check if the entered parameters pass certain conditions
        self.confirmButton_VVI = tk.Button(self.tab_VVI, text="Confirm Changes", font=("Arial", 15), bg="white", command=self.VVI_ConfigConfirm)
        self.confirmButton_VVI.grid(column=4, row=12, columnspan=5, padx=752, pady=67)

    # Method used to validate user input
    def validateInput(self, input):
        # There should not be any string value input ever, therefore validation only checks for numerical input and "."

        try:
            if input:
                temp = int(input)   # Checks to see if string input can be typecasted to integer
            return True
        except ValueError:
            try:
                if input:
                    temp = float(input) # If string input cannot be typecasted to integer, checks to see if it can be typecasted to float
                return True
            except ValueError:
                messagebox.showerror("Input Error", "Error - Only numbers and '.' are accepted") # Otherwise, attempted input did not contain numbers or "." exclusively
                return False

    # Enforces AOO value limits, cleans up UI to prevent memory leaking, and updates values
    def AOO_ConfigConfirm(self):
        invalid = False

        # Checks if user's entered AOO parameters pass the certain ranges
        # Displays an error message if user's entry is out of range

        if (self.lowerRateLimit_AOO.get() < 30) or (self.lowerRateLimit_AOO.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Lower Rate Limit must be between 30-175 ppm")

        if (self.upperRateLimit_AOO.get() < 50) or (self.upperRateLimit_AOO.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Upper Rate Limit must be between 50-175 ppm")

        if (self.atrialAmp_AOO.get() < 3.5) or (self.atrialAmp_AOO.get() > 7.0):
            if (self.atrialAmp_AOO.get() < 0.5) or (self.atrialAmp_AOO.get() > 3.2):
                if (self.atrialAmp_AOO.get() != 0):
                    invalid = True
                    messagebox.showerror("Value Error", "Atrial Amplitude must be 0 for off or between 0.5 and 3.2 V or between 3.5 and 7.0 V")

        if (self.atrialPulseWidth_AOO.get() < 0.1 or self.atrialPulseWidth_AOO.get() > 1.9):
            if (self.atrialPulseWidth_AOO.get() != 0.05):
                invalid = True
                messagebox.showerror("Value Error", "Atrial Pulse Width must be 0.5 or between 0.1 and 1.9 ms")

        if invalid:
            # Does nothing on invalid input to force the user to correct the error
            pass

        # If entered values are within parameter ranges:
        else:
            # Updates the AOO tab
            self.tab_AOO.update()
            # Updates values in the user's specific DCM values csv file
            self.save_settings()
            # Recreates the AOO page with labels and updated values
            self.create_AOO_tab()

            # Recreates the "Configure AOO Mode Settings" button
            self.AOO_settings_button = tk.Button(self.tab_AOO, text="Configure AOO Mode Settings", font=("Arial", 15), command=self.AOO_InterfaceConfig)
            self.AOO_settings_button.grid(column=4, row=12, columnspan=5, padx=800, pady=332)

            # Destroys the entry boxes to allow for only label display
            self.lowerRateInput_AOO.destroy()
            self.upperRateInput_AOO.destroy()
            self.atrialAmpInput_AOO.destroy()
            self.atrialPulseInput_AOO.destroy()
            self.confirmButton_AOO.destroy()

    # Enforces VOO value limits, cleans up UI to prevent memory leaking, and updates values
    def VOO_ConfigConfirm(self):
        invalid = False

        # Checks if user's entered VOO parameters pass the certain ranges
        # Displays an error message if user's entry is out of range

        if (self.lowerRateLimit_VOO.get() < 30) or (self.lowerRateLimit_VOO.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Lower Rate Limit must be between 30-175 ppm")

        if (self.upperRateLimit_VOO.get() < 50) or (self.upperRateLimit_VOO.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Upper Rate Limit must be between 50-175 ppm")

        if (self.ventrAmp_VOO.get() < 3.5) or (self.ventrAmp_VOO.get() > 7.0):
            if (self.ventrAmp_VOO.get() < 0.5) or (self.ventrAmp_VOO.get() > 3.2):
                if (self.ventrAmp_VOO.get() != 0):
                    invalid = True
                    messagebox.showerror("Value Error", "Ventricular Amplitude must be 0 for off or between 0.5 and 3.2 V or between 3.5 and 7.0 V")
        
        if (self.ventrPulseWidth_VOO.get() < 0.1 or self.ventrPulseWidth_VOO.get() > 1.9):
            if (self.ventrPulseWidth_VOO.get() != 0.05):
                invalid = True
                messagebox.showerror("Value Error", "Ventricular Pulse Width must be 0.5 or between 0.1 and 1.9 ms")
        
        if invalid:
            # Does nothing on invalid input to force the user to correct the error
            pass

        # If entered values are within parameter ranges:    
        else:
            # Updates the VOO tab
            self.tab_VOO.update()
            # Updates values in the user's specific DCM values csv file
            self.save_settings()
            # Recreates the VOO page with labels and updated values
            self.create_VOO_tab()

            # Recreates the "Configure VOO Mode Settings" button
            self.VOO_settings_button = tk.Button(self.tab_VOO, text="Configure VOO Mode Settings", font=("Arial", 15), command=self.VOO_InterfaceConfig)
            self.VOO_settings_button.grid(column=4, row=12, columnspan=5, padx=752, pady=332)

            # Destroys the entry boxes to allow for only label display
            self.lowerRateInput_VOO.destroy()
            self.upperRateInput_VOO.destroy()
            self.ventrAmpInput_VOO.destroy()
            self.ventrPulseInput_VOO.destroy()
            self.confirmButton_VOO.destroy()

    # Enforces AAI value limits, cleans up UI to prevent memory leaking, and updates values
    def AAI_ConfigConfirm(self):
        invalid = False

        # Checks if user's entered VOO parameters pass the certain ranges
        # Displays an error message if user's entry is out of range

        if (self.lowerRateLimit_AAI.get() < 30) or (self.lowerRateLimit_AAI.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Lower Rate Limit must be between 30-175 ppm")
        
        if (self.upperRateLimit_AAI.get() < 50) or (self.upperRateLimit_AAI.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Upper Rate Limit must be between 50-175 ppm")
        
        if (self.atrialAmp_AAI.get() < 3.5) or (self.atrialAmp_AAI.get() > 7.0):
            if (self.atrialAmp_AAI.get() < 0.5) or (self.atrialAmp_AAI.get() > 3.2):
                if (self.atrialAmp_AAI.get() != 0):
                    invalid = True
                    messagebox.showerror("Value Error", "Atrial Amplitude must be 0 for off or between 0.5 and 3.2 V or between 3.5 and 7.0 V")
        
        if (self.atrialPulseWidth_AAI.get() < 0.1) or (self.atrialPulseWidth_AAI.get() > 1.9):
            if (self.atrialPulseWidth_AAI.get() != 0.05):
                invalid = True
                messagebox.showerror("Value Error", "Atrial Pulse Width must be 0.5 ms or between 0.1 and 1.9 ms")
        
        if (self.atrialSens_AAI.get() < 1.0) or (self.atrialSens_AAI.get() > 10):
            if (self.atrialSens_AAI.get() != 0.25) and (self.atrialSens_AAI.get() != 0.5) and (self.atrialSens_AAI.get() != 0.75):
                invalid = True
                messagebox.showerror("Value Error", "Atrial Sensitivity must be 0.25, 0.5, 0.75 mV or between 1.0 and 10 mV")
        
        if (self.ARP_AAI.get() < 150) or (self.ARP_AAI.get() > 500):
            invalid = True
            messagebox.showerror("Value Error", "ARP must be between 150 and 500 ms")
        
        if (self.PVARP_AAI.get() < 150) or (self.PVARP_AAI.get() > 500):
            invalid = True
            messagebox.showerror("Value Error", "PVARP must be between 150 and 500 ms")
        
        if (self.hyster_AAI.get() < 30) or (self.hyster_AAI.get() > 175):
            if (self.hyster_AAI.get() != 0):            
                invalid = True
                messagebox.showerror("Value Error", "Hysteresis must be 0 for off or between 30 and 175 ms")
        
        if (self.RS_AAI.get() != 0) and (self.RS_AAI.get() != 3) and (self.RS_AAI.get() != 6) and (self.RS_AAI.get() != 9 and (self.RS_AAI.get() != 12) and (self.RS_AAI.get() != 15) and (self.RS_AAI.get() != 18) and (self.RS_AAI.get() != 21) and (self.RS_AAI.get() != 25)):
            invalid = True
            messagebox.showerror("Value Error", "Rate Smoothing must be 0 for off or 3, 6, 9, 12, 15, 18, 21, or 25%")
        
        if invalid:
            # Does nothing on invalid input to force the user to correct the error
            pass

        # If entered values are within parameter ranges:    
        else:
            # Updates the AAI tab
            self.tab_AAI.update()
            # Updates values in the user's specific DCM values csv file
            self.save_settings()
            # Recreates the AAI page with labels and updated values
            self.create_AAI_tab()

            # Recreates the "Configure AAI Mode Settings" button
            self.AAI_settings_button = tk.Button(self.tab_AAI, text="Configure AAI Mode Settings", font=("Arial", 15), command=self.AAI_InterfaceConfig)
            self.AAI_settings_button.grid(column=4, row=11, columnspan=5, padx=800)

            # Destroys the entry boxes to allow for only label display
            self.lowerRateInput_AAI.destroy()
            self.upperRateInput_AAI.destroy()
            self.atrialAmpInput_AAI.destroy()
            self.atrialPulseInput_AAI.destroy()
            self.atrialSensInput_AAI.destroy()
            self.ARPInput_AAI.destroy()
            self.PVARPInput_AAI.destroy()
            self.hysterInput_AAI.destroy()
            self.RSInput_AAI.destroy()
            self.confirmButton_AAI.destroy()

    # Enforces VVI value limits, cleans up UI to prevent memory leaking, and updates values
    def VVI_ConfigConfirm(self):
        invalid = False

        # Checks if user's entered VOO parameters pass the certain ranges
        # Displays an error message if user's entry is out of range

        if (self.lowerRateLimit_VVI.get() < 30) or (self.lowerRateLimit_VVI.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Lower Rate Limit must be between 30-175 ppm")
        
        if (self.upperRateLimit_VVI.get() < 50) or (self.upperRateLimit_VVI.get() > 175):
            invalid = True
            messagebox.showerror("Value Error", "Upper Rate Limit must be between 50-175 ppm")
        
        if (self.ventrAmp_VVI.get() < 3.5) or (self.ventrAmp_VVI.get() > 7.0):
            if (self.ventrAmp_VVI.get() < 0.5) or (self.ventrAmp_VVI.get() > 3.2):
                if (self.ventrAmp_VVI.get() != 0):
                    invalid = True
                    messagebox.showerror("Value Error", "Ventricular Amplitude must be 0 for off or between 0.5 and 3.2 V or between 3.5 and 7.0 V")
        
        if (self.ventrPulseWidth_VVI.get() < 0.1 or self.ventrPulseWidth_VVI.get() > 1.9):
            if (self.ventrPulseWidth_VVI.get() != 0.05):
                invalid = True
                messagebox.showerror("Value Error", "Ventricular Pulse Width must be 0.5 ms or between 0.1 and 1.9 ms")
        
        if (self.ventrSens_VVI.get() < 1.0) or (self.ventrSens_VVI.get() > 10):
            if (self.ventrSens_VVI.get() != 0.25) and (self.ventrSens_VVI.get() != 0.5) and (self.ventrSens_VVI.get() != 0.75):
                invalid = True
                messagebox.showerror("Value Error", "Ventricular Sensitivity must be 0.25, 0.5, 0.75 mV or between 1.0 and 10 mV")
        
        if (self.VRP_VVI.get() < 150) or (self.VRP_VVI.get() > 500):
            invalid = True
            messagebox.showerror("Value Error", "VRP must be between 150 and 500 ms")
        
        if (self.hyster_VVI.get() < 30) or (self.hyster_VVI.get() > 175):
            if (self.hyster_VVI.get() != 0):            
                invalid = True
                messagebox.showerror("Value Error", "Hysteresis must be 0 for off or between 30 and 175 ms")
        
        if (self.RS_VVI.get() != 0) and (self.RS_VVI.get() != 3) and (self.RS_VVI.get() != 6) and (self.RS_VVI.get() != 9 and (self.RS_VVI.get() != 12) and (self.RS_VVI.get() != 15) and (self.RS_VVI.get() != 18) and (self.RS_VVI.get() != 21) and (self.RS_VVI.get() != 25)):
            invalid = True
            messagebox.showerror("Value Error", "Rate Smoothing must be 0 for off or 3, 6, 9, 12, 15, 18, 21, or 25%")
        
        if invalid:
            # Does nothing on invalid input to force the user to correct the error
            pass
        
        # If entered values are within parameter ranges:   
        else:
            # Updates the VVI tab
            self.tab_VVI.update()
            # Updates values in the user's specific DCM values csv file
            self.save_settings()
            # Recreates the VVI page with labels and updated values
            self.create_VVI_tab()

            # Recreates the "Configure VVI Mode Settings" button
            self.VVI_settings_button = tk.Button(self.tab_VVI, text="Configure VVI Mode Settings", font=("Arial", 15), command=self.VVI_InterfaceConfig)
            self.VVI_settings_button.grid(column=4, row=12, columnspan=5, padx=752, pady=67)

            # Destroys the entry boxes to allow for only label display
            self.lowerRateInput_VVI.destroy()
            self.upperRateInput_VVI.destroy()
            self.ventrAmpInput_VVI.destroy()
            self.ventrPulseInput_VVI.destroy()
            self.ventrSensInput_VVI.destroy()
            self.VRPInput_VVI.destroy()
            self.hysterInput_VVI.destroy()
            self.RSInput_VVI.destroy()
            self.confirmButton_VVI.destroy()

'''
    def go_to_welcome_page(self):
        self.controller.show_welcome_page()
'''

import tkinter as tk
from tkinter import messagebox
from math import pi


def help_click():
    messagebox.showinfo(
        "How To Use",
        "Enter the diameter and height of a water tower to calculate the volume, surface "
        "area, gallons of water it will hold, the weight of that water, and the head pressure."
    )


def about_click():
    messagebox.showinfo(
        "About",
        "Created by MrJ\n2024©"
    )


def calculate_properties(diameter_ft, diameter_in, height_ft, height_in):
    # Get values from entry fields
    diameter_feet = diameter_ft
    diameter_inches = diameter_in
    height_feet = height_ft
    height_inches = height_in

    # Convert inches to feet and calculate radius (ft)
    radius_feet = (diameter_feet + diameter_inches / 12) / 2

    # Convert inches to feet and calculate height (ft)
    height_feet = height_feet + height_inches / 12

    # Calculate volume, surface area, gallons of water, weight of water, head pressure
    volume = pi * (radius_feet ** 2) * height_feet
    surface_area = 2 * pi * (radius_feet ** 2) + 2 * pi * radius_feet * height_feet

    # Calculate number of gallons and weight of water in pounds
    gallons_of_water = volume * 7.48052
    weight_of_water_pounds = gallons_of_water * 8.330

    # Calculate head pressure
    head_pressure = height_feet / 2.31

    return volume, surface_area, gallons_of_water, weight_of_water_pounds, head_pressure


class WaterTowerCalculator:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()

        # Set the window title
        self.root.title("Water Works")

        # Set the window size
        self.root.geometry("500x680")

        # Create a help bar
        menu_bar = tk.Menu(
            self.root,
            background="#f0eaae",
            foreground="#17130d"
        )

        help_menu = tk.Menu(
            menu_bar,
            background="#f0eaae",
            foreground="#17130d",
            tearoff=0
        )

        help_menu.add_command(
            label='How To Use...',
            background="#f0eaae",
            foreground="#17130d",
            command=help_click
        )

        help_menu.add_command(
            label='About',
            background="#f0eaae",
            foreground="#17130d",
            command=about_click
        )

        menu_bar.add_cascade(
            label='Help',
            menu=help_menu
        )

        # Configure help menu bar
        self.root.config(menu=menu_bar)

        # Create frame for Water Works logo
        self.logo_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.logo_frame.pack(fill=tk.X)

        # Add to logo_frame
        photo = tk.PhotoImage(file="WaterWorks.png")
        self.image_label = tk.Label(
            self.logo_frame,
            image=photo,
            relief=tk.GROOVE,
            borderwidth=5,
            background="#719037",
            width=98,
            height=98
        )
        self.image_label.pack()

        # Create labels and entry fields for diameter (feet) and height (feet)

        self.diameter_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.diameter_frame.pack(fill=tk.X)

        self.diameter_label = tk.Label(
            self.diameter_frame,
            text="Diameter (ft):",
            font=("Baskerville", 14),
            background="#719037",
            foreground="#17130d",
            height=3
        )
        self.diameter_label.pack(side="left", fill=tk.X)

        self.diameter_feet_entry = tk.Entry(
            self.diameter_frame,
            font=("Baskerville", 14),
            background="#f0eaae",
            foreground="#17130d"
        )
        self.diameter_feet_entry.pack(side="right", fill=tk.X)
        self.diameter_feet_entry.insert(0, "0")

        self.diameter_frame2 = tk.Frame(
            self.root,
            background="#719037"
        )
        self.diameter_frame2.pack(fill=tk.X)

        # Create labels and entry fields for diameter (inches) and height (inches)
        self.diameter_inches_label = tk.Label(
            self.diameter_frame2,
            text="Diameter (in):",
            font=("Baskerville", 14),
            background="#719037",
            foreground="#17130d",
            height=3
        )
        self.diameter_inches_label.pack(side="left", fill=tk.X)

        self.diameter_inches_entry = tk.Entry(
            self.diameter_frame2,
            font=("Baskerville", 14),
            background="#f0eaae",
            foreground="#17130d"
        )
        self.diameter_inches_entry.pack(side="right", fill=tk.X)
        self.diameter_inches_entry.insert(0, "0")

        # Create frame for height
        self.height_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.height_frame.pack(fill=tk.X)

        self.height_feet_label = tk.Label(
            self.height_frame,
            text="Height (ft):",
            font=("Baskerville", 14),
            background="#719037",
            foreground="#17130d",
            height=3
        )
        self.height_feet_label.pack(side="left", fill=tk.X)

        self.height_feet_entry = tk.Entry(
            self.height_frame,
            font=("Baskerville", 14),
            background="#f0eaae",
            foreground="#17130d"
        )
        self.height_feet_entry.pack(side="right", fill=tk.X)
        self.height_feet_entry.insert(0, "0")

        self.height_frame2 = tk.Frame(
            self.root,
            background="#719037"
        )
        self.height_frame2.pack(fill=tk.X)

        self.height_inches_label = tk.Label(
            self.height_frame2,
            text="Height (in):",
            font=("Baskerville", 14),
            background="#719037",
            foreground="#17130d",
            height=3
        )
        self.height_inches_label.pack(side="left", fill=tk.X)

        self.height_inches_entry = tk.Entry(
            self.height_frame2,
            font=("Baskerville", 14),
            background="#f0eaae",
            foreground="#17130d"
        )
        self.height_inches_entry.pack(side="right", fill=tk.X)
        self.height_inches_entry.insert(0, "0")

        # Create labels for Results
        self.volume_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.volume_frame.pack(fill=tk.X)

        self.volume_label = tk.Label(
            self.volume_frame,
            text="\tVolume: ",
            background="#719037",
            foreground="#17130d",
            height=2
        )
        self.volume_label.pack(side="left", fill=tk.X)

        self.surface_area_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.surface_area_frame.pack(fill=tk.X)

        self.surface_area_label = tk.Label(
            self.surface_area_frame,
            text="\tSurface Area: ",
            background="#719037",
            foreground="#17130d",
            height=2
        )
        self.surface_area_label.pack(side="left", fill=tk.X)

        self.gallons_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.gallons_frame.pack(fill=tk.X)

        self.gallons_label = tk.Label(
            self.gallons_frame,
            text="\tGallons of Water: ",
            background="#719037",
            foreground="#17130d",
            height=2
        )
        self.gallons_label.pack(side="left", fill=tk.X)

        self.weight_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.weight_frame.pack(fill=tk.X)

        self.weight_label = tk.Label(
            self.weight_frame,
            text="\tWeight of Water: ",
            background="#719037",
            foreground="#17130d",
            height=2
        )
        self.weight_label.pack(side="left", fill=tk.X)

        self.head_pressure_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.head_pressure_frame.pack(fill=tk.X)

        self.head_pressure_label = tk.Label(
            self.head_pressure_frame,
            text="\tHead Pressure: ",
            background="#719037",
            foreground="#17130d",
            height=2
        )
        self.head_pressure_label.pack(side="left", fill=tk.X)

        # Create frame for buttons
        self.button_frame = tk.Frame(
            self.root,
            background="#719037"
        )
        self.button_frame.pack(fill=tk.X)

        # Create buttons for calculating and resetting
        self.calculate_button = tk.Button(
            self.button_frame,
            text="Calculate",
            command=self.calc_click,
            font=("gothic", 14),
            background="#f0eaae",
            relief=tk.RAISED,
            borderwidth=3,
            foreground="#17130d"
        )
        self.calculate_button.pack(side="bottom", fill=tk.X)

        self.reset_button = tk.Button(
            self.button_frame,
            text="Reset",
            command=self.reset_entries,
            font=("gothic", 14),
            background="#f0eaae",
            relief=tk.RAISED,
            borderwidth=3,
            foreground="#17130d"
        )
        self.reset_button.pack(side="left", fill=tk.X)

        self.exit_button = tk.Button(
            self.button_frame,
            text="Exit",
            command=self.root.destroy,
            font=("gothic", 14),
            background="#f0eaae",
            relief=tk.RAISED,
            borderwidth=3,
            foreground="#17130d"
        )
        self.exit_button.pack(side="right", fill=tk.X)

        # This is not an erroneous extra call, it is essential for image to display
        self.root.mainloop()

    def calc_click(self):
        # Get values from entry fields
        diameter_feet = float(self.diameter_feet_entry.get())
        diameter_inches = int(self.diameter_inches_entry.get())
        height_feet = float(self.height_feet_entry.get())
        height_inches = int(self.height_inches_entry.get())

        # Send to calculate_properties function
        volume, surface_area, gallons_of_water, weight_of_water_pounds, head_pressure = calculate_properties(
            diameter_feet, diameter_inches, height_feet, height_inches
        )

        # Display results
        self.volume_label.config(text=f"\tVolume: {volume.__format__(',')} cubic feet")
        self.surface_area_label.config(text=f"\tSurface Area: {surface_area.__format__(',')} sq. ft.")
        self.gallons_label.config(text=f"\tGallons of Water: {gallons_of_water.__format__(',')}")
        self.weight_label.config(text=f"\tWeight of Water: {weight_of_water_pounds.__format__(',')} lbs")
        self.head_pressure_label.config(text=f"\tHead Pressure: {head_pressure.__format__(',')} psi")

    def reset_entries(self):
        # Reset entry fields to empty
        self.diameter_feet_entry.delete(0, tk.END)
        self.diameter_feet_entry.insert(0, "0")

        self.diameter_inches_entry.delete(0, tk.END)
        self.diameter_inches_entry.insert(0, "0")

        self.height_feet_entry.delete(0, tk.END)
        self.height_feet_entry.insert(0, "0")

        self.height_inches_entry.delete(0, tk.END)
        self.height_inches_entry.insert(0, "0")

        self.volume_label.config(text="\tVolume: ")
        self.surface_area_label.config(text="\tSurface Area: ")
        self.gallons_label.config(text="\tGallons: ")
        self.weight_label.config(text="\tWeight of Water: ")
        self.head_pressure_label.config(text="\tHead Pressure: ")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calculator = WaterTowerCalculator()
    calculator.run()


import math
from datetime import datetime

# Get tire information from the user
width = float(input("Enter the width of the tire in mm (e.g. 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g. 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g. 15): "))

# Calculate the tire volume
volume = (math.pi * width ** 2 * aspect_ratio * 
          (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the tire volume
print(f"The approximate volume is {volume:.2f} liters")

# Get the current date
current_date = datetime.now().date()

# Save the information in a text file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

print("The tire information has been saved successfully.")

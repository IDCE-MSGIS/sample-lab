"""
Name: Banana McClane
Date created: 24-Jan-2020
Version of Python: 3.4
This script is for calculating rain run-off.
"""
original_length=50                      # The original length in feet.
plot_length=(original_length*12)        # Plot length in inches.
original_width=20                       # The original width in feet.

plot_width=(original_width*12)          # Plot width in inches.
plot_area=(plot_length*plot_width)      # Plot area in inches
rainfall_inches=1                       # Rainfall amount in inches
plot_volume=(plot_area*rainfall_inches) # Volume of the plot covered by 1-inch rainfall
runoff_gallons=(plot_volume*0.004329)   # Total runoff in gallons
runoff_gallons= round(runoff_gallons, 2)

# Final results

print ("plot_length is:"), plot_length, "inches"
print ("plot_width is:"), plot_width, "inches"
print ("rainfall inches is:"), rainfall_inches, "inch"
print ("runoff_gallons is:"), runoff_gallons


"""
Another way to comment the same code is as follows: 
"""

# Coded by Banana McClane
# Date created: 24-Jan-2020
# This script is for calculating rain run-off.

# Creating variables with values in feet and inches

original_length=50                      # feet
plot_length=(original_length*12)        # inches
original_width=20                       # feet

# These statements perform the calculations

plot_width=(original_width*12)          # Plot width in inches.
plot_area=(plot_length*plot_width)      # Plot area in inches
rainfall_inches=1                       # Rainfall amount in inches
plot_volume=(plot_area*rainfall_inches) # Volume of the plot covered by 1-inch rainfall
runoff_gallons=(plot_volume*0.004329)   # Total runoff in gallons
runoff_gallons= round(runoff_gallons, 2)

# Outputs

print ("plot_length is:"), plot_length, "inches"
print ("plot_width is:"), plot_width, "inches"
print ("rainfall inches is:"), rainfall_inches, "inch"
print ("runoff_gallons is:"), runoff_gallons

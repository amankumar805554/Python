## Introduction To Python

# Fill in the correct Python command to put “My first Python program” onto the screen
print("My first Python program")

# Convert this Bash command into Python:
# echo Have a nice day
print("Have a nice day")

# Fill in the correct Python commands to put “This is fun!” onto the screen 5 times.
for i in range(5):
     print("This is fun!")

# Select the Python code snippet that corresponds to the following Javascript snippet:
for i in range(10):
     print(i)

## Hello World
# Output a message that says "Programming in Python is fun!" to the screen.
print("Programming in Python is fun!")

# Replace the ___ placeholder and calculate the Golden ratio: (1 + √5)/2.
ratio = (1 + 5**(1/2))/2
print(ratio)

## Module 1 Graded Assessment
# Write a Python script that outputs "Automating with Python is fun!" to the screen.
print("Automating with Python is fun!")

# Fill in the blanks so that the code prints "Yellow is the color of sunshine".
color = 'Yellow'
thing = 'sunshine'
print(color + " is the color of " + thing)

# Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days. Print the result on the screen.
# Note: Your result should be in the format of just a number, not a sentence.
secondsInADay = 86400;
daysInAWeek = 7;
secondsInAWeek = secondsInADay * daysInAWeek
print(secondsInAWeek)

# Use Python to calculate how many different passwords can be formed with 6 lower case English letters. For a 1 letter password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities. Using this information, print the amount of possible passwords that can be formed with 6 letters.
print(26**6)

# Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.
# Note: Your result should be in the format of just a number, not a sentence.
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size/sector_size

print(sector_amount)
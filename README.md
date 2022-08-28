# **Python**
# **Crash Course on Python**
## **Coursera Python Quizzes**
**There're 6 Weeks, Each Topic has 5 Questions and 10 Questions in Graded Assessment**
1. Week 1 :- Hello Python!
>- [Introduction to Programming](#introduction-to-programming)
>- [Introduction to Python](#introduction-to-python)
>- [Hello World](#hello-world)
>- [Module 1 Graded Assessment](#module-1-graded-assessment)

2. Week 2 :- Basic Python Syntax
>- [Expressions and Variables](#expressions-and-variables)
>- [Functions](#functions)
>- [Conditionals](#conditionals)
>- [Module 2 Graded Assessment](#module-2-graded-assessment)

3. Week 3 :- Loops
>- [While Loops](#while-loops)
>- [For Loops](#for-loops)
>- [Recursion](#recursiom)
>- [Module 3 Graded Assessment](module-3-graded-assessment)

4. Week 4 : - Strings, Lists and Dictionaries
>- [Strings](#strings)
>- [Lists](#lists)
>- [Dictionaries](#dictionaries)
>- [Module 4 Graded Assessment](module-4-graded-assessment)

5. Week 5 :- Object Oriented Programming
>- [Object Oriented Programming](#object-oriented-programming)
>- [Classes and Methods](#classes-and-methods)
>- [Code Reuse](#code-reuse)
>- [Module 5 Graded Assessment](#module-5-graded-assessment)

6. Week 6 :- Final Project

# Week 1 :- Hello Python! Quiz
## Introduction to Programming

1. **What’s a computer program ?**

**Ans-**
```
    A list of instructions that the computer has to follow to reach a goal
```
2. **What’s the syntax of a language ?**

**Ans-**
```
    The rules of how to express things in that language
```
3. **What’s the difference between a program and a script ?**

**Ans-**
```
    There’s not much difference, but scripts are usually simpler and shorter.
```
4. **Which of these scenarios are good candidates for automation? Select all that apply.**

**Ans-**
```
    a. Generating a sales report, split by region and product type
    b. Copying a file to all computers in a company
    c. Sending personalized emails to subscribers of your website
```
5. **What are semantics when applied to programming code and pseudocode ?**

**Ans-**
```
     The effect the programming instructions have
```

## Introduction to Python

1. **Fill in the correct Python command to put “My first Python program” onto the screen.**

**Ans-**
```python
     print("My first Python program")
```
2. **Python is an example of what type of programming language ?**
   
**Ans-**
```
     General purpose scripting language
```
3. **Convert this Bash command into Python:**

**Ans-**
```python
     print("Have a nice day")
```
4. **Fill in the correct Python commands to put “This is fun!” onto the screen 5 times.**

**Ans-**
```python
     for i in range(5):
       print("This is fun!")
```
5. **Select the Python code snippet that corresponds to the following Javascript snippet:**

**Ans-**
```python
    for i in range(10):
       print(i)
```

## Hello World

1. **What are functions in Python ?**

**Ans-**
```
     Functions are pieces of code that perform a unit of work.
```
2. **What are keywords in Python ?**

**Ans-**
```
      Keywords are reserved words that are used to construct instructions.
```
3. **What does the print function do in Python ?**

**Ans-**
```
      The print function outputs messages to the screen
```
4. **Output a message that says "Programming in Python is fun!" to the screen.**

**Ans-**
```python
      print("Programming in Python is fun!")
```
5. **Replace the ___ placeholder and calculate the Golden ratio: (1 + √5)/2.**

**Ans-**
```python
      ratio = (1 + 5**(1/2))/2
        print(ratio)
```
## Module 1 Graded Assessment

1. **What is a computer program ?**

**Ans-**
```
      A step-by-step recipe of what needs to be done to complete a task, that gets executed by the computer.
```
2. **What’s automation ?**

**Ans-**
```
      The process of replacing a manual step with one that happens automatically.
```
3. **Which of the following tasks are good candidates for automation? Check all that apply.**

**Ans-**
```
    a. Creating a report of how much each sales person has sold in the last month.
    b. Setting the home directory and access permissions for new employees joining your company.
    c. Populating your company's e-commerce site with the latest products in the catalog.
```
4. **What are some characteristics of the Python programming language? Check all that apply.**

**Ans-**
```
     a. Python programs are easy to write and understand.
     b. The Python interpreter reads our code and transforms it into computer instructions.
     c. We can practice Python using web interpreters or codepads as well as executing it locally.
```
5. **How does Python compare to other programming languages ?**

**Ans-**
```
      Each programming language has its advantages and disadvantages.
```
6. **Write a Python script that outputs "Automating with Python is fun!" to the screen.**

**Ans-**
```python
      print("Automating with Python is fun!")
```
7. **Fill in the blanks so that the code prints "Yellow is the color of sunshine".**

**Ans-**
```python
      color = 'Yellow'
      thing = 'sunshine'
      print(color + " is the color of " + thing)
```
8. **Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days.  Print the result on the screen.**

   **Note: Your result should be in the format of just a number, not a sentence.**

**Ans-**
```python
       secondsInADay = 86400;
       daysInAWeek = 7;
       secondsInAWeek = secondsInADay * daysInAWeek
       print(secondsInAWeek)
```
9. **Use Python to calculate how many different passwords can be formed with 6 lower case English letters.  For a 1 letter password, there would be 26 possibilities.  For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  Using this information, print the amount of possible passwords that can be formed with 6 letters.**

**Ans-**
```python
       print(26**6)
```
10. **Most hard drives are divided into sectors of 512 bytes each.  Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.**

    **Note: Your result should be in the format of just a number, not a sentence.**

**Ans-**
```python
       disk_size = 16*1024*1024*1024
       sector_size = 512
       sector_amount = disk_size/sector_size

       print(sector_amount)
```

# Week 2 :- Basic Python Syntax
## Expressions and Variables

1. **In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.**

**Ans-**
```python
      bill = 47.28
      tip = bill * 0.15
      total = bill + tip
      share = 2
      print("Each person needs to pay: " + str(total / share))
```
2. **This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.**

**Ans-**
```python
      numerator = 10
      denominator = 10
      result = (numerator / denominator)
      print(result)
```
3. **Combine the variables to display the sentence "How do you like Python so far ?"**

**Ans-**
```python
      word1 = "How "
      word2 = "do "
      word3 = "you "
      word4 = "like "
      word5 = "Python "
      word6 = "so "
      word7 = "far? "
      sentence = word1 + word2 + word3 + word4 + word5 + word6 + word7
      print(sentence)
```
4. **This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.**

**Ans-**
```python
       print("2 + 2 = " + str(2 + 2))
```
5. **What do you call a combination of numbers, symbols, or other values that produce a result when evaluated ?**

**Ans-**
```
       An expression
```

## **Functions**

1. **This function converts miles to kilometers (km).**

      **1. Complete the function to return the result of the conversion**

      **2. Call the function to convert the trip distance from miles to kilometers**

      **3. Fill in the blank to print the result of the conversion**

      **4. Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result**

**Ans-**
```python
       # 1) Complete the function to return the result of the conversion
      def convert_distance(miles):
	      km = miles * 1.6  # approximately 1.6 km in 1 mile
	      return km

      my_trip_miles = 55

      # 2) Convert my_trip_miles to kilometers by calling the function above
      my_trip_km = 55 * 1.6

      # 3) Fill in the blank to print the result of the conversion
      print("The distance in kilometers is " + str(my_trip_km))

      # 4) Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

      round_trip = (my_trip_km)*2
      print("The round-trip in kilometers is " + str(round_trip))
```
2. **This function compares two numbers and returns them in increasing order.**

     **1. Fill in the blanks, so the print statement displays the result of the function call in order.**

      **Hint: if a function returns multiple values, don't forget to store these values in multiple variables**

**Ans-**
```python
      # This function compares two numbers and returns them
      # in increasing order.
      def order_numbers(number1, number2):
	      if number2 > number1:
		      return number1, number2
	      else:
		      return number2, number1

      # 1) Fill in the blanks so the print statement displays the result of the function call

      smaller, bigger = order_numbers(100, 99)
      print(smaller, bigger)
```
3. **What are the values passed into functions as input called ?**

**Ans-**
```    
      Parameters
```
4. **Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to complete the code to make it work.**

**Ans-**
```python
      def lucky_number(name):
            number = len(name) * 9
            message = "Hello " + name + ". Your lucky number is " + str(number)
            return message
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
```
5. **What is the purpose of the def keyword ?**

**Ans-**
```
      Used to define a new function
```
## **Conditionals**

1. **What's the value of this Python expression: (2 ** 2) == 4 ?**

**Ans-**
```
      True
```
2. **Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".**

**Ans-**
```python
      def greeting(name):
        if name == "Taylor":
          return "Welcome back Taylor!"
        else:
          return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
```
3. **What’s the output of this code if number equals 10 ?**

**Ans-**
```
      2
```
4. **Is "A dog" smaller or larger than "A mouse"? Is 9999+8888 smaller or larger than 100*100? Replace the plus sign in the following code to let Python check it for you and then answer.**

**Ans-**
```python
      print(len("A dog") > len("A mouse"))
      print(9999+8888 > 100*100)

      "A dog" is smaller than "A mouse" and 9999+8888 is larger than 100*100
```
5. **If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size ?**

**Ans-**
```python
      def calculate_storage(filesize):
          block_size = 4096
          # Use floor division to calculate how many blocks are fully occupied
          full_blocks = filesize // block_size
          # Use the modulo operator to check whether there's any remainder
          partial_block_remainder = filesize % block_size
          # Depending on whether there's a remainder or not, return
          # the total number of bytes required to allocate enough blocks
          # to store your data.
          if partial_block_remainder > 0:
            return 4096 * (full_blocks + 1)
          return 4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
```
## **Module 2 Graded Assessment**

1. **Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.**

**Ans-**
```python
      def color_translator(color):
            if color == "red":
	            hex_color = "#ff0000"
	      elif color == "green":
		      hex_color = "#00ff00"
	      elif color == "blue":
		      hex_color = "#0000ff"
	      else:
		      hex_color = "unknown"
	      return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
```
2. **What's the value of this Python expression: "big" > "small"**

**Ans-**
```
      False
```
3. **What is the elif keyword used for ?**

**Ans-**
``` 
      To handle more than two comparison cases
```
4. **Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.**

**Ans-**
```python
      def exam_grade(score):
	      if score > 95:
		      grade = "Top Score"
	      elif score >= 60:
		      grade = "Pass"
	      else:
		      grade = "Fail"
	      return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
```
5. **What's the value of this Python expression: 11 % 5 ?**

**Ans-**
```
      1
```
6. **Complete the body of the** ***format_name*** **function. This function receives the** ***first_name*** **and** ***last_name*** **parameters and then returns a properly formatted string.**

      **Specifically:**

      **If both the** ***last_name*** **and the** ***first_name*** **parameters are supplied, the function should return like so:**

**Ans-**
```python
      def format_name(first_name, last_name):
      	# code goes here
      	string = ("Name: " + last_name + ", " + first_name)
      	if first_name == "":
      		return("Name: " + last_name)
      	elif last_name == "":
      		return ("Name: " + first_name)
      	else:
      		return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"
```
7. **The** ***longest_word*** **function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen.**

**Ans-**
```python
      def longest_word(word1, word2, word3):
      	if len(word1) >= len(word2) and len(word1) >= len(word3):
      		word = word1
      	elif len(word2) >= len(word1) and len(word2) >= len(word3):
      		word = word2
      	else:
      		word = word3
      	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
```
8. **What’s the output of this code ?**

**Ans-**
```
      10
```
9. **What's the value of this Python expression ?**

**Ans-**
```
      True
```
10. **The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0** **and 1). Complete the body of the function so that it returns the right number.**
**Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.**

**Ans-**
```python
      def format_name(first_name, last_name):
      	# code goes here
      	string = 'Name: ' + ', '.join([name for name in [last_name, first_name] if name]) if any([last_name, first_name]) else ''
      	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
```

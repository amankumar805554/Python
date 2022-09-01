# **Python**
![Logo](../python/Logo/python%20logo.png)
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
>- [Recursion](#recursion)
>- [Module 3 Graded Assessment](#module-3-graded-assessment)

4. Week 4 : - Strings, Lists and Dictionaries
>- [Strings](#strings)
>- [Lists](#lists)
>- [Dictionaries](#dictionaries)
>- [Module 4 Graded Assessment](#module-4-graded-assessment)

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

# **Week 3 :- Loops**
## **While Loops**

1. **What are while loops in Python ?**

**Ans-**
```
      While loops let the computer execute a set of instructions while a condition is true.
```
2. **Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.**

**Ans-**
```python
      def print_prime_factors(number):
        # Start with two, which is the first prime
        factor = 2
        # Keep going until the factor is larger than the number
        while factor <= number:
          # Check if factor is a divisor of number
          if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
          else:
            # If it's not, increment the factor by one
            factor += 1
        return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
```
3. **The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.** <br>
**Note: Try running your function with the number 0 as the input, and see what you get!**

**Ans-**
```python
      def is_power_of_two(n):
        # Check if the number can be divided by two without a remainder
        while n % 2 == 0 and n!= 0:
          n = n / 2
        # If after dividing by two the number is 1, it's a power of two
         if n == 1:
          return True
          n += 1
        return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
```
4. **Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.**

**Ans-**
```python
      def sum_divisors(n):
        x = 1
        sum = 0
        # Return the sum of all divisors of n, not including n
        while x < n:
          if n % x == 0:
            sum += x
            x += 1
          else:
            x += 1
        return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
```
5. **The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. An additional requirement is that the result is not to exceed 25, which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions.**

**Ans-**
```python
      def multiplication_table(number):
      	# Initialize the starting point of the multiplication table
      	multiplier = 1
      	# Only want to loop through 5
      	while multiplier <= 5:
      		result = multiplier * number
      		# What is the additional condition to exit out of the loop?
      		if result > 25:
      			break
      		print(str(number) + "x" + str(multiplier) + "=" + str(result))
      		# Increment the variable for the loop
      		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24
```
# **For Loops**

1. **How are while loops and for loops different in Python ?**

**Ans-**
```
      While loops iterate while a condition is true, for loops iterate through a sequence of elements.
```
2. **Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.**

**Ans-**
```python
      def factorial(n):
          result = 1
          for x in range(1,n):
              result *= x
          return result

for n in range(0,10):
    print(n, factorial(n+1))
```
3. **Write a script that prints the first 10 cube numbers (x ** 3), starting with x=1 and ending with x=10.**

**Ans-**
```python
      for x in range(1, 11):
        print(x**3)
```
4. **Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.**

**Ans-**
```python
      number = 0
      multiplier = 7
      while number <= 100:
          print(number)
          number += multiplier
```
5. **The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.  Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.**

**Ans-**
```python
      def retry(operation, attempts):
        for n in range(attempts):
          if operation():
           print("Attempt " + str(n) + " succeeded")
            break
          else:
            print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)
```
# **Recursion**

1. **What is recursion used for ?**

**Ans-**
```
      Recursion lets us tackle complex problems by reducing the problem to a simpler one.
```
2. **Which of these activities are good use cases for recursive programs? Check all that apply.**

**Ans-**
```
      Going through a file system collecting information related to directories and files.

      Managing permissions assigned to groups inside a company, when each group can contain both subgroups and users.
```
3. **Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.**

**Ans-**
```python
      def is_power_of(number, base):
        # Base case: when number is smaller than base.
        if number < base:
          # If number is equal to 1, it's a power (base**0).
          return number == 1

        # Recursive case: keep dividing number by base.
        return is_power_of(number//base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
```
4. **The count_users function recursively counts the amount of users that belong to a group in the company system, by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members. But it has a bug! Can you spot the problem and fix it ?**

**Ans-**
```python
      def count_users(group):
        count = 0
        for member in get_members(group):
          if is_group(member):
            count += count_users(member)
          else:
            count += 1
        return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
```
5. **Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.**

**Ans-**
```python
      def sum_positive_numbers(n):
        if n == 0:
          return n
        return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
```
## **Module 3 Graded Assessment** 
<br>

1. **Fill in the blanks of this code to print out the numbers 1 through 7.**

**Ans-**
```python
      number = 1
      while number <= 7:
      	print(number, end=" ")
      	number += 1
```
2. **The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.**

**Ans-**
```python
      def show_letters(word):
      	for x in word:
      		print(x)

show_letters("Hello")
# Should print one line per letter
```
3. **Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.**

**Ans-**
```python
      def digits(n):
      	count = 0
      	if n == 0:
      	  return 1
      	while (n >= 1):
      		count += 1
      		n = n/10
      	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
```
4. **This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:**

      **1 2 3**

      **2 4 6** 

      **3 6 9**

**Ans-**
```python
      def multiplication_table(start, stop):
      	for x in range(start, stop+1):
      		for y in range(start, stop+1):
      			print(str(x*y), end=" ")
      		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
```
5. **The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.**

**Ans-**
```python
      def counter(start, stop):
      	x = start
      	if start > stop:
      		return_string = "Counting down: "
      		while x >= stop:
      			return_string += str(x)
      			if x > stop:
      				return_string += ","
      			x -= 1
      	else:
      		return_string = "Counting up: "
      		while x <= stop:
      			return_string += str(x)
      			if x < stop:
      				return_string += ","
      			x += 1
      	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
```
6. **The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.**

**Ans-**
```python
      def even_numbers(maximum):
      	return_string = ""
      	for x in [num for num in range(1, maximum+1) if num % 2 == 0]:
      		return_string += str(x) + " "
      	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
```
7. **The following code raises an error when executed. What's the reason for the error ?**

**Ans-**
```
      Failure to initialize variables
```
8. **What is the value of x at the end of the following code ?**

**Ans-**
```
      7
```
9. **What is the value of y at the end of the following code ?**

**Ans-**
```
     8
```
10. **How does this function need to be called to print yes, no, and maybe as possible options to vote for ?**

**Ans-**
```
      votes(['yes', 'no', 'maybe'])
```

# **Week 4 :- Strings, Lists & Dictionaries**
## **Strings**

1. **The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.**

**Ans-**
```python
      def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string.lower():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if letter.isalpha():
			new_string = new_string + letter
			reverse_string = letter + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
```
2. **Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".**

**Ans-**
```python
      def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
```
3. **If we have a string variable named Weather = "Rainfall", which of the following will print the substring or all characters before the "f" ?**

**Ans-**
```
print(Weather[:4])
```
4. **Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."**

**Ans-**
```python
def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 
```
5. **The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).**

**Ans-**
```python
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(old)
		new_sentence = sentence[:-i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
```
## **Lists**

1. **Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.**

**Ans-**
```python
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [file.replace(".hpp", ".h") for file in filenames]  

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
```
2. **Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.**

**Ans-**
```python
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    piglatinword = word[1:] + word[0] + "ay"
    say += " " + piglatinword
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
```
3. **The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.**
**For example:**
**640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be:** **"rw-r-----"**
**755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x".Fill in the blanks to make the code convert a permission in octal format into a string format.**

**Ans-**
```python
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
```
4. **Tuples and lists are very similar types of sequences. What is the main thing that makes a tuple different from a list ?**

**Ans-**
```
A tuple is immutable
```
5. **The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.**

**Ans-**
```python
def group_list(group, users):
  members = ",".join(users)
  return "{}:{}".format(group, " " + members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
```
6. **The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.**

**Ans-**
```python
def guest_list(guests):
	for person in guests:
		name, age, profession = person
		print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
```
## **Dictionaries**
<br>

1. **The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).**

**Ans-**
```python
def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user + '@' + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
```
2. **The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.**

**Ans-**
```python
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
			user_groups[user] = user_groups.get(user,[]) + [group]

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
```
3. **The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries are replaced and new entries are added. What is the content of the dictionary “wardrobe“ at the end of the following code?**

**Ans-**
```
{'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
```
4. **What’s a major advantage of using dictionaries over lists ?**

**Ans-**
```
It’s quicker and easier to find a specific element in a dictionary
```
5. **The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.**

**Ans-**
```python
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item in basket:
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += basket[item]
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
```

## **Module 4 Graded Assessment**
<br>

1. **The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.**

**Ans-**
```python
def format_address(address_string):
  # Declare variables
  house_number = ""
  street_name = ""
  # Separate the address string into parts
  address_string = address_string.split()

  # Traverse through the address parts
  for string in address_string:
    # Determine if the address part is the
    # house number or part of the street name
    if string.isdigit():
      house_number = string
    
  # Does anything else need to be done 
  # before returning the result?
    else:
      street_name += string + " "
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
```
2. **The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line ?**

**Ans-**
```python
def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper(), 1))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
```
3. **A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.**

**Ans-**
```python
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  return list2 + list1[::-1]
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
```
4. **Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.**
**For example, squares(2, 3) should return [4, 9].**

**Ans-**
```python
def squares(start, end):
	return [num ** 2 for num in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
5. **Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one**

**Ans-**
```python
def car_listing(car_prices):
  result = ""
  for cars in car_prices:
    result += "{} costs {} dollars".format(cars, car_prices[cars]) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
```
6. **Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.**

**Ans-**
```python
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests = guests2.copy()
  guests.update(guests1)
  return guests
  
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
```
7. **Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}**

**Ans-**
```python
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower():
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      if letter not in result:
        result[letter] = 1
    # Add or increment the value in the dictionary
      else:
        result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
```
8. **What do the following commands return when animal = "Hippopotamus"?**

**Ans-**
```

pop, t, us
```
9. **What does the list "colors" contain after these commands are executed ?**

**Ans-**
```
['red', 'white', 'yellow', 'blue']
```
10. **What do the following commands return ?**

**Ans-**
```
['router', 'localhost', 'google']
```

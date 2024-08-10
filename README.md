# Password-Generator
 The random module is imported to enable the generation of random numbers.
This module provides functions that allow us to generate random integers, floats, and more. In this case, we use it to generate random integers.
The program prompts the user to enter the number of digits they wish to generate.
The input is taken as a string and then converted into an integer using the int() function.
n will store the integer value corresponding to the number of digits to be generated.
The for loop runs n times, where n is the number of digits specified by the user.
Inside the loop:
random.randint(0, 9) generates a random integer between 0 and 9 (inclusive).
This random digit is stored in the variable c.
The print(c, end=" ") statement prints the digit c on the same line, followed by a space, due to the end=" " parameter.
The output will vary each time the program is run due to the random nature of digit generation
Key Points:
Random Number Generation: The use of random.randint(0, 9) ensures that each digit generated is between 0 and 9.
User Interaction: The program is interactive, as it prompts the user for input to determine how many random digits to generate.
Output Formatting: The print function with end=" " ensures that all digits are printed on the same line, separated by spaces.

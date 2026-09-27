"""
Module 2 — Lesson 1: Variables & Data Types
Student: Michaelle Vickeemae G. Sarmiento
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

Variables and data types are one of the basic 
parts of Python programming. A variable is like 
a labeled container where we store information, 
while a data type tells what kind of 
information is being stored. For example, if I 
want to store a student's name and age, I can use 
different variables for each one like student_name 
and student_age. It is a must to properly label to 
easily identify what it contain. Python then uses 
the data type to know how it should handle each value. 
Like string for the student_name because it contains 
text, and then integer for the student_age because it 
contain whole number. Understanding this is important 
because most programs need to store, process, and use 
different kinds of information.


============================================
KEY VOCABULARY
============================================
- variable: labeled container of information
- data type: what kind of data (like string for text, and integer for whole number)
- int: a whole number like 10, 20
- float: a number with decimal value like 99.9
- string: a text information like "Michaelle"
- boolean: value that can only be True or False
- value: the actual information to be stored in the variable
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

student_name = "Dumbo Disney" 
subjects_num = 6 
average_grade = 99.9 
is_enrolled = True 

print(f"Student: {student_name}") 
print(f"Number of Subjects: {subjects_num}") 
print(f"Average Grade: {average_grade}") 
print(f"Currently Enrolled: {is_enrolled}")
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

One thing I found confusing before in my first year 
in college about this topic is that some values can 
look the same but have different data types. For 
instance, 20 is an integer, while "20" is a string. 
At first, I thought think they are basically the same 
because they both show 20, but Python treats them differently 
(actually other programming languages too). 

It is also a must to be careful when naming variables because 
the variable name should clearly describe what information 
it stores and not just having x and y as variable names. 

Another thing to avoid is accidentally assigning the wrong 
type of value to a variable, especially when working with 
grades, calculations, or user input. I realized 
that even small mistakes in the data type can 
affect how the rest of the program works, so it is important 
to understand what kind of data is being stored
instead of just focusing on whether the code runs.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]

This connects to the systems and applications we are 
learning about because they all need to store information. 
For instance, an attendance system would need variables 
for a student's name, ID, attendance status, and possibly 
the number of absences. This made me realize that variables 
and data types are not just basic Python concepts, they are 
part of how real systems store and manage information.
"""

"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Michaelle Vickeemae G. Sarmiento
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

Control flow is how we tell Python what to do 
depending on a certain situation. Think of it 
like making a decision in everyday scenario. 
For instance, if I am going to school and it is raining, 
I will bring an umbrella. If it is not raining but 
it is a little hot, I might bring water instead. 
If neither of those situations applies, I can 
simply go to school normally. 

In Python, if, elif, and else work in a similar way. 
The program checks a condition, and depending on whether 
it is true or false, it chooses what action to perform. 
This allows a program to respond differently instead of 
always doing the same thing.


============================================
KEY VOCABULARY
============================================
- condition: a situation to check 
- if: checks the first condition if true, 
    the code runs below this if it is true
- elif: checks another condition if the previous 
    condition was false, the code below this will 
    run if the condition is met and true
- else: runs when none of the previous conditions are true
- comparison operator: operator used to compare values, 
    especially used in condition like if x == 10
- boolean expression: an expression that results in 
    either True or False
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

attendance = 85 

if attendance >= 90: 
    print("Excellent percentage attendance!") 

elif attendance >= 75: 
    print("Percentage is low, but Attendance is acceptable.") 
    
else: print("Percentage too low. Attendance needs improvement.")
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

One thing that can be easy to get wrong is the 
comparison operator. For instance, = is used to 
assign a value, while == is used to check if two 
values are equal. It is also a must to be careful with 
the indentation because Python uses indentation to 
determine which statements belong to an if, elif, 
or else block. 

Another thing is putting the conditions in the wrong 
order because Python checks them from top to bottom 
and stops once it finds a true condition.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]

The concept of if/elif/else can be compared to how 
a traffic light controls the actions of drivers. 
If the traffic light is green, the driver is allowed 
to proceed. If it is yellow, the driver is expected 
to slow down and prepare to stop. If neither of 
these conditions applies and the light is red, 
the driver must stop. 

This is similar to control flow in Python because 
the program evaluates conditions and performs a 
specific action based on the result. The traffic 
light serves as a simple real-life example of 
conditional decision-making, where different 
conditions lead to different actions.
"""

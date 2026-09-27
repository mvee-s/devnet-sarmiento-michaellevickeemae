"""
Functions
Student: Michaelle Vickeemae G. Sarmiento
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

A function is like making a shortcut for a task 
that I know I will need to do again. Instead of 
writing all the instructions every time, we can 
put them inside a function once and just call 
the function whenever we need it. 

I think of it like a vending machine. The 
machine already knows what steps to follow when 
someone chooses a drink. The customer only need 
to make a choice and press the button, and the 
machine handles the process. 

In Python, we can do something similar by creating 
a function that already contains the instructions 
for a specific task. Then give it different information 
and call it again whenever I need the same task. This 
helps in reusing code instead of repeating the same 
instructions over and over.



============================================
KEY VOCABULARY
============================================
- function: reusable set of instruction for a specific task
- def: keyword/start to create a function
- parameter: the information a function is designed to receive
- argument: the actual value given to a function
- return: sends a result back from the function
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

def make_ticket(name): 
    return "Queue ticket for " + name 

ticket = make_ticket("Michaelle") 

print(ticket)
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

The part I get most confused about is the 
difference between a parameter and an argument. 
At first, they seem like they are basically the 
same thing because both are related to the 
information given to a function. For instance, 
in def make_ticket(name):, I sometimes have 
to remind myself that name is the parameter 
because it is the placeholder that the 
function is expecting. 

When I call the function using make_ticket("Michaelle"), 
"Michaelle" is the argument because it is the 
actual value I am giving to the function.

What helped me understand it is thinking of a 
parameter as an empty space waiting for 
information, while the argument is the actual 
information placed in that space. I still 
need to be careful with this because when I 
look at the code quickly, they can look 
like the same thing. 

I want to remember it as: 
parameter = what the function expects, and
argument = what I actually give it.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
Functions can be connected to a queue management 
system. For instance, a queue system may need 
to create a ticket every time a student joins 
a line. Instead of writing separate instructions 
for every student, the system can have one 
function for creating a queue ticket. 

Whenever another student joins, the same 
function can be called with their information. 
This shows how functions can make a system 
more organized because one prepared process 
can be reused many times with different 
information.



"""

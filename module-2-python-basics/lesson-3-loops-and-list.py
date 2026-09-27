"""
Module 2 — Lesson 3: Loops & Lists
Student: Michaelle Vickeemae G. Sarmiento
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

Lists and loops are used when a program needs 
to work with multiple pieces of information. 
A list can be compared to a class attendance 
sheet where the names of all the students are 
written together in one place. Instead of having 
a separate variable for every student, the names 
can be stored in one list. A loop is like the 
process of the teacher checking the attendance 
sheet from the first student until the last one. 
The same action is repeated for every name on the list. 

In Python, a loop allows the program to go through 
each item in a list and perform the same task 
automatically. This makes it easier to handle 
many pieces of data without writing the same 
instructions repeatedly.


============================================
KEY VOCABULARY
============================================
- list: collection of multiple values
- for loop: repeats an action for each item
- while loop: repeats an action as long as the condition is true
- index: the position of an item in a list (starting with 0)
- iteration: repetition of a loop
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
artists = ["Michaelle", "Wonwoo", "Seonghyeon", "Dumbo", "Dinosaur"] 

for artist in artists:
     print(f"{artist} is Present today!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

One thing that can be confusing about lists is 
that Python starts counting the position of items 
at 0, not 1. For instance, the first item has an 
index of 0, the second item has an index of 1, 
and so on. This can easily cause confusion when 
trying to access a specific item. 

For loops, one mistake to avoid is misunderstanding 
how the loop repeats an instruction. The loop 
automatically processes each item one at a time, 
so the same instruction does not need to be 
written repeatedly. It is also important to check 
the loop condition and indentation, especially 
when using while loops, because an incorrect 
condition can cause the loop to continue indefinitely.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]

Lists and loops can be connected to how a supermarket 
handles a customer's shopping cart. The list can 
represent all the items placed in the cart, 
such as bread, milk, eggs, and rice. Instead 
of storing each item separately, the system can 
keep them together in one list. 

A loop can then be used to go through each item 
in the cart one by one to calculate the total price, 
check the items, or display them on the receipt. 
This shows how lists are useful for storing related 
information, while loops are useful for repeatedly 
processing that information. The same concept can 
be applied to real systems that need to handle 
many records or items without writing the same 
instructions repeatedly.

"""

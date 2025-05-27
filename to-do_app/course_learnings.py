"""

Day 3
+ how to print each items per line in a list without the display of brackets and quotations?
    - use a for loop to loop the lists
- using strip method
- whatever block in case

Day 4
+ How to integrate an edit feature in our to-do list
    + how to overwrite an existing list
    + how to select which index in the list is to edit

    - It's actually quite easy not that I've seen the code. Just use an assignment operator

+ How to change something in a specfiied string on a list
    - use .replace method

Day 5
- used enumerate on a string on the for-loop
+ how to print the numbers of a string in each loop
    - my first approach is to assign a variable. The second is to use the enumerate function
+ how to checked or remove an item in a to-do list?
    - use the pop method

Day 6
+ How to store the inputs of the user such that the task is saved?
    + how to store the inputs in the file?
        - use the file function of python with open method and .writelines
    - use file handlings using open, write and read methods

+ How to create a program in which the data of a list for example will be stored in the text file even though the text file is created on the fly?
    - use zip function

- Used read and write method in file handling

Day 7
- List comprehension
- sum() function

Day 8
- How to improve the code, make it more readable for the other developer
    + How to edit files in a text?
        - incorporate read and write method as well as \n

Day 9
- how to replace something in the string
- learned isdigit()
- learned isupper()
- learned all() for the list

Day 10
- learned how to use startswith() method
- exit() function

Day 11
- How to use a function
- index slicing
+ How to make a program in which the number that is inputted is stored into the file and is calcucalted the average
- How to use the max() and min() of a list

Day 12
- .split() method in a string
- default parameters

Day 13
- using seperate files using "from __ import ___'
- using __name__ = "__main__"

Day 15
- adding time module to print out date and time in real time on my terminal
- using a file variable of the text file for better code optimization
- four important modules
    - glob
    - csv
    - shutil
    - webbrowser
- used json file for more comprehensive data structures of this shit
"""


def say_something(say):
    return say


print(say_something('hello muelvin!'))

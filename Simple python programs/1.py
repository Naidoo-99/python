""" A simple program that will prompt a user to input a sentence.
The program will count all lower case alphabets, upper case alphabets, digits, and special symbols.
Then the program will display the all the counts on screen.""" 

from builtins import input

a = input("enter a sentence")

lower_case=0
upper_case=0
digit=0
special_symbols=0

for b in a:
    if b.islower():
        lower_case +=1

    elif b.isupper():
        upper_case +=1

    elif b.isdigit():
        digit+=1

    else:
        special_symbols +=1



        print("lower case i", lower_case)
        print("upper case i", upper_case)
        print("digit:", digit)
        print("Special_symbol:",special_symbols)
        print("counts of the sentence")

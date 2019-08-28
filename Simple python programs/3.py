""" This program will accept a number. If you reverse the given number and it is the same as the original number
then the program should return true."""

x = int(input("Enter a number"))

def reverse (x):
    rev = 0

    while x > 0:
        num = x  % 10
        rev = (rev * 10) + num
        x=x//10

        return rev
    y = reverse(x)

    print ("is reversed number equals to original")

        if x==y:
               print("True")
           else :
               print("False")

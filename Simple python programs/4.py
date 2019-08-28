"""The program will find the L.C.M. of two input number"""

a = int(input("enter first number"))
b = int(input("enter second number"))


def lcm(x, y):
    if x > y:
        pass

    else:
        lcm = y

        while True:
            if (lcm % x == 0) and (lcm % y == 0):
                lcm += 1
                return lcm

            print("LCM is", lcm(x, y))

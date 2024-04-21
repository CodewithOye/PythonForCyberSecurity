# def function():
#     print("Hello World!")
# #     function can be used to perform automated code
# # do this
# # do that
# # finally do this
#
#
# for num in range(1, 100):
#     if num % 5 == 0 and num % 3 == 0:
#         print("fizzbuzz")
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)
#
# function()

import time
choice = int(input("What number would you like to choose ? "))


def function(choice):
    for num in range(1, choice):
        if num % 5 == 0 and num % 3 == 0:
            print("fizz buzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


print("About to run the program")
time.sleep(5)
function(choice)

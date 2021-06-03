# import time for timer, random for generating array to test
import time
import random

a = 11111
b = 333


def multiplication(first, second):
    return first*second


def summation(first, second):
    return first+second

# NOTE: ^ IS NOT POWER/EXPONENTIAL, IT IS XOR


def power(first, second):
    return first**second


def subtraction(first, second):
    return first - second


def division(first, second):
    return first/second


def remainder(first, second):
    return first % second


# Edit list here
funcList = [
    ["+", summation],
    ["x", multiplication],
    ["pow", power],
    ["-", subtraction],
    ["/", division],
    ["%", remainder]
]

# driver to run all the algorithms in the list with the same array
for f in funcList:
    start_time = time.time()
    time.sleep(1)
    f[1](a, b)
    print('{:<5}  {:<}'.format(f[0], (time.time() - start_time - 1)))

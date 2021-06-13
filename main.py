# import time for timer, operation for math functions
import time
from operation import *

# VARIABLES
a = 11111
b = 333

# Edit list here
funcList = [
    ["+", summation],
    ["x", multiplication],
    ["pow", power],
    ["-", subtraction],
    ["/", division],
    ["%", remainder]
]

# DRIVER
# to run all the algorithms in the list with the same array
for f in funcList:
    start_time = time.time()
    time.sleep(1)
    f[1](a, b)
    print('{:<5}  {:<}'.format(f[0], (time.time() - start_time - 1)))

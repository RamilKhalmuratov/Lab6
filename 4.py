import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  
    return math.sqrt(number)

num = int(input(""))
delay = int(input(""))

result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")
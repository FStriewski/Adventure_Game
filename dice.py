# Implements a D6 dice
import random

def dice_d(number:int =1, d:int =6) -> int:
    result = 0
    for i in range(0,number):
        result += random.randint(1,d)
    return(result)

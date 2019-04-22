# Implements a D6 dice
import random

def dice_d6(number =1):
    result = 0
    for i in range(0,number):
        result += random.randint(1,6)

    print(result)

    return result


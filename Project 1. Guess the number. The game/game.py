""""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

count = 0 # the number of tries

while True:
    count+=1
    predict_number = int(input("We guessed a number from 1 to 100. What do you think it is? "))
    
    if predict_number > number:
        print("the number is smaller")
        
    elif predict_number < number:
        print("the number is larger")
        
    else:
        print(f"You are correct. The number is {number}. You've guessed it in {count} tries")
        break # the end of the game
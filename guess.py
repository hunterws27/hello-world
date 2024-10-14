import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
max_guesses = math.ceil(math.log2(larger - smaller + 1))
print(f"I will guess your number in no more than {max_guesses} tries.")

count = 0
while smaller <= larger:
    count += 1
    guess = (larger + smaller) // 2
    print(f"My guess is: {guess}")
    feedback = input("Is it correct, too high (H), or too low (L)? ")
    
    if feedback == 'h':
        larger = guess - 1
    elif feedback == 'l':
        smaller = guess + 1
    elif feedback == 'correct':
        print(f"I've got it in {count} tries!")
        break
    else:
        print("Please enter 'H', 'L', or 'correct'.")
    
    if count > max_guesses:
        print("Something's not right; I should have guessed it by now. No cheating!")
        

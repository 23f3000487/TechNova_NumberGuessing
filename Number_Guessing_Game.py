import random 

print("=== NUmber Guessing Game ===")
print("I have chosen a number between 1 and 100.")

number = random.randint(1,100)
attempts=0

while True:
    try:
        guess=int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again")
        elif guess > number:
            print("Too high! Try again")      
        else:
            print("Correct!")
            print("You guessed it in", attempts, "attempts.")
            break
    
    except ValueError:
        print("Enter a valid number")
print("Thanks for playing")
            

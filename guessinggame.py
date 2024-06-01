import random

def main():
    print("Welcome to the Number Guessing Game!")
    
   
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    
    while not guessed_correctly:
        try:
            
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts to guess the number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
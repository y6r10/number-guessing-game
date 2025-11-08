import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose difficulty: 1 (Easy: 1-50), 2 (Medium: 1-100), 3 (Hard: 1-200)")
    
    difficulty = int(input("Enter difficulty: "))
    
    if difficulty == 1:
        max_num = 50
    elif difficulty == 2:
        max_num = 100
    else:
        max_num = 200
    
    number = random.randint(1, max_num)
    attempts = 0
    
    print(f"I'm thinking of a number between 1 and {max_num}.")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You won in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game()
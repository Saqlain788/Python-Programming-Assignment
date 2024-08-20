import random
from typing import Literal

NUM_ROUNDS: int = 5  # You can change the number of rounds here

def get_user_guess() -> Literal['higher', 'lower']:
    """Get and validate the user's guess."""
    while True:
        guess: str = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()
        if guess in ['higher', 'lower']:
            return guess
        else:
            print("Please enter either 'higher' or 'lower'.")

def evaluate_round(user_number: int, computer_number: int, guess: Literal['higher', 'lower']) -> bool:
    """Evaluate the round and return whether the user's guess was correct."""
    if (user_number > computer_number and guess == 'higher') or (user_number < computer_number and guess == 'lower'):
        return True
    else:
        return False

def play_game() -> None:
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score: int = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        user_number: int = random.randint(1, 100)
        computer_number: int = random.randint(1, 100)
        
        print(f"Your number is {user_number}")
        
        guess: Literal['higher', 'lower'] = get_user_guess()
        
        if evaluate_round(user_number, computer_number, guess):
            score += 1
            print(f"You were right! The computer's number was {computer_number}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
    evaluate_performance(score)

def evaluate_performance(score: int) -> None:
    """Evaluate and print the performance message based on the player's score."""
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()

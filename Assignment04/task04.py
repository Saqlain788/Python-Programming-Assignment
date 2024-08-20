from typing import List, Tuple

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main() -> None:
    # Step 1: Gather user's name and favorite numbers
    name: str = input("Enter your name: ")
    num1: int = int(input("Enter your first favorite number: "))
    num2: int = int(input("Enter your second favorite number: "))
    num3: int = int(input("Enter your third favorite number: "))
    
    # Store the numbers in a list
    numbers: List[int] = [num1, num2, num3]
    
    # Step 2: Check if numbers are even or odd
    even_odd_info: List[Tuple[int, str]] = []
    for num in numbers:
        if num % 2 == 0:
            even_odd_info.append((num, "even"))
        else:
            even_odd_info.append((num, "odd"))
    
    # Step 3: Greet the user and display the even/odd information
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    for info in even_odd_info:
        print(f"The number {info[0]} is {info[1]}.")
    
    # Step 4: Calculate and display the square of each number
    for num in numbers:
        square_tuple: Tuple[int, int] = (num, num ** 2)
        print(f"The number {num} and its square: {square_tuple}")
    
    # Step 5: Calculate the sum of the numbers and display it
    total_sum: int = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    
    # Step 6: Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"The sum {total_sum} is not a prime number.")
        
# Run the program
main()

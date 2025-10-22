#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_user_input():
    valid = False
    while not valid:
        user_input = input("Enter the number of Fibonacci terms you want: ")
        if user_input.isdigit():
            terms = int(user_input)
            if terms > 0:
                valid = True
                return terms
            else:
                print("Please enter a positive number.")
        else:
            print("Invalid input. Please enter a whole number.")


def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_fibonacci(sequence):
    """Print the Fibonacci sequence in a readable format."""
    print("\nFibonacci sequence:")
    print(*sequence, sep=", ")


def main():
    num_terms = get_user_input()
    fib_sequence = generate_fibonacci(num_terms)
    print_fibonacci(fib_sequence)


main()

#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_user_input():
    while True:
        try:
            terms = int(input("Enter the number of Fibonacci terms you want: "))
            if terms <= 0:
                print("Please enter a positive integer.")
            else:
                return terms
        except ValueError:
            print("Invalid input. Please enter an integer.")


def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_fibonacci(sequence):
    print("\nFibonacci sequence:")
    print(", ".join(map(str, sequence)))


def main():
    num_terms = get_user_input()
    fib_sequence = generate_fibonacci(num_terms)
    print_fibonacci(fib_sequence)


main()

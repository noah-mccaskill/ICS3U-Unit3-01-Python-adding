#!/usr/bin/env python3

# Created by Noah McCaskill
# Created in April 2022
# Program that adds 2 numbers


def main():
    # This function finds the sum of 2 numbers

    # Input
    print("This program adds 2 numbers together!")
    first_number = int(input("Please enter the first number: "))
    second_number = int(input("Please enter the second number: "))

    # Process
    sum = first_number + second_number

    # Output
    print("{0}+{1}={2}".format(first_number, second_number, sum))


if __name__ == "__main__":
    main()

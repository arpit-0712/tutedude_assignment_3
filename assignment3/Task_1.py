#!/usr/bin/env python3


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


x = int(input("Enter a number: "))
print(f"Factorial of {x} is:",factorial(x))



#!/usr/bin/env python3

def factorial(num):
    fact=1;
    for i in range(1,num+1):
        fact*=i;
    return fact;

x=int(input("Enter the number to find factorial: "))
print(factorial(x))

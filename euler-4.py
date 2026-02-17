import math
import os
import random
import re
import sys

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_product_of_3_digit_numbers(num):
    for i in range(100, 1000):
        if num % i == 0:
            j = num // i
            if 100 <= j < 1000:
                return True
    return False

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        for num in range(n-1, 10000, -1):
            if is_palindrome(num) and is_product_of_3_digit_numbers(num):
                print(num)
                break
        
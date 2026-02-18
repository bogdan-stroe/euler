import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        sum_of_squares = sum(i**2 for i in range(1, n+1))
        square_of_sum = sum(range(1, n+1)) ** 2
        print(square_of_sum - sum_of_squares)
        
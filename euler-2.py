import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        sum = 0
        f1 = 1
        f2 = 1
        f3 = f1 + f2
        while f3 < n:
            if f3 % 2 == 0:
                sum += f3
            f1 = f2
            f2 = f3
            f3 = f1 + f2
        print(sum)

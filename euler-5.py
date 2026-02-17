import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        lcm = 1
        for i in range(2, n+1):
            lcm = lcm * i // math.gcd(lcm, i)
        print(lcm)
        
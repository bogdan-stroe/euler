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
        p3 = (n - 1) // 3
        p5 = (n - 1) // 5
        p15 = (n - 1) // 15
        sum += 3 * p3 * (p3 + 1) // 2
        sum += 5 * p5 * (p5 + 1) // 2
        sum -= 15 * p15 * (p15 + 1) // 2
        print(sum)

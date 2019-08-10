#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    result = list()

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.match('[a-z]*[.]*[a-z]*@gmail.com', emailID) :
            result.append(firstName)

    result.sort()
    for x in result:
        print(x)
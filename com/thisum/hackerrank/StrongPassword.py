#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    needed_length = 0

    result = re.search("[a-z]", password)
    if not result:
        needed_length += 1

    result = re.search("[A-Z]", password)
    if not result:
        needed_length += 1

    result = re.search("[0-9]", password)
    if not result:
        needed_length += 1

    result = re.search("[!@#$%^&*()\-+]", password)
    if not result:
        needed_length += 1

    needed_length += 0 if (needed_length + n >= 6) else (6 - (needed_length + n))

    return needed_length


if __name__ == '__main__':

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
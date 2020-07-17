# The following iterative sequence is defined for the set of positive integers:
# n e28692 n/2 (n is even)n e28692 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 e28692 40 e28692 20 e28692 10 e28692 5 e28692 16 e28692 8 e28692 4 e28692 2 e28692 1
# It can be seen that this sequence (starting
# at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz
# Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
from decorators import *
import numpy as np
import math


def v1():
    print()


@timer
def main():
    v1()


if __name__ == '__main__':
    main()

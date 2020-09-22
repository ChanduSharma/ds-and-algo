#!/bin/python3
# Solution to problem link:  https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

import math
import os
import random
import re
import sys

# Complete the steadyGene function below.
def steadyGene(gene):

    def allBalancedCharacters(map):
        for i in map.values():
            if i > n//4:
                return False
        return True
    left,right = 0,0
    length = len(gene)
    countMap = {'A':0,'C':0,'G':0,'T':0}
    for c in gene:
        countMap[c] += 1
    minimum = 500001

    while right < n - 1:
        rightCharacter = gene[right]
        right += 1
        countMap[rightCharacter] -= 1
        while (allBalancedCharacters(countMap)):
            minimum = min(minimum, right-left)
            leftCharacter = gene[left]
            left += 1
            countMap[leftCharacter] += 1
    
    return minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()

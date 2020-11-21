"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

import getopt, sys
from Example1 import Example1

def main():

    if len(sys.argv) != 3: 
        print ("Usage:\n  Main.py <algorithm to use> <example to use>")
        print ("\nExample:\n  Main.py -m Example1")
        print ("\nAvailable algorithms:\n  -r (recursive); -m (memoization); -d (dynamic)")
        print ("\nAvailable examples:\n  Example1")

        sys.exit()

    alg=sys.argv[1]
    example=sys.argv[2]

    if example == 'Example1':
        example1 = Example1()
        example1.chose_alg(alg)



    if alg not in ['-r','-m','-d'] or example != 'Example1':
        print ("Usage:\n  Main.py <algorithm to use> <example to use>")
        print ("\nExample:\n  Main.py -m Example1")
        print ("\nAvailable algorithms:\n  -r (recursive); -m (memoization); -d (dynamic)")
        print ("\nAvailable examples:\n  Example1")


        sys.exit()





if __name__ == '__main__':
    main()


"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

import getopt, sys
from Examples.Example1 import Example1
from Examples.Example2 import Example2
from Examples.Example4 import Example4



def main():

    if len(sys.argv) < 3: 
        print ("Usage:\n  Main.py <algorithm to use> <example to use> <optional:show longest subsquence if dynamic alg used>")
        print ("\nExample:\n  Main.py -m Example1")
        print ("\nExample:\n  Main.py -d Example1 -s")
        print ("\nExample:\n  Main.py -d Example1")
        print ("\nAvailable algorithms:\n  -r (recursive); -m (memoization); -d (dynamic)")
        print ("\nAvailable examples:\n  Example1 Example2 Example4")

        sys.exit()

    alg=sys.argv[1]
    example=sys.argv[2]
    show = ""

    if len(sys.argv) == 4:
        show = sys.argv[3]

    if example == 'Example1':
        example1 = Example1()
        if show == "":
            example1.chose_alg(alg)
        else:
            example1.chose_alg(alg,show)

    if example == 'Example2':
        example2 = Example2()
        if show == "":
            example2.chose_alg(alg)
        else:
            example2.chose_alg(alg,show)

    if example == 'Example4':
        example4 = Example4()
        if show == "":
            example4.chose_alg(alg)
        else:
            example4.chose_alg(alg,show)

    
    if alg == '-d':
        if show not in ["", '-s']:
            print ("Usage:\n  Main.py <algorithm to use> <example to use> <optional:show longest subsquence if dynamic alg used>")
            print ("\nExample:\n  Main.py -m Example1")
            print ("\nExample:\n  Main.py -d Example1 -s")
            print ("\nExample:\n  Main.py -d Example1")
            print ("\nAvailable algorithms:\n  -r (recursive); -m (memoization); -d (dynamic)")
            print ("\nAvailable examples:\n  Example1 Example2 Example4")
            sys.exit()

    if alg not in ['-r','-m','-d'] or example not in ['Example1', 'Example2', 'Example4']:
        print ("Usage:\n  Main.py <algorithm to use> <example to use> <optional:show longest subsquence if dynamic alg used>")
        print ("\nExample:\n  Main.py -m Example1")
        print ("\nExample:\n  Main.py -d Example1 -s")
        print ("\nExample:\n  Main.py -d Example1")
        print ("\nAvailable algorithms:\n  -r (recursive); -m (memoization); -d (dynamic)")
        print ("\nAvailable examples:\n  Example1 Example2 Example4")
        sys.exit()


if __name__ == '__main__':
    main()


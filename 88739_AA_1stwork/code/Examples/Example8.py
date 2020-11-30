"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

from Recursive.LCS_recursive import LCS_recursive
from Memoization.LCS_memoization_wrapper import LCS_memoization_wrapper
from Dynamic.LCS_dynamic import LCS_dynamic

class Example8:

    def __init__(self):
        with open('Examples/creatures.txt', 'r') as file:
            self.seqA = file.read().replace('\n', '')
        with open('Examples/redwitch.txt', 'r') as file:
            self.seqB = file.read().replace('\n', '')

    def chose_alg(self,chosen, show=None):
        if chosen == "-r":
            #TODO Escrever para ficheiro
            recursive = LCS_recursive(self.seqA,self.seqB)
            recursive.get_lcs_len_recursive()
        elif chosen == "-m":
            memoization = LCS_memoization_wrapper(self.seqA,self.seqB)
            memoization.get_lcs_len_memoization()
        elif chosen == "-d":
            dynamic = LCS_dynamic(self.seqA, self.seqB)
            dynamic.get_lcs_len_dynamic()
            if show == "-s":
                dynamic.get_lcs_longest_subsquence()

    
    
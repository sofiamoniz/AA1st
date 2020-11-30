"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

from Recursive.LCS_recursive import LCS_recursive
from Memoization.LCS_memoization_wrapper import LCS_memoization_wrapper
from Dynamic.LCS_dynamic import LCS_dynamic

class Example2:

    def __init__(self):
        self.seqA = "BANANABANANA"
        self.seqB = "ATANAATANA"

    def chose_alg(self,chosen,show=None):
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

    
    
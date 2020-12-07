"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

from Recursive.LCS_recursive import LCS_recursive
from Memoization.LCS_memoization_wrapper import LCS_memoization_wrapper
from Dynamic.LCS_dynamic import LCS_dynamic

##Class that represents the third example, in which the LCS has a len of 25

class Example3:

    def __init__(self):
        self.seqA = "AGGTABAGGTABAGGTABAGGTABAGGTABAGGTABAG"
        self.seqB = "GXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTX"

    def chose_alg(self,chosen,show=None):
        if chosen == "-r":
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

    
    
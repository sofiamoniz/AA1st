"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

from Recursive.LCS_recursive import LCS_recursive

class Example1:

    def __init__(self):
        self.seqA = "ABCD"
        self.seqB = "ACBAD"

    def chose_alg(self,chosen):
        if chosen == "-r":
            #Escrever para ficheiro
            recursive = LCS_recursive(self.seqA,self.seqB)
            recursive.get_lcs_len_recursive()
    
    
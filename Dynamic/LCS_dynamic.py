"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

#import sys
from Table import Table

##Class that calculates Longest Common Subsquence for two given strings, using dynamic programming

class LCS_dynamic:

    def __init__(self, seqA , seqB):
        self.seqA = seqA
        self.seqB = seqB
        self.lcs = ""
        self.table = Table(len(self.seqA), len(self.seqB)).build_array()
        #sys.setrecursionlimit(15000)

    def lcs_dynamic(self, m, n):

        """
        This function will calculate, using dynamic programming  in a bottom up approach, the len of the 
        longest subsquence between two sequences. This will allow to improve the
        complexity of the problem, once besides avoiding the occurence of repeated subproblems, will avoid
        recursive calls by visiting the array (table) systematically. The only thing to worry about is that
        when a cell is filled, we need to know the values it depends on.        
        """
        
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0: 
                    self.table[i][j] = 0
                elif self.seqA[i-1] == self.seqB[j-1]:
                    self.table[i][j] = self.table[i-1][j-1] + 1
                else:
                    self.table[i][j] = max(self.table[i-1][j],self.table[i][j-1])

        return self.table[m][n]


    def get_lcs_len_dynamic(self):

        """
        Getter for lcs len
        """

        print("The len of LCS (calculated using dynamic programing) is",self.lcs_dynamic(len(self.seqA), len(self.seqB)) )
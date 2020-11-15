"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""
from Memoization_table import Memoization_table

##Class that calculates Longest Common Subsquence for two given strings, using memoization

class LCS_memoization:

    def __init__(self, seqA , seqB):
        self.seqA = seqA
        self.seqB = seqB
        #self.lcs = ""
        self.table = Memoization_table(len(self.seqA),1000).build_array()
        
    def lcs_memoization(self ,m, n):

        """
        This function will calculate, using memoization, the len of the 
        longest subsquence between two sequences. This will allow to improve the
        complexity of the problem, once it will avoid the occurence of repeated subtrees, in the tree
        (in the recursive version, it may exist subproblems that are solved several times). 
        Thus, an array will be needed so that we can store these subproblemas results - if we want a
        subproblem solution, first we check if the array already contains it.
        """

        # The len of each sequence passed will be used so that a for loop can be avoided
        # m and n is used so that it can be imagined as a matrix
        if (m==0 or n==0): #If any have len=0, 0 will be returned
            return 0

        if (self.table[m-1][n-1] == -1): #If the table contains -1 at that position, it means that this subproblem
                                            #Wasn't computed already
            if (self.seqA[m-1] == self.seqB[n-1]): #If the symbol of each sequence match
                self.table[m-1][n-1] = 1 + self.lcs_memoization(m-1,n-1) #If the symbols match, 1 is added and a move in each sequence is made
                return self.table[m-1][n-1] #We move in the table too
            else:
                self.table[m-1][n-1] = max(self.lcs_memoization(m-1,n), self.lcs_memoization(m, n-1)) #We move in each sequence and check which
                                                                                                        #one returns a max value
                return self.table[m-1][n-1] #We move in the table too
        else: #If that subproblem was already calculated, we grab it from the table
            return self.table[m-1][n-1]

    
    def get_lcs_len_memoization(self):

        """
        Getter for lcs len
        """

        print("The len of LCS (calculated in memoization) is",self.lcs_memoization(len(self.seqA), len(self.seqB)) )
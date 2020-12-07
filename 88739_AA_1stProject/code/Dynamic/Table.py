"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

##Class that will be used to store repeated subproblems, in the dynamic programming algorithm

class Table:

    def __init__(self, m, n):
        self.m = m
        self.n = n

    def build_array(self):

        """
        Creates a 2D array with size m+1*n-1 
        """
        
        #The multiplication is made so that we can avoid another for loop
        return [[-1]*(self.n+1) for j in range(self.m+1)] #With size m+1*n-1 we will never get out of range
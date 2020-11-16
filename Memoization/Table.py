"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

##Class that will be used to store repeated subproblems, in the memoization aproach

class Table:

    def __init__(self, lenM, maximum):
        self.lenM = lenM
        self.maximum = maximum #a maximum value is used so that we never get out of range
    
    def build_array(self):
        return [[-1 for i in range(self.maximum)] for j in range(self.lenM)]


"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

##Class that will be used to store repeated subproblems, in the memoization aproach

class Table:

    def __init__(self, m, n):
        self.m = m
        self.n = n

    def build_array(self):
        return [[None]*(self.n+1) for j in range(self.m+1)]
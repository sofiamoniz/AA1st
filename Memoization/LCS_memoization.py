"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""
from Table import Table
import sys


##Class that calculates Longest Common Subsquence for two given strings, using memoization

class LCS_memoization:

    def __init__(self, seqA , seqB):
        self.seqA = seqA
        self.seqB = seqB
        self.lcs = set()
        self.table = Table(len(self.seqA), len(self.seqB)).build_array()
        self.i =0
        self.j=0
        sys.setrecursionlimit(15000)
        
    def lcs_memoization(self ,m, n):

        """
        This function will calculate, using memoization, the len of the 
        longest subsquence between two sequences. This will allow to improve the
        complexity of the problem, once it will avoid the occurence of repeated subtrees, in the tree
        (in the recursive version, it may exist subproblems that are solved several times). 
        Thus, an array will be needed so that we can store these subproblemas results - if we want a
        subproblem solution, we check if the array already contains it.
        """
        # The len of each sequence passed will be used so that a for loop can be avoided
        # m and n is used so that it can be imagined as a matrix
        if (m==0 or n==0): #If any have len=0, 0 will be returned
            return 0

        if (self.table[m-1][n-1] != -1): #If the table doesn't contain -1 at that position, it means that this subproblem
                                            #was already computed, so we can take it from the table
            return self.table[m-1][n-1]

        ##In case the table doesn't contain the subproblem solution:
        
        if (self.seqA[m-1] == self.seqB[n-1]): #If the symbol of each sequence match
            self.table[m-1][n-1] = 1 + self.lcs_memoization(m-1,n-1) #If the symbols match, 1 is added and a move in each sequence is made
            return self.table[m-1][n-1] #We move in the table too

        else:
            self.table[m-1][n-1] = max(self.lcs_memoization(m-1,n), self.lcs_memoization(m, n-1)) #We move in each sequence and check which
                                                                                                    #one returns a max value
            return self.table[m-1][n-1] #We move in the table too
    

    
    def traceback_table_forward(self,m,n):
        while(self.i<m and self.j<n):
            lcs=set()
            
            if self.seqA[self.i] == self.seqB[self.j]:
                lcs.add(self.seqA[self.i])
                self.i += 1
                self.j += 1
            
            else:
            #If the last values don't match, the LCS must be constructed by left direction or top direction. We
            #go for the biggest value, or for both if they are equal
            #Top direction: table[m-1][n]
            #Left direction : table[m][n-1]

                if (self.table[self.i][self.j+1] > self.table[self.i+1][self.j]):
                    self.j+=1
                    lcs = self.traceback_table(self.i, (self.j)+1)
                    

                if (self.table[self.i+1][self.j] >= self.table[self.i][self.j+1]):
                    self.i+=1
                    lcs = self.traceback_table((self.i)+1, self.j)

                if (self.table[self.i+1][self.j] == self.table[self.i][self.j+1]):
                    left = self.traceback_table(self.i, self.j+1)
                    top = self.traceback_table(self.i+1, self.j)

                    for l in left:
                        for t in top:
                            lcs.add(l)
                            lcs.add(t)

                    self.i+=1
                    self.j+=1
                    

        return lcs

    def get_lcs_len_memoization(self):

        """
        Getter for lcs len
        """

        print("The len of LCS (calculated in memoization) is",self.lcs_memoization(len(self.seqA), len(self.seqB)) )
        #print("lcs ", self.traceback_table(len(self.seqA), len(self.seqB)))

       
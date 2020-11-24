"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""

import sys, time
from Dynamic.Table import Table

##Class that calculates Longest Common Subsquence for two given strings, using dynamic programming

class LCS_dynamic:

    def __init__(self, seqA , seqB):
        self.seqA = seqA
        self.seqB = seqB
        self.table = Table(len(self.seqA), len(self.seqB)).build_array()
        self.num_iter = 0
        self.max_calc = 0
        self.sum_count = 0
        sys.setrecursionlimit(15000)

    def lcs_dynamic(self, m, n):
        
        """
        This function will calculate, using dynamic programming , the len of the 
        longest subsquence between two sequences. This will allow to improve the
        complexity of the problem, once besides avoiding the occurence of repeated subproblems, it will avoid
        recursive calls by visiting the array (table) systematically. The only thing to worry about is that
        when a cell is filled, we need to know the values it depends on.        
        """
        
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0: 
                    self.table[i][j] = 0
                elif self.seqA[i-1] == self.seqB[j-1]: #If the symbol of each sequence match
                    self.sum_count += 1
                    self.table[i][j] = self.table[i-1][j-1] + 1 #We add 1 and go to the next element in the array
                else:
                    self.max_calc += 1
                    self.table[i][j] = max(self.table[i-1][j],self.table[i][j-1]) #We found if the max is the left cell
                                                                                #Or the top cell and return it
        return self.table[m][n]



    def traceback_table(self,m,n):
        
        """
        This function will traceback the table (2d array), that stores the LCS sequence
        len of each step of the calculation.
        The traceback starts by the last cell -> when the len decreases between cells,
        it might be a sign that the subsquences have that element in common.
        """

        lcs = set() #lcs set to store the possible subsquence(s)

        if m==0 or n==0: #If they are 0, we know that we are at the first column/row and that those values are 0 - no symbol
            lcs.add("")
            return lcs

        if (self.seqA[m-1] == self.seqB[n-1]): #If the last value of each subsquence is equal, this char
                                            #Must be present in all substrings once this is a match
            all_subsquences = self.traceback_table(m-1,n-1)
            for sub in all_subsquences:
                lcs.add(self.seqA[m-1] + sub)
        else:
            #If the last values don't match, the LCS must be constructed by left direction or top direction. We
            #go for the biggest value, or for both if they are equal
            #Top direction: table[m-1][n]
            #Left direction : table[m][n-1]

            if (self.table[m][n-1] > self.table[m-1][n]): #If the value on the left is bigger, we go left
                lcs = self.traceback_table(m,n-1)

            if (self.table[m-1][n] > self.table[m][n-1]): #If the value on the top is bigger, we go top
                lcs = self.traceback_table(m-1,n)

            if (self.table[m-1][n] == self.table[m][n-1]): #If both values are the same, we go both ways
                left = self.traceback_table(m,n-1)
                top = self.traceback_table(m-1,n)

                for l in left:
                    for t in top:
                        lcs.add(l)
                        lcs.add(t)
          

        return lcs
     
     
    def get_lcs_len_dynamic(self):

        """
        Getter for lcs len
        """
        start_time = time.time()
        recursive_len = self.lcs_dynamic(len(self.seqA), len(self.seqB))
        end_time = time.time() - start_time

        print("\nAlgorithm used - Dynamic \n"
                    +"\n--- LCS len:  %s " % (recursive_len) 
                    +"\n--- Execution time:  %s seconds" % (round(end_time,7))
                    +"\n--- Basic operations:  %s sums and %s maximum calculations" % (self.sum_count, self.max_calc))    
        

    def get_lcs_longest_subsquence(self):
        print("\nLongest subsquence(s) found:")
        for subsq in self.traceback_table(len(self.seqA), len(self.seqB)):
            print (subsq[::-1])
        

        

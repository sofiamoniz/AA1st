"""
AA, December 2020
Assignment 1: Estratégias de Desenvolvimento de Algoritmos 
            - The Longest Common Subsequence Problem
Autor: Ana Sofia Fernandes, 88739
"""
import sys
import time

##Class that calculates Longest Common Subsquence for two given strings, in a recursive way

class LCS_recursive:

    def __init__(self, seqA , seqB):
        self.seqA = seqA
        self.seqB = seqB
        self.num_iter = 0
        self.max_calc = 0
        self.sum_count = 0
        sys.setrecursionlimit(15000)
        

    def lcs_recursive_way(self ,m, n):
        self.num_iter +=1
        """
        This function will calculate, in a recursive way, the len of the 
        longest subsquence between two sequences. There are two cases:
            1-The last carachter match - increment the length and proceed in the sequence (-1 in each)
            2-The last character doesn't match - find the max between lcs_recursive_way(m-1,n) and lcs_recursive_way(m, n-1)
        """
        
        # The len of each sequence passed will be used so that a for loop can be avoided
        # m and n is used so that it can be imagined as a matrix
        if (m==0 or n==0): #If any have len=0, 0 will be returned
            return 0

        elif (self.seqA[m-1] == self.seqB[n-1]): #If the symbols match, 1 is added to the len (we have a match) 
                                                #and a move in each sequence is made
            self.sum_count += 1
            return 1 + self.lcs_recursive_way(m-1,n-1)
        
        else: # If there's no match in that position
            self.max_calc += 1
            return max(self.lcs_recursive_way(m-1,n), self.lcs_recursive_way(m, n-1)) #We move in each sequence and check which
                                                                                        #one returns a max value for the len

    def get_lcs_len_recursive(self):

        """
        Getter for lcs len
        """
        start_time = time.time()
        recursive_len = self.lcs_recursive_way(len(self.seqA), len(self.seqB))
        end_time = time.time() - start_time
        print("\n    Algorithm used - recursive \n"
                    +"\n--- LCS len:  %s " % (recursive_len) 
                    +"\n--- Execution time:  %s seconds" % (round(end_time,7))
                    +"\n--- Basic operations:  %s sums and %s maximum calculations" % (self.sum_count, self.max_calc)
                    +"\n--- Recursive calls:  %s " % (self.num_iter))
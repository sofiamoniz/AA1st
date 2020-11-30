 """
        if m == 0 or n == 0:
            return "";
        if (self.seqA[m - 1] == self.seqB[n - 1]):
            return self.backtrack(m - 1, n - 1) + self.seqA[m - 1]
        if (self.table[m][n-1] > self.table[m - 1][n]):
            return self.backtrack(m,n-1)
        return self.backtrack(m-1, n);
        """
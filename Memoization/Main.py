from LCS_memoization import LCS_memoization

def main():

    lcs = LCS_memoization("AGGTABAGGTABAGGTABAGGTAB","GXTXAYBGXTXAYBGXTXAYBGXTXAYBGXTXAYB")
    lcs.get_lcs_len_memoization()

if __name__ == '__main__':
    main()

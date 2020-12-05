from LCS_recursive import LCS_recursive

def main():
    
    lcs = LCS_recursive("AB  ", "ACBAALKBAB ")
    lcs.get_lcs_len_recursive()

if __name__ == '__main__':
    main()

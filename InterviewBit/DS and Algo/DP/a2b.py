# Problem from HackerRank: DP - Abbreviation


# Complete the abbreviation function below.
def abbreviation(a, b):
    ''' check a can converted to b '''
    na = len(a)
    nb = len(b)
    #  we want to calculate the matrix V[i,j]
    # V[i,j] == can a[:i] be converted to b[:j], i=0..,na, j=0,..,nb
    # to calculate V[i,j] we need V[i-1,j] and V[i-1,j-1]
    # we calculate on row at a time to save memory
    # Init first row:: V[0,:], i.e, a=="", in this case b[:j] can only be converted if it is empty
    row = [False for _ in range(nb+1)]
    row[0] = True # if a==b==""
    for i in range(1, na+1):
        prev_row = row.copy()
        for j in range(nb+1):
            row[j] = (a[i-1].islower() and prev_row[j]) \
                      or (j > 0 and a[i-1].upper() == b[j-1] and prev_row[j-1])
    # finally, check if a[:na+1] can be converted to b[:nb+1]
    if row[-1]:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    
    print(abbreviation.__doc__)
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)

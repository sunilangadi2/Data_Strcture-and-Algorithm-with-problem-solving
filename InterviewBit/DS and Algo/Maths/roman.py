

def to_roman(n):
    st = ''
    if n <= 0:
        return st
    if n > 10000:
        print("Crossed maximum limit.")
        return st
    d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    limits = [1, 5, 10, 50, 100, 500, 1000, 10001]
    #d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for l in range(len(limits)):
        if (n >= limits[l] and n < limits[l+1]):
            for x in range(l+1):
                if n == limits[l+1] - limits[x]:
                    st += d[limits[x]]
                    st += d[limits[l+1]]
                    return st
            while(n >= limits[l]):
                st += d[limits[l]]
                n -= limits[l]
            st += to_roman(n)
    return st


print to_roman(1)
print to_roman(3)
print to_roman(8)
print to_roman(51)
print to_roman(49)
print to_roman(19)
print to_roman(4)
print to_roman(489)

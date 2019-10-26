class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(a, b):
        ret = []
        for i in range(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret

    print(rotateArray([1,2,3,4,5],2))

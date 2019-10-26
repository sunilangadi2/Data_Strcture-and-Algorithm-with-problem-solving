# For problem statement look at Hacker-Rank

# In this greedy method by sorting the contestant with max value

# Complete the luckBalance function below.
def luckBalance(k, contests):

    # sort from greatest luck to least luck
    contests.sort(reverse=True)

    luck, important = 0, 0

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif important < k:
            luck += contest[0]
            important += 1
        else:
            luck -= contest[0]

    return luck


if __name__ == '__main__':
    
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)
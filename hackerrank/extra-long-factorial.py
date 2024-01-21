def extraLongFactorials(n):
    memo = [0 for _ in range(n)]
    memo[0] = 1

    for i in range(1, n):
        memo[i] = (i+1) * memo[i-1]

    print(memo[-1])
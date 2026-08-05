a = input("Enter your first word:")
b = input("Enter your second word:")
def lcs(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if x[i] == y[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    i, j = 0, 0
    result_chars = []
    while i < m and j < n:
        if x[i] == y[j]:
            result_chars.append(x[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    print("Your LCS is:", "".join(result_chars))

lcs(a, b)
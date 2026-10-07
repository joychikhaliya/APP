def count_ways(coins, target):
    # dp[i] = number of ways to make amount i
    dp = [0] * (target + 1)
    dp[0] = 1  # one way to make 0: use no coins

    # Outer loop over coins ensures combinations (not permutations) are counted
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]


def main():
    coins = list(map(int, input("Enter coin denominations (space-separated): ").split()))
    target = int(input("Enter target amount: "))

    if target < 0 or any(c <= 0 for c in coins):
        print("Please enter positive coin values and a non-negative target.")
        return

    coins = sorted(set(coins))  # remove duplicates
    print(f"Total possible combinations: {count_ways(coins, target)}")


if __name__ == "__main__":
    main()

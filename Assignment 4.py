def fib_memo(n, memo=None):
    # Initialize the memoization dictionary on the first call
    if memo is None:
        memo = {}
        
    # Check the lookup table (cache) first
    if n in memo:
        return memo[n]
        
    # Base cases
    if n <= 1:
        return n
        
    # Compute, store in memo, and return
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
  
def fib_tabulation(n):
    if n <= 1:
        return n
        
    # Create an array to store intermediate results
    dp = [0] * (n + 1)
    
    # Initialize the base states
    dp[0] = 0
    dp[1] = 1
    
    # Fill the table iteratively from the bottom up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

print(fib_tabulation(10))  # Output: 55
print(fib_memo(10))  # Output: 55

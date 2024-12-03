def count_ways_to_make_change(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1 

    for coin in coins: 
        for amount in range(coin, target + 1): 
            dp[amount] += dp[amount - coin]

    return dp[target]  


target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(count_ways_to_make_change(target,coins))
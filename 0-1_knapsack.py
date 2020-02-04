def knapsack(wt, price, n, weight):
    if weight == 0 or n == 0:
        return 0
    
    if wt[n-1] > weight:
        return knapsack(wt, price, n-1, weight)
    
    return max(knapsack(wt, price, n-1, weight),
               price[n-1] + knapsack(wt, price, n-1, weight-wt[n-1]))

wt = [2, 7, 3, 4]
price = [5, 20, 20, 10]
n = 4
weight = 11

print(knapsack(wt, price, n, weight))
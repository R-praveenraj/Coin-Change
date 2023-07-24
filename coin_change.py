def coin_change(coins,amount):
    collected_coins= {}
    def min_coins_needed(amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in collected_coins:
            return collected_coins[amount]
        min_coins = float('inf')
        for i in coins:
            remaining_coins=min_coins_needed(amount-i)
            if remaining_coins>=0:
                min_coins = min(min_coins, remaining_coins + 1)
        collected_coins[amount] = min_coins if min_coins != float('inf') else -1
        return collected_coins[amount]
    return min_coins_needed(amount)

coins=list(map(int,input().split()))
amount=int(input())
print(coin_change(coins,amount))
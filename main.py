import timeit

def find_coins_greedy(amount):
    '''Функція жадібного алгоритму'''
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    '''Функція динамічного програмування'''
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    last_coin = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

# Приклади для перевірки ефективності
amount = 113
greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1)
dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1)
print(f"Сума: {amount}")
print()
print(f"Жадібний алгоритм: {greedy_time:.6f} секунд")
print(find_coins_greedy(amount))
print()
print(f"Динамічне програмування: {dp_time:.6f} секунд")
print(find_min_coins(amount))
print()

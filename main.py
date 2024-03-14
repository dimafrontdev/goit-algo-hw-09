def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            coin_count[coin] = count
        if amount == 0:
            break
    return coin_count


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    result = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i >= coin and min_coins[i] == min_coins[i - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                i -= coin
                break
    return result


import timeit

test_amounts = [113, 567, 1124, 5678, 11245]

greedy_times = []
for amount in test_amounts:
    start_time = timeit.default_timer()
    find_coins_greedy(amount)
    greedy_times.append(timeit.default_timer() - start_time)

dp_times = []
for amount in test_amounts:
    start_time = timeit.default_timer()
    find_min_coins(amount)
    dp_times.append(timeit.default_timer() - start_time)


# Перетворення часу виконання в мілісекунди (мс)
greedy_times_ms_dynamic = [time * 1000 for time in greedy_times]
dp_times_ms_dynamic = [time * 1000 for time in dp_times]

# Формування таблиці результатів
results_table_dynamic = {
    "Test Amounts": test_amounts,
    "Greedy Times (ms)": greedy_times_ms_dynamic,
    "DP Times (ms)": dp_times_ms_dynamic,
}

print(results_table_dynamic)

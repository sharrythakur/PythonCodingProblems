def buy_sell_max(stock_prices):
    max_profit = 0
    min_price = stock_prices[0]

    for price in stock_prices:
        min_price = min(min_price, price)

        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit


if __name__ == '__main__':
    price = [1, 5, 2, 3, 7, 6, 4, 5]
    print(buy_sell_max(price))

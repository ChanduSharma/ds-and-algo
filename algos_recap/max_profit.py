def max_profit(prices):
    min_buy = float('inf')
    max_pro = 0

    for price in prices:
        min_buy = min(min_buy, price)
        max_pro = max(max_pro, price - min_buy)
    
    return max_pro


if __name__ == '__main__':
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print(max_profit(prices))
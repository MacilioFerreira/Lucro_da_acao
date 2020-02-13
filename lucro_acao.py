#!/usr/bin/env python
# coding: utf-8


def read_vector_prices(prices):
    prices_ = []
    for p in prices:
        if p != ' ':
            prices_.append(int(p))
    return prices_

def get_best_benefit(prices):
    purchase_day_action = min(prices)
    purchase_day_index = prices.index(purchase_day_action)
    sell_day_action = max(prices[purchase_day_index:]) 

    if sell_day_action != None:
        return sell_day_action - purchase_day_action
    else:
        return 0


if __name__ == "__main__":
    prices = read_vector_prices(list(input()))
    print(get_best_benefit(prices))


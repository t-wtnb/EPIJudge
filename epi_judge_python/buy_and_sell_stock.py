from selectors import EpollSelector
from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    tmp_min = float('inf')
    max_diff = float('-inf')
    for p in prices:
        tmp_min = min(tmp_min, p)
        max_diff = max(max_diff, p - tmp_min)
    return max_diff
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))

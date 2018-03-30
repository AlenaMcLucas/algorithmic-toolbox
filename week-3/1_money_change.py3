# Goal: Find the minimum number of coins needed to change the input value into coints with denominations 1, 5, and 10.
# Input: integer m
# Constraints: 1 <= m <= 10^3
# Output: minimum number of oins with denomiantions, 1, 5, 10 that changes m.

import sys

def get_change(m):
    coin_count = 0
    [coins, remainder] = check_change(m,10)
    coin_count += coins
    [coins, remainder] = check_change(remainder,5)
    coin_count += coins + remainder
    return coin_count

def check_change(n, check):
	coins = int(n / check)
	remainder = n % check
	return [coins,remainder]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

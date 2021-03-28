# Uses python3
import sys

def get_change(money):
    #write your code here
    min_num_coins = [0 for i in range(0,money+1)]
    print('Min Num Coins',min_num_coins)
    for m in range(1,money+1):
        print('**********************************')
        print('M is',m)
        min_num_coins[m] = sys.maxsize
        for i in 1,3,4:
            print('For coin',i)
            if m >= i:
                num_coins = min_num_coins[m-i] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
                print('Num coins',num_coins,'=',min_num_coins[m-i],'+ 1','--------------Min Num Coins[',m,'] is',min_num_coins[m])
    print('Min Num Coins',min_num_coins)
    return min_num_coins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

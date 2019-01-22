# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
import winsound
import time

p = False
f = 500

def main():
    winsound.Beep(f,200)
    start = time.time()
    coins = {1:0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0}
    count = len(coins);
    keys = list(coins.keys())
    desired = keys[len(keys)-1]
    if p:
        print(keys)
    while (coins[keys[0]] < desired/keys[0]):
        if p:
            print(coins)
        sum = 0
        for i in keys:
            sum+= coins[i]*i
        if(sum==desired):
            count+=1
        tmpIndex = len(keys)-1
        coins[keys[tmpIndex]]+=1
        while tmpIndex > 0:
            if(coins[keys[tmpIndex]] >= desired/keys[tmpIndex]):
                coins[keys[tmpIndex]] = 0
                coins[keys[tmpIndex-1]]+=1
            tmpIndex-=1
    print(count)
    end = time.time()
    winsound.Beep(f,200)
    print("this operation took : " + str(end-start)+" seconds")

if __name__ == '__main__':
    main()

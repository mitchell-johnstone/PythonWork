# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def main():
    highest = 0
    for i in range(100):
        for j in range(100):
            s = sum(int(d) for d in str(i**j))
            if(highest < s):
                highest = s
    print(highest)

if __name__ == '__main__':
    main()

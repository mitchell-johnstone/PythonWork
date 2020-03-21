def findNewA(n, c, d):
    count = 0
    while (n ** .5 + c) / d > 1:
        count += 1
        c -= d
    return count


def findSequence(n):
    a = [n ** .5 // 1]
    c = a[0]
    den = n - c ** 2
    # sqrt(23) + 4 / 7

    while den != 1:
        if len(a)>1:
            c *= -1
            den = (n - c ** 2) / den
        newA = findNewA(n, c, den)
        a += [newA]
        c -= den * newA

    return a[1:]


def run():
    count = 0
    squares = [i ** 2 for i in range(100)]
    for n in range(10000):
        if n not in squares:
            if not findSequence(n) or len(findSequence(n)) % 2 == 1:
                count += 1
    return count


def main():
    print(run())


if __name__ == '__main__':
    main()

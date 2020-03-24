import math


def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return 0
    x, y = 1, n
    while x + 1 < y:
        mid = (x + y) // 2
        if mid ** 2 < n:
            x = mid
        else:
            y = mid
    return n == x ** 2 or n == (x + 1) ** 2


def v1():
    squares = [i ** 2 for i in range(1, 100)]
    largestXSqr = 0
    goldenD = 0
    for D in range(2, 1001):
        if D not in squares:
            print(D)
            # x = 2
            # found = False
            # while not found:
            #     xSqr = x**2
            #     ySqr = int((xSqr-1)/D)
            #     y = math.sqrt(ySqr)
            #     # if D == 61:
            #     #     print(x)
            #     if (int(y + .5)) ** 2 == ySqr:
            #         if xSqr >= largestXSqr:
            #             largestXSqr = xSqr
            #             goldenD = D
            #             # print(str(goldenD) + " " + str(largestXSqr))
            #         found = True
            #     x += 1

            y = 1
            found = False
            while not found and y < 99999:
                ySqr = int(y ** 2)
                # print("\t", ySqr)
                xSqr = int(1 + D * ySqr)
                # if D == 61:
                #     print(x)
                if is_square(xSqr):
                    if xSqr >= largestXSqr:
                        largestXSqr = xSqr
                        goldenD = D
                        print(str(goldenD) + " " + str(largestXSqr))
                    found = True
                y += 1
    print("X^2 = " + str(largestXSqr) + " = " + str(largestXSqr ** .5) + "^2")
    print("D value was " + str(goldenD))


def v2():
    squares = [i ** 2 for i in range(1, 100)]
    largestXSqr = 0
    goldenD = 0
    for D in range(2, 1001):
        if D not in squares:
            print(D)
            x = 2
            found = False
            while not found:
                xSqr = x ** 2
                ySqr = int((xSqr - 1) / D)
                y = math.sqrt(ySqr)
                # if D == 61:
                #     print(x)
                if (int(y + .5)) ** 2 == ySqr:
                    if xSqr >= largestXSqr:
                        largestXSqr = xSqr
                        goldenD = D
                        # print(str(goldenD) + " " + str(largestXSqr))
                    found = True
                x += 1
    print("X^2 = " + str(largestXSqr) + " = " + str(largestXSqr ** .5) + "^2")
    print("D value was " + str(goldenD))


def v3():
    squares = [i ** 2 for i in range(35)]
    DVals = [i for i in range(1001) if i not in squares]
    x = 1
    while len(DVals) > 1:
        x += 1
        if x % 10000 == 0:
            print(x)
            print(len(DVals))
        for D in DVals:
            ySqr = (x ** 2 - 1) / D
            if x ** 2 - int(ySqr + .5) * D == 1 and is_square(int(ySqr + .5)):
                if D == 61:
                    print(D, " ", ySqr, " ", x ** 2)
                i = DVals.index(D)
                del DVals[i]
                # break
                # print(D)
    print(DVals)


def v4():
    DVals = [i for i in range(1, 1001) if not is_square(i)]
    y = 0
    largestXSqr = 0
    largestD = 0
    while len(DVals) > 0:
        y += 1
        ySqr = y ** 2
        if y % 10000 == 0:
            print("current Y=", y)
            print("D = ", len(DVals), DVals)
        for D in DVals:
            xSqr = 1 + D * ySqr
            if is_square(xSqr):
                if xSqr > largestXSqr:
                    largestD = D
                    largestXSqr = xSqr
                print("Eliminated D=", D, " XSqr=", xSqr)
                i = DVals.index(D)
                del DVals[i]
    # print(DVals)
    print(largestXSqr)
    print(largestD)


def findNewA(n, c, d):
    count = 0
    while (n ** .5 + c) / d > 1:
        count += 1
        c -= d
    return count


def findSequence(n):
    a = [int(n ** .5 // 1)]
    c = a[0]
    den = n - c ** 2
    # sqrt(23) + 4 / 7

    while len(a) == 1 or den != 1:
        if len(a) > 1:
            c *= -1
            den = (n - c ** 2) / den
        newA = findNewA(n, c, den)
        a += [newA]
        c -= den * newA

    return a


# Alright, so I did some more research, and it turns out that the x ** 2 - D * y ** 2 = 1
# is actually a "Pell equation". The minimal solution for x is found as x/y, with x/y being a convergent
# of the continued fraction that represents the square root of n. Look at 64 and 65 for background
def v5():
    DVals = [i for i in range(2, 1001) if not is_square(i)]
    largest = [0, 0]  # [x,D]
    for D in DVals:
        seq = findSequence(D)
        print(seq)
        seqI = 1
        h = [seq[0], seq[0] * seq[1] + 1]
        k = [1, seq[1]]
        i, x, y = 1, h[1], k[1]
        while x ** 2 - D * (y ** 2) != 1:
            seqI += 1
            if seqI == len(seq):
                seqI = 1
            h += [seq[seqI] * h[len(h) - 1] + h[len(h) - 2]]
            k += [seq[seqI] * k[len(k) - 1] + k[len(k) - 2]]
            i += 1
            x, y = h[i], k[i]
            print(x,y)
        if x > largest[0]:
            largest[0] = x
            largest[1] = D
        print("Done with D=", D)
    print(largest)


def main():
    v5()
    # print(findSequence(2))

if __name__ == '__main__':
    main()

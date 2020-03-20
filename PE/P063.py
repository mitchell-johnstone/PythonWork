def solve():
    power = 1
    count = 0
    while len(str(9 ** power)) == power:
        print("power " + str(power))
        for base in range(9, 0, -1):
            print("base " + str(base))
            if len(str(base ** power)) == power:
                count += 1
            else:
                break
        power += 1
    return count


def main():
    print(solve())


if __name__ == '__main__':
    main()

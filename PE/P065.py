def main():
    sequence = [2]
    k = 1
    while (len(sequence) < 100):
        sequence += [1, 2 * k, 1]
        k += 1
    sequence = sequence[:100]
    print(sequence)
    num = 1
    den = sequence[len(sequence) - 1]
    for i in range(len(sequence) - 2, 0, -1):
        num += sequence[i] * den
        num, den = den, num
    num += sequence[0] * den
    print(num)
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum)


if __name__ == '__main__':
    main()

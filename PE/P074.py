
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

#   1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

#       169 ---> 363601 ---> 1454 ---> 169
#       871 ---> 45361 ---> 871
#       872 ---> 45362 ---> 872

#       It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

#       69 ---> 363600 ---> 1454 ---> 169 ---> 363601 (---> 1454)
#       78 ---> 45360 ---> 871 ---> 45361 (---> 871)
#       540 --> 145 (--> 145)

#       Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

#       How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?


def sum_fact_digits(n, f):
    return sum(f[int(i)] for i in list(str(n)))


def main():
    facts = [1,1,2,6,24,120,720,5040,40320,362880]
    count = 0
    for start in range(3,10**6):
        chain = [start]
        curNum = sum_fact_digits(start, facts)
        good = True
        while curNum not in chain and good:
            chain += [curNum]
            curNum = sum_fact_digits(curNum, facts)
            if len(chain)>60:
                good = False
        if len(chain) == 60 and good:
            count+=1
    print(count)


if __name__ == "__main__":
    main()

# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact,
# 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

# Instead of trying to permute a certain cube in every possible way, I will make a dictionary of the number
# and its cube. Then, after collecting a large amount, I will take their cubes and sort alphabetically as strings,
# which will allow me to see if certain cubes use the same digits and, thus, are permutations of one another.


def findSmallest(target):
    smallestCubes = {}
    i = 1
    while True:
        # Get the actual cube
        cube = str(i ** 3)
        # Put the cube digits into alphabetical order
        sCube = str(sorted(cube))

        # check if we've already found that permutation
        if sCube in smallestCubes.keys():
            # increase the number of primes with that permutation by 1
            smallestCubes[sCube][1] += 1
            # if we have reached the target, return the smallest cube with that permuation
            if smallestCubes[sCube][1] == target:
                print("Smallest cube with 5 cubes as permutations: " + smallestCubes[sCube][0])
                return

        # If we haven't had this permutation, record it
        else:
            # keep cube as the first index because it is the lowest cube with that specific permutation
            smallestCubes[sCube] = [cube, 1]
        i += 1


def main():
    findSmallest(5)


if __name__ == '__main__':
    main()

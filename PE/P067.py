def main():
    # 2D array for holding numbers in triangle
    triangle = []

    # Read the file and import the numbers into the array
    f = open("P067_triangle.txt")
    for line in f:
        triangle += [[int(i) for i in line.split()]]
    # print(triangle)

    # Since there's 100 lines in the triangle, start at line 99
    # Each line has the same number of indices as the line #
    for line in range(98, -1, -1):
        for position in range(line+1):
            # If the left one is greater than the right one, add the left. Otherwise, add the right
            triangle[line][position] += triangle[line + 1][position] if triangle[line + 1][position] > \
                                        triangle[line + 1][position + 1] else triangle[line + 1][position + 1]
    print(triangle)


if __name__ == '__main__':
    main()

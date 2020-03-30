# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
#
# Working clockwise, and starting from the group of three with the numerically lowest external node
# (4,3,2 in this example), each solution can be described uniquely. For example,
# the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
#
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
#
# Total	Solution Set
# 9	4,2,3; 5,3,1; 6,1,2
# 9	4,3,2; 6,2,1; 5,1,3
# 10	2,3,5; 4,5,1; 6,1,3
# 10	2,5,3; 6,3,1; 4,1,5
# 11	1,4,6; 3,6,2; 5,2,4
# 11	1,6,4; 5,4,2; 3,2,6
# 12	1,5,6; 2,6,4; 3,4,5
# 12	1,6,5; 3,5,4; 2,4,6
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
#
# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
# What is the maximum 16-digit string for a "magic" 5-gon ring?
from decorators import *
from itertools import permutations


# a,b,c; d,c,e; f,e,g; h,g,i; j,i,b
def create_nodes(perm):
    nodes = [0] * 15
    nodes[0] = perm[0]
    nodes[1] = nodes[14] = perm[1]
    nodes[2] = nodes[4] = perm[2]
    nodes[3] = perm[3]
    nodes[5] = nodes[7] = perm[4]
    nodes[6] = perm[5]
    nodes[8] = nodes[10] = perm[6]
    nodes[9] = perm[7]
    nodes[11] = nodes[13] = perm[8]
    nodes[12] = perm[9]
    return nodes


def list_to_string(list_of_nums):
    return "".join([str(i) for i in list_of_nums])


@timer
def main():
    # Get all permutations of list
    all_perm = list(permutations([i for i in range(1, 11)]))

    for perm in all_perm:
        nodes = create_nodes(perm)

        # First condition: start with the smallest external node
        # if first node > 6, then all further permutations can't work
        if nodes[0] > 6:
            break
        if nodes[0] < min([nodes[3], nodes[6], nodes[9], nodes[12]]):
            # Second condition: each triplet adds to the same total
            total = sum(nodes[0:3])
            if total == sum(nodes[3:6]):
                if total == sum(nodes[6:9]):
                    if total == sum(nodes[9:12]):
                        if total == sum(nodes[12:]):
                            print("Found a new max: ", list_to_string(nodes))
                            print("Total was: ", total)


if __name__ == '__main__':
    main()

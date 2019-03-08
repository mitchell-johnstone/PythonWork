# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

#method to check if the values make a right triagle
def isRightTriangle(n):
    a = n[0]
    b = n[1]
    c = n[2]
    #pythagruim theorum
    return a**2 + b**2 == c**2

def main():
    #array to hold perimeters
    p = [0]*1001

    #array to hold the sides of the triangles
    #val[0]<val[1]<val[2]
    vals = [0,0,3]

    #only loop to 500, because after that, the sides can never make a triangle
    for i in range(3,500):
        # print(i)
        vals[2] = i
        vals[1] = 2

        #loop the second value until it gets to the hypotenuse
        while(vals[1]<vals[2]):
            vals[0] = 1

            #first value must always be lower than the second
            while(vals[0]<vals[1]):
                # print(vals)

                #check if the first + second > first
                #that makes it a real triange
                if(vals[0] + vals[1] > vals[2]):
                    #check if it is a right triangle
                    if(isRightTriangle(vals)):
                        p[sum(vals)]+=1
                vals[0]+=1
            vals[1]+=1

    highest = 0
    #loop through, find which value of p is the highest
    for i in range(1001):
        if(p[i]>p[highest]):
            highest = i
    print(highest)

if __name__ == '__main__':
    main()

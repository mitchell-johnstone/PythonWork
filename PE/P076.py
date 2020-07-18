def refill( N, splitList ):
    target = splitList.pop()
    while target == 1: target = splitList.pop()
    target -= 1
    s = sum(splitList)
    splitList += [target] * ((N-s)//target)
    r = (N-s) % target
    if r != 0: splitList += [r]

def v1():
    splitList = [100]
    count = 0
    while splitList[0] != 1:
        refill( 100, splitList )
        print(splitList)
        count += 1
    print(count)

Pn = [1]
def calcP(n):
    n = int(n)
    print(Pn)
    if n < 0: return 0
    if Pn[n] > 0: return Pn[n]
    P = 0
    for k in range(1,n): #int(n**.5)):
        n1 = n - k*(3*k-1)/2
        n2 = n - k*(3*k+1)/2
        Pn1 = calcP(n1)
        Pn2 = calcP(n2)
        if k%2 ==1: P += (Pn1 + Pn2)
        else: P-=(Pn1+Pn2)
    while len(Pn) <= n:
        Pn += [0]
    Pn[n] = P
    return P

def improvement(n):
    print(sum([calcP(i) for i in range(1,n+1)]))

def main():
    #v1()
    improvement(100)

if __name__ == "__main__":
    main()

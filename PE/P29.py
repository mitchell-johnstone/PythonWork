
def main():
    max = 100
    originals = [];
    a  = 2
    while a < max+1:
        b = 2
        while b < max+1:
            if a**b not in originals:
                originals = originals + [a**b]
            b+=1
        a+=1
    print(len(originals))

if __name__ == '__main__':
    main()

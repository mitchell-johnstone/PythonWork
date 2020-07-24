from turtle import *
from math import *
from time import sleep


def drawKoch(n,l,x,y,a):
    if n == 0:
        goto(x,y)
        setheading(a)
        down()
        forward(l)
        up()
    else:
        l//=3
        n-=1
        degrees = [60,-120,60]
        for d in degrees:
            drawKoch(n,l,x,y,a)
            x+=l*cos(radians(a))
            y+=l*sin(radians(a))
            a+=d
        drawKoch(n,l,x,y,a)


def main():
    ht()
    up()
    speed('fastest')
    tracer(0,0)
    while True:
        for i in range(7):
            clear()
            begin_fill()
            l = 3**5
            d = l*3**.5
            drawKoch(i,d,l*cos(radians(150)),l*sin(radians(150)),0)
            drawKoch(i,d,l*cos(radians(30)),l*sin(radians(30)),-120)
            drawKoch(i,d,0,l*sin(radians(270)),120)
            end_fill()
            update()
            sleep(2)
    done()


if __name__ == "__main__":
    main()

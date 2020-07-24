from tkinter import *
from turtle import *
import time


def grow(n,l,a,t1):
    if n != 0:
        t1.fd(l)
        t2 = t1.clone()
        t1.lt(a)
        t2.rt(a)
        t2.ht()
        l//=2
        n-=1
        grow(n,l,a,t1)
        grow(n,l,a,t2)


def main():
    screen = Screen()
    ht()
    def grow_helper(temp):
        clearscreen()
        screen.tracer(0,0)
        tree = Turtle()
        tree.ht()
        speed('fastest')
        tree.pu()
        tree.goto(0,-300)
        tree.pd()
        tree.setheading(90)
        grow(n.get(), l.get(), deg.get(), tree)

        update()
    # code for 2 sliders, one vertical, one horizontal
    master = Tk()
    n = Scale(master, from_=1, to=9, command=grow_helper)
    n.pack()
    deg = Scale(master, from_=0, to=180, orient=HORIZONTAL, command=grow_helper)
    deg.pack()
    l = Scale(master, from_=2**6, to=2**9, command=grow_helper)
    l.pack()
    # Button(master, text='Draw', command=grow_helper).pack()

    mainloop()

if __name__ == "__main__":
    main()

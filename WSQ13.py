import math

x1= int(input("X1 position: "))
y1= int(input("Y1 position: "))
x2= int(input("X2 position: "))
y2= int(input("Y2 position: "))

def distance (x1,y1,x2,y2):
    h=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return h

print("The distance between (",x1,",",y1,") and (",x2,",",y2,") is:","%.2f"%distance(x1,y1,x2,y2))


def superpower (b,p):
    c=1
    num=b
    while(c<p):
        num=num*b
        c=c+1
    return num
b= int(input("Base: "))
p= int(input("Power: "))

print(superpower(b,p))


def figure ():
    size = int(input("Give me the size: "))
    s = " "

    for n in range (size):
        s = s + "T"
        print (s)

    for n in range (size):
        s = s[:-1]
        print (s)

figure()


n=int(input("Type a number: "))

def fibonnaci (n):
    x = 0
    y = 1
    z = 0

    for a in range (n-1):
        z = x + y
        x = y
        y = z
        print (z)
    return

fibonnaci (n)

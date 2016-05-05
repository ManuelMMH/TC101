import math
x1=int(input("Type the first ""x"" point: "))
y1=int(input("Type the first ""y"" point: "))
x2=int(input("Type the second ""x"" point: "))
y2=int(input("Type the first ""y"" point: "))

def Distance (x1,y1,x2,y2):
    p=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return p

print (Distance(x1,y1,x2,y2))

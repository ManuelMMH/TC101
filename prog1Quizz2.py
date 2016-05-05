p1=int(input("Give me a number: "))
p2=int(input("Give me another number: "))

def superpower(p1,p2):
    n=1
    for i in range(p2):
        n=n*p1
    return n

print(superpower(p1,p2))

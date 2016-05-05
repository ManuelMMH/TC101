def gcd(a,b):
    if (a == b):
        return (a)
    else:
        if(a > b):
            return (gcd(a-b,b))
        else:
            return (gcd(a,b-a))

a = int(input("Type the first number: "))
b = int(input("Type the second number: "))
gcd(a,b)
print("The Greatest Common Denominator is: ",gcd(a,b))

a=int(input("Give me a number: "))
b=int(input("Give me another number: "))

def remainder (a,b):
    print ("The remainder of the integer division between",a, "and" ,b, "is =" , a % b)

def substraction (a,b):
    print (a,"-",b,":",a-b)

def multiplication (a,b):
    print (a,"*",b,":",a*b)

def integerdivision (a,b):
    print (a,"/",b,":",a//b)

remainder (a,b)
substraction (a,b)
multiplication (a,b)
integerdivision (a,b)

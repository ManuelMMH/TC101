n=int(input("Type a number: "))

def stars(n):
    s = ""
    a = 0
    while n > a:
        n = n - 1
        s = s + "*"
    else:
        print (s)

stars(n)

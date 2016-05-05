def factorial():
    while True:
        try:
            n = int(input("Enter a non-negative integer:"))
            if (n <= 0):
                print("Non-negative number and different from 0 please.")
            else:
                break
        except ValueError:
            print("INTEGER number please.")

    factorial = 1
    for x in range(n):
        factorial = factorial * n
        n = n-1
    print ("The factorial number of is: ", factorial)

factorial()

while True:
    a = input("Wanna try another number? (yes/no)")
    if(a == "yes"):
        factorial()
    elif (a == "no"):
        print ("All right, thanks.")
        break

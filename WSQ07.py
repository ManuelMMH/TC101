while True:
    try:
        lb=int(input("Please give us a lower bound: " ))
        hb=int(input("Now, give us a higher bound: "))
        total=0

    except ValueError:
        print ("Only integers, please.")
        break
    if lb > hb:
        print ("Your lower bound is higher than the higher bound. Please try again.")
        break
    elif lb == hb:
        print ("Your lower and higher bounds are equial. Please try again.")
        break

    else:
        for x in range (lb,hb+1):
            total= total + x
        print ("The sum from your lower bound,", lb, "to your higher bound,", hb, "is: ", total)
        break

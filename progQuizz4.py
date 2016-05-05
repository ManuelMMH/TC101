def euler_calc(precision):
    e = 2
    for i in range(1,precision+1):
        e = (1 + 1/i)**i
    e = str(e)
    return(e[:precision + 2])

print(euler_calc(4))

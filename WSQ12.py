def finder (word):
    f = open("test.txt")
    text = f.read()
    list = text.split(" ")
    count = 0

    for n in list:
        print (n)
        if(n.lower()==word):
            count+= 1
    return count

word = input("Type the word you are looking for: ")
print ("Times found: ",finder(word))

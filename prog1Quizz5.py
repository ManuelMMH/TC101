w = str(input("Type a word: "))
w = w.lower()
def is_palindrome(w):
    t = w[::-1]

    if (w==t):
        print ("True")

    else:
        print ("False")

is_palindrome(w)

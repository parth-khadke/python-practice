def checkPallindrome(word):
    rev = word[::-1]
    if rev == word:
        return True
    else:
        return False

word = input("Enter a word : ")

if checkPallindrome(word):
    print("Pallindrome")
else:
    print("Not Pallindrome")
string=input("Enter a string: ")
'''
string=string.strip()
n=0
for char in string:
    if char==" ":
        n+=1

print(f"The string has {n+1} words.")
'''

words=string.split()
print(words)
print(f"The string has {len(words)} words.")

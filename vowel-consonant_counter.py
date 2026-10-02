print("*** Character type checker ***")
vowel=0
consonant=0
digits=0
special=0
string=input("Enter a string: ")
string=string.lower()
for char in string:
    if char==" ":
        continue
    elif char.isdigit():
        digits+=1
    elif char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        vowel+=1
    elif char=="," or char=="." or char=="#" or char=="&":
        special+=1
    else:
        consonant+=1

print("Number of consonants: ", consonant)
print("Number of vowels: ", vowel)
print("Number of digits: ", digits)
print("Number of special chars: ", special)

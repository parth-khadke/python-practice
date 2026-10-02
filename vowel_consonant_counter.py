vowels=0
consonants=0
string=input("Enter a string: ")
string=string.lower()
for char in string:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        vowels+=1
    elif char=="," or char=="." or char=="#" or char=="&" or char=="!" or char==" ":
        pass
    else:
        consonants+=1

print("Number of vowels in string: ",vowels)
print("Number of consonants in string: ",consonants)
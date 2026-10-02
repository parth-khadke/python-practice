char_dict={}
string=input("Enter a string: ")
string=string.lower()
for ch in string:
    if ch==' ':
        continue

    if ch not in char_dict:
        char_dict[ch]=1
    else:
        char_dict[ch]+=1
    
for char, count in char_dict.items():
    print(f"{char}: {count}")
def encrypt(msg):
    cypher_letters= []
    for char in msg:
        if char.isalpha():
            if char.islower():
                cypher_letters.append(chr((ord(char) - ord('a') + 3) % 26 + ord('a')))
            elif char.isupper():
                cypher_letters.append(chr((ord(char) - ord('A') + 3) % 26 + ord('A')))
        elif char.isdigit():
            cypher_letters.append(char)
        else:
            cypher_letters.append(char)

    encrypted = "".join(cypher_letters)
    return encrypted
        


msg = "hello, kalyani"

print(encrypt(msg))



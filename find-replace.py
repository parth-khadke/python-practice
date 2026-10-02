sentence=input("Enter a sentence:")
list=sentence.split()
word=input("Search for a word: ")
if word in list:
    replace=input("Word found!! Choose replacement: ")
    index=(list.index(word))
    list[index]=replace
    print(' '.join(list))
else:
    print("word not found")

'''
sentence = input("Enter a sentence: ")
word = input("Search for a word: ")
replace = input("Choose replacement: ")

new_sentence = sentence.replace(word, replace)
print(new_sentence)
'''
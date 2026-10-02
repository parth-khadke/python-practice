str = "the cat sat on the mat the cat"

words = str.split()

counter = {}

for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

sorted_desc = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
print(sorted_desc)
    
sentense = input("Enter a sentense:")

lowercase = sentense.lower()
split = lowercase.split()
original = set(split)
print(lowercase)

print(f"Total words in the sentense is {len(split)}")
print(set(lowercase))
print(f"Unique words are {len(original)}")


counts = {}

for word in split:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1

print(counts)
            
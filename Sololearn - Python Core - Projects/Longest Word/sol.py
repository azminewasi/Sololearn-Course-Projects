txt = input()

words=txt.split()
numOfWords=len(words)

wordLength=list()

for word in words:
    wordLength.append(len(word))

print(words[wordLength.index(max(wordLength))])
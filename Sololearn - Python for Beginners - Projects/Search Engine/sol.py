
text = input()
word = input()

def search(text,word):
    if word in text:
        return ("Word found")
    else:
        return ("Word not found")

print(search(text, word))
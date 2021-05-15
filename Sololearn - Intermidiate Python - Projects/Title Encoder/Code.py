file = open("/usercode/files/books.txt", "r")
BookNames=file.readlines()

for bookName in BookNames:
    words=bookName.split()
    code=""
    for word in words:
        code+=word[0]
    print(code)

file.close()
file = open("/usercode/files/books.txt", "r")

#your code goes here
data=file.readlines()

for line in data:
    line=line.strip()
    length=len(line)
    print(line[0]+str(length))

file.close()
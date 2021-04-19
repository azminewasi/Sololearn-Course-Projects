def concatenate(*args):
    return '-'.join(map(str, args)) 
    

print(concatenate("I", "love", "Python", "!"))
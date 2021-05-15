try:
    name = input()
    if len(name)>3:
        print("Account Created")
    else:
        raise valueError
    
except:
    print("Invalid Name")
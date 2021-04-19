import re
#your code goes here
number=input()
regEx = re.compile("^[0-9]{8}$");

if (number.startswith("1") or number.startswith("8") or number.startswith("9")) and regEx.match(number):
    print("Valid")
else:
    print ("Invalid")
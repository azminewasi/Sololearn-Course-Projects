class Stack:
    def __init__(self):
        self.items = []  
  
    def is_empty(self):
        return self.items == []
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        return list(self.items)
    

def balanced(expression):
  s = Stack()
  for letter in expression:
    if letter == "(":
      s.push('a')
    elif letter==")":
      if len(s.print_stack())==0:
          return False
      s.pop()
  if len(s.print_stack())==0:
    return True
  else:
    return False
    

print(balanced(input()))
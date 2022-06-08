class stack:
    def __init__(self, n):
        self.stack = []
        self.n = n

    def push(self, k):
        if len(self.stack) < n:
            self.stack.append(k)
        else:
            print("The stack is full.")

    def pop(self):
        if len(self.stack) == 0: # If the stack is empty then pop should do nothing
            print("The stack is empty.")
        else:
            self.stack.pop(-1) # delete the last element and return it
    
    def top(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


s = Stack()

s.push(5)
s.push(10)
s.push(15)
print(s.top())
s.pop()
print(s.top())


# Bracket Matching

# expression should only contain round brackets
expresion = input("Enter the brackets combination - ")

flag = True
s = stack()
for i in range(expression):
    if expression[i] == '(':
        s.push(expression[i])
    else:
        top = s.top()
        if top == '(':
            continue
        else:
            flag = False
            break


if flag == True and s.size() == 0:
    print("The expression is valid")
else:
    print("The expression is not valid")
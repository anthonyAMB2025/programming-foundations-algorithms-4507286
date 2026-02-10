# Example file for Programming Foundations: Algorithms by Joe Marini
# Use a stack to see if a programming statement is balanced


def is_balanced(thestr):
    strStack = []
    for c in thestr:
        if c in ['(','{','[']:
            strStack.append(c)

        if c in [')','}',']']:
            if len(strStack) == 0:
                return False
        
            test = strStack.pop()
            if test == ')' and c != '(':
                return False
            if test == ']' and c != '[':
                return False
            if test == '}' and c != '{':
                return False
            
    if len(strStack) > 0: 
        return False
                
    return True

test_statements = [
    "print('Hello World!')",
    "a(x[i]) == b(x[i])",
    "{c for c in a(x)}",
    "Hello!)",
    "(This is not [balanced)",
    "{{{[[(())]}}",
    "(",
    "}"
]

for statement in test_statements:
    print(f'{statement} balanced: {is_balanced(statement)}')

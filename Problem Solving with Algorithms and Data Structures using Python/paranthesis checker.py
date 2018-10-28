from pythonds.basic.stack  import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    
    while balanced and index < len(symbolString):
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
        
    if balanced and s.isEmpty():
        return True
    return False
        
    
    
    
print(parChecker('((()))'))
print(parChecker('(()'))
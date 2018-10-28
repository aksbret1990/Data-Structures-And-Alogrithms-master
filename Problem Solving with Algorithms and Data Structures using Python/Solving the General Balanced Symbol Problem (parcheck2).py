from pythonds.basic.stack  import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    
    while balanced and index < len(symbolString):
        symbol = symbolString[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(symbol, top):
                    balanced = False
        index += 1
        
    if balanced and s.isEmpty():
        return True
    return False

def matches(symbol, top):
    
    opens = '({['
    closes = ')}]'
    
    return opens.index(top) == closes.index(symbol)
        
    
    
    
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))


def add(x, y):
    return x + y

def mult(x, y):
    value = 0;
    for i in range(y):
        value += x
    return value

def div(x, y):
    if (y == 0):
        return "Cannot divide by 0"
    return x * 1.0 / y

def sub(x, y):
    return x - y

i = 1
while (i < 5):
    i = i + 1
    x = i
    y = 100 / i
    print "Added:\t",add(x,y)
    print "Multiplied:\t",mult(x,y)
    print "Divided:\t",div(x,y)



#!/usr/bin/env python3
import readline
import operator
from colorama import Fore, Back, Style
op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def calculate(arg):
    stack = arg.split()
    while len(stack) > 1:
        token = stack.pop()
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            func = op[token]
            result = func(val1,val2)
            stack.append(str(result))
    return int(stack[0])
def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result > 0:
            print(Fore.green + str(result))
        elif result < 0:
            print(Fore.red + str(result))
        else:
            print(result)

if __name__ == '__main__':
    main()

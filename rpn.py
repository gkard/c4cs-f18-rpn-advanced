#!/usr/bin/env python3
import math
from colored import fg, bg, attr

def calculate(arg):
    stack = [] 

    tokens = arg.split()

    for token in tokens:
        if token == 'q':
            exit(0)
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '^':
                result = math.pow(val1, val2)
            elif token == '*':
                result = val1 * val2

            stack.append(result)

    if len(stack) > 1:
        raise ValueError('Too many arguments on the stack')

    return stack[0]


def main():
    print('Type q <enter> at any time to quit')
    while True:
        try:            
            color = input('Type: red green yellow or blue: ')
            colorCode = 0
            if color == 'q':
                exit(0)
            elif color == 'red':
                colorCode = 1
            elif color == 'green':
                  colorCode = 2
            elif color == 'yellow':
                  colorCode = 3
            elif color == 'blue':
                  colorCode = 4
            result = calculate(input('rpn calc> '))
            print ('%s %d %s' % (fg(colorCode), result, attr(0)))
        except ValueError:
            pass

if __name__ == '__main__':
    main()

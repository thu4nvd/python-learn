#!/usr/bin/python3
#Retain the last n items using deque

__doc__ = '''
practice deque data structures
'''

from collections import deque


def search(lines, pattern, history=5):
    prevlines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prevlines
        prevlines.append(line)


def main():
    with open('deque.input', 'rt') as f:
        for line, prevlines in search(f, 'python', 6):
            for pline in prevlines:
                print('*{}'.format(pline))
            print('*Result: {}'.format(line))
            print('*'*30)


if __name__ == "__main__":
    main()
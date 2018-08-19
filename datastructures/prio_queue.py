#!/usr/bin/python3
#implementation of priority queue using heapq

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


def main():
    #routine to test Priority Queue
    q = PriorityQueue()
    q.push(Item('An'), 12)
    q.push(Item('Binh'), 2)
    q.push(Item('Cuong'), 3)
    q.push(Item('Duc'), 6)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

if __name__ == "__main__":
    main()
#!/usr/bin/python3
#Implemention of multi dict that maps keys to more than one value

from collections import defaultdict

def main():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(3)
    print(d)

    e = defaultdict(set)
    e['a'].add(1)
    e['a'].add(2)
    e['b'].add(3)
    print(e)

    #default dict auto add key if not yet exist

if __name__ == "__main__":
    main()
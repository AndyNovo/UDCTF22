#!/usr/bin/env python2.7
import random
def rotl(n, k):
    return ((n << k) | (n >> (64-k))) & 0xffffffffffffffff

flag = "REDACTED"

def main():
    a=random.randint(0,2**63)
    b=random.randint(0,(2**32) -1)
    print("Welcome to the future of seed cracking, targets: %d %d\n" % (a,b))
    try:
        s=[int(raw_input("Feed me state_%d:" % (i))) for i in range(2)]
    except:
        print("Invalid state values, positive ints please")
        exit(1)
    def next():
        s0=s[0]
        s1=s[1]
        res = (rotl(s0 + s1, 17) + s0) & 0xffffffffffffffff
        s1= s1 ^ s0
        s[0] = (rotl(s0,49) ^ s1 ^ (s1 << 21)) & 0xffffffffffffffff
        s[1] = rotl(s1, 28)
        return res
    for _ in range(10000):
        next()
    if not next()==a:
        print("you lose at a")
        exit(1)
    if not (next() % 2**32) ==b:
        print("you lose at b")
        exit(1)
    print("well done")
    print(flag)
    exit(0)

if __name__ == "__main__":
    main()

#!/usr/bin/env python2.7
import random
def rotl(n, k):
    return ((n << k) | (n >> (32-k))) & 0xffffffff

flag = "UDCTF{wh04_p3rh4ps_th3_futur3_h4s_h0pe}"

def main():
    a=random.randint(0,2**31)
    b=random.randint(0,2**31)
    c=random.randint(0,2**31)
    try:
        s=[int(raw_input("Feed me state_%d:" % (i))) for i in range(4)]
    except:
        print("Invalid state values, positive ints please")
        exit(1)
    def next():
        res = (rotl(s[0] + s[3], 7) + s[0]) & 0xffffffff
        t = (s[1] << 9) & 0xffffffff
        s[2] = (s[2] ^ s[0]) & 0xffffffff
        s[3] = (s[3] ^ s[1]) & 0xffffffff
        s[1] = (s[1] ^ s[2]) & 0xffffffff
        s[0] = (s[0] ^ s[3]) & 0xffffffff
        s[2] = (s[2] ^ t) & 0xffffffff
        s[3] = rotl(s[3], 11)
        return res
    for _ in range(10000):
        next()
    if not next()==a:
        print("you lose")
        exit(1)
    if not next()==b:
        print("you lose")
        exit(1)
    if not next()==c:
        print("you lose")
        exit(1)
    print("well done")
    print(flag)
    exit(0)

if __name__ == "__main__":
    main()

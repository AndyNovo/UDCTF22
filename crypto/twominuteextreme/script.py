import random
import hashlib
f=open("dictionary.txt","r")
lngstr=f.read()
f.close()
words=lngstr.split("\n")[:-1]
assert(len(words)==187632)
word1=random.choice(words)
word2=random.choice(words)
target = hashlib.sha256("%s %s" % (word1, word2)).hexdigest()
print(target)
word3=random.choice(words)
print(word3)
word4=random.choice(words)
print(word4)
target = hashlib.sha256("%s %s" % (word3, word4)).hexdigest()
print(target)

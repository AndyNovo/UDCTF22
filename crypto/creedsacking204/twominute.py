# coding: utf-8
get_ipython().magic(u'clear ')
get_ipython().magic(u'clear ')
get_ipython().magic(u'ls ')
from pwn import *
get_ipython().magic(u'clear ')
get_ipython().magic(u'ls ')
def pst(strip):
    winners=[]
    for cr in string.printable:
        tmp=xor(cr, strip)
        gotem = True
        for c in tmp:
            if not c in uni:
                gotem = False
        if gotem:
            winners.append(cr)
    return winners
uni='0123456789abcdef'
ct='61217660734247595d165c47545e524049307077617748455c0c4508465058544d1860737761711a400d5e125c4a525b511c4e67707667764e155d5d465040535f004f1c617d7065721e405c5c465e4a550e531d496c7772617f4e405d5c405b47055c044f1f62257730724f41515e4b5d16555f50484e65702662274d405e51470c46555d524a4e607d7660734a475a5d165e12545e56484933707762724d4c5c0c475e475458574d186325766d7142400d5c475f40525950404a34727067774f115e08465840505f034d496071746d721e420c5d175a43540a504d4860732260234f405d50440847075e544a196620'.decode('hex')
ct
strips=[ct[i::17] for i in range(17)]
for stp in strips:
    print pst(stp)
    
get_ipython().magic(u'save twominute.py 1-13')

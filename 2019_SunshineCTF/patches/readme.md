```
ugongjae@ubuntu:~/CTF/sunshineCTF/patches$ peda patches 
Reading symbols from patches...(no debugging symbols found)...done.
gdb-peda$ pdisass main
Dump of assembler code for function main:
   0x0000051d <+0>:	lea    ecx,[esp+0x4]
   0x00000521 <+4>:	and    esp,0xfffffff0
   0x00000524 <+7>:	push   DWORD PTR [ecx-0x4]
   0x00000527 <+10>:	push   ebp
   0x00000528 <+11>:	mov    ebp,esp
   0x0000052a <+13>:	push   ebx
   0x0000052b <+14>:	push   ecx
   0x0000052c <+15>:	sub    esp,0x10
   0x0000052f <+18>:	call   0x5c6 <__x86.get_pc_thunk.ax>
   0x00000534 <+23>:	add    eax,0x1aa4
   0x00000539 <+28>:	mov    DWORD PTR [ebp-0x10],0x1
   0x00000540 <+35>:	cmp    DWORD PTR [ebp-0x10],0x0
   0x00000544 <+39>:	jne    0x5a3 <main+134>
   0x00000546 <+41>:	mov    DWORD PTR [ebp-0xc],0x0
   0x0000054d <+48>:	jmp    0x580 <main+99>
   0x0000054f <+50>:	lea    ecx,[eax+0xc8]
   0x00000555 <+56>:	mov    edx,DWORD PTR [ebp-0xc]
   0x00000558 <+59>:	add    edx,ecx
   0x0000055a <+61>:	movzx  edx,BYTE PTR [edx]
   0x0000055d <+64>:	mov    ecx,edx
   0x0000055f <+66>:	mov    edx,DWORD PTR [ebp-0xc]
   0x00000562 <+69>:	mov    edx,DWORD PTR [eax+edx*4+0x48]
   0x00000569 <+76>:	sub    ecx,edx
   0x0000056b <+78>:	mov    edx,ecx
   0x0000056d <+80>:	mov    ebx,edx
   0x0000056f <+82>:	lea    ecx,[eax+0xc8]
   0x00000575 <+88>:	mov    edx,DWORD PTR [ebp-0xc]
   0x00000578 <+91>:	add    edx,ecx
   0x0000057a <+93>:	mov    BYTE PTR [edx],bl
   0x0000057c <+95>:	add    DWORD PTR [ebp-0xc],0x1
   0x00000580 <+99>:	cmp    DWORD PTR [ebp-0xc],0x1e
   0x00000584 <+103>:	jle    0x54f <main+50>
   0x00000586 <+105>:	sub    esp,0x8
   0x00000589 <+108>:	lea    edx,[eax+0xc8]
   0x0000058f <+114>:	push   edx
   0x00000590 <+115>:	lea    edx,[eax-0x1988]
   0x00000596 <+121>:	push   edx
   0x00000597 <+122>:	mov    ebx,eax
   0x00000599 <+124>:	call   0x3b0 <printf@plt>
   0x0000059e <+129>:	add    esp,0x10
   0x000005a1 <+132>:	jmp    0x5b7 <main+154>
   0x000005a3 <+134>:	sub    esp,0xc
   0x000005a6 <+137>:	lea    edx,[eax-0x1970]
   0x000005ac <+143>:	push   edx
   0x000005ad <+144>:	mov    ebx,eax
   0x000005af <+146>:	call   0x3b0 <printf@plt>
   0x000005b4 <+151>:	add    esp,0x10
   0x000005b7 <+154>:	mov    eax,0x0
   0x000005bc <+159>:	lea    esp,[ebp-0x8]
   0x000005bf <+162>:	pop    ecx
   0x000005c0 <+163>:	pop    ebx
   0x000005c1 <+164>:	pop    ebp
   0x000005c2 <+165>:	lea    esp,[ecx-0x4]
   0x000005c5 <+168>:	ret    
End of assembler dump.
```
if you ignore first jump(0x00000544), you can see right flag.

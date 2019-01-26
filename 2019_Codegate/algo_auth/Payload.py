from pwn import *
import base64

li=[3]
dx=[-1,0,1]
dy=[0,1,0]
ma = 2000000000

def Ch(x,y):
    if(x<0 or x>6):
        return False
    if(y<0 or y>6):
        return False
    return True

def DFS(x,y,su,pre):
    global li
    global dx
    global dy
    global ma
    su+=li[x][y]
    if(su>ma):
        return
    if(y==6):
        if(su<ma):
            ma=su

    for i in range(0,3):
        if(pre==0 and i==2):
            continue
        if(pre==2 and i==0):
            continue
        if(Ch(x+dx[i],y+dy[i])):
            DFS(x+dx[i],y+dy[i],su,i)

def main():
    p=remote("110.10.147.104",15712)

    p.recvuntil(">>")
    p.sendline("G")
    global ma
    res=""+chr(82)
    print(p.recvuntil(" ***\n"))
    ma=2000000000
    del li[:]
    
    print(p.recvuntil(">>>"))
    p.sendline("82")

    

    for i in range(1,100):
        print(p.recvline())
        ma=2000000000
        del li[:]
        for j in range(0,7):
            st=p.recvline()
            print(st)
            li.append(map(int,st.split()))
        for j in range(0,7):
            DFS(j,0,0,0)
        print(p.recvuntil(">>>"))
        p.sendline(str(ma))
        res+=chr(ma)
    print(p.recvline())
    print(base64.b64decode(res).decode('utf-8'))


if __name__=="__main__":
    main()
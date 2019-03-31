you can see flag in plain text through hex editor, IDA, or 'strings'.

~~~
ugongjae@ubuntu:~/CTF/UTCTF/basic_re$ strings calculator 
.................................

%.1lf * %.1lf = %.1lf
%.1lf / %.1lf = %.1lf
Error! operator is not correct
utflag{str1ng5_15_4_h4ndy_t00l}
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.11) 5.4.0 20160609
crtstuff.c
__JCR_LIST__
deregister_tm_clones
__do_global_dtors_aux
..................................
ugongjae@ubuntu:~/CTF/UTCTF/basic_re$ 
~~~

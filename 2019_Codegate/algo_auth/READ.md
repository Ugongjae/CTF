ugongjae@ubuntu:~/CTF/codegate$ nc 110.10.147.109 15712
==> Hi, I like an algorithm. So, i make a new authentication system.
==> It has a total of 100 stages.
==> Each stage gives a 7 by 7 matrix below sample.
==> Find the smallest path sum in matrix, 
    by starting in any cell in the left column and finishing in any cell in the right column, 
    and only moving up, down, and right.
==> The answer for the sample matrix is 12.
==> If you clear the entire stage, you will be able to authenticate.

[sample]
99 99 99 99 99 99 99 
99 99 99 99 99 99 99 
99 99 99 99 99 99 99 
99 99 99 99 99 99 99 
99  1  1  1 99  1  1 
 1  1 99  1 99  1 99 
99 99 99  1  1  1 99 

If you want to start, type the G key within 10 seconds....>> G

*** STAGE 1 ***
18 17 16 15 14 13 12 
 9 11 13 15 17 19 21 
18 17 16 15 14 13 12 
14 16 18 20 22 24 26 
16 15 14 13 12 11 10 
 6  8 10 12 14 16 18 
22 21 20 19 18 17 16 

Answer within 10 seconds >>> 82
*** STAGE 2 ***
13 40  8 31 33  1 28 
40 31 22 30 36 40 39 
32 15 32 24  7 10  7 
25 48 49 14 32 27 36 
26  9 15 21 13 15  8 
27  2 48 20  6 39 31 
45 13 37 16  6 45  9 

Answer within 10 seconds >>>

===========================================================================================

After you solve 100 problems, you can get 100 integer answers.

Switch the integers to string, then decode using base64

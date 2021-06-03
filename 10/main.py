'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
s, l1, r1, l2, r2 = map(int, input().split())
if l1 + l2 <= s and s <= l1 + r2 :
    if s <= r2 :
        print(l1, s-l1)
    else :
        print(s - r2, r2)
elif r1 + l2 <= s and s <= r1 + r2 :
    if s <= r2 :
        print(r1, s - r1)
    else :
        print(s - r2, r2)
else :
    print(-1)

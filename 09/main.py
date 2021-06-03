'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))
if h1 == 0:
    h1 = 24
if h2 == 0:
    h2 = 24
if h1 - h2 > 0:
    print("Встреча не состоится")
elif h1 - h2 == 0 and m1 - m2 < 15:
    print("Встреча состоится")
else:
    print("Встреча не состоится")
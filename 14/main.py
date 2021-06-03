'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n = input("Введите n ")
n = int(n)
counter = int(0)
i = int(0)
while 2**i <= n:
    counter = counter + 1
    i = i + 1
print(counter)
    
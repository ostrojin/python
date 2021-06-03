'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
first = int(input())
second = int(input())
buf = first
first = second
second = buf
print ("first = " + str(first))
print ("second = " + str(second))
first = first + second
second = first - second
first = first - second
print ("first = " + str(first))
print ("second = " + str(second))
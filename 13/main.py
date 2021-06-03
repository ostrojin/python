'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n = input("Введите число ")
i = int(2)
n = int(n)
istrue = bool(True)
while i <= (n // 2) + 1 :
    if n%i != 0:
         i = i + 1
    else:
        print("Число составное")
        istrue = False
        break
    i = i + 1
if istrue == True:
    print("Число простое")
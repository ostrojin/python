'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from random import randint
print("Вас приветсвует казино питон")
i = int(0)
while i <= 6:
    if i == 0:
        n = randint(0, 100)
        print(n)
    if i < 6:
        yourNum = int(input())
        if(n < yourNum):
            print("Загаданное число меньше")
        elif(n > yourNum):
            print("Загаданное число больше")
        elif(n == yourNum):
            print("Вы угадали")
        i = i + 1
    if i == 5:
        k = int(input("Желаете начать заново? "))
        if k == 1:
            i = 0
        elif k != 1:
            break
        
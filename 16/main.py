'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import sys
isCorect = bool(False)
isTrue = bool(True)
myString = str('a11155661')
n = int(input())
counter = 0
string = list(input().split())
while isCorect == False:
    if int(len(string)) != n:
        print("Неверное количество элементов")
        string = list(input().split())
    else:
        isCorect = True
i = int(0)
j = int(0)
while i < len(string):
    isTrue = True
    if len(string[i]) != 9:
        continue
    while j < 9:
        if j == 1:
            j = j + 3
        if string[i][j] == myString[j]:
            j = j + 1
        else:
            isTrue = False
            break
    if isTrue == True:
        counter = counter + 1
        print(string[i])
    i = i + 1
if counter == 0:
    print("-1")
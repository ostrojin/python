'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print("Выберите вариант решения")
var = int(input())
if var == 1:
    print("Введите длины сторон")
    a, b, c = map(int, input().split())
    p = (a + b + c)/2
    S = (p*(p-a)*(p-b)*(p-c))**(0.5)
    print("S = ", S)
elif var == 2:
    print("Введите координаты вершин")
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    Cx, Cy = map(int, input().split())
    S = (Ax - Cx)*(By - Cy) - (Bx - Cx)*(Ay - Cy)
    S = abs(S) * 0.5
    print("S = ", S)
else:
    print("Выбран неверный параметр")
'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
first, operator, second = input().split()
if operator == "+":
    x = float(first) + float(second)
elif operator == '-':
     x = float(first) - float(second)
elif operator == '*':
     x = float(first) * float(second)
elif operator == '/':
     x = float(first) / float(second)
else:
    print("Такой параметр не предусмотрен")
print(x)    
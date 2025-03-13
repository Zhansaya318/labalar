n = int(input("Enter N: "))

# Generator for squares up to N
def square_gen(n):
    for i in range(n + 1):
        yield i * i

for num in square_gen(n):
    print(num)



# Even numbers generator
def even_gen(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_gen(n):
    print(num)



# Generator for numbers divisible by 3 and 4
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for num in div_by_3_and_4(n):
    print(num)



# Generator for squares from a to b
a = int(input("Enter A: "))
b = int(input("Enter B: "))
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


for num in squares(a, b):
    print(num)



# Generator counting down from n to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(n):
    print(num)
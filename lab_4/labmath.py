import math
# 1 task
def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = int(input("Input degree: "))
radian = degree_to_radian(degree)
print("Output radian: ", radian)

# 2 task
height = int(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = 0.5 * (base1 + base2) * height
print("Expected Output: ", area)

# 3 task
n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
#(n * s^2) / (4 * tan(π / n))
area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))
print("The area of the polygon is: ", round(area))

# 4 task 
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output: ", area)

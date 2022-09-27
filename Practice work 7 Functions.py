import math

#1.1
print("1.")
r = float(input("Enter the radius of the circle: "))
a = math.pi * pow(r, 2)
print(f"The area of the circle is: {round(a, 2)}")
print("\n")

w = float(input("Enter the width of the rectangle: "))
l = float(input("Enter the length of the rectangle: "))
a = w * l
print(f"The area of the ractangle is: {round(a, 2)}")
print("\n")

a, b, c = map(float, input("Enter each side of the triangle: ").split())
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is: {round(area, 2)}")
print("\n")

#1.2  
a1 = [10, 10, 10, 11, 4, 5, 6, 7]
count = 0
for i in a1:
    count += i
avg = count/len(a1)
print("First array: ", a1)
print("Sum of a1 = ", count)
print("Arithmetic mean of a1 = ", avg)
print("\n")

a2 = [1, 2, 3, 4, 5, 6, 7]
count = 0
for i in a2:
    count += i
avg = count/len(a2)
print("Second array: ", a2)
print("Sum of a2 = ", count)
print("Arithmetic mean of a2 = ", avg)
print("\n")

a3 = [9, 7, 3, 5, 11, 6, 56, 2, 11, 90, 64]
count = 0
for i in a3:
    count += i
avg = count/len(a3)
print("Third array: ", a3)
print("Sum of a3 = ", count)
print("Arithmetic mean of a3 = ", avg)
print("\n")



#2.1
print("2.")

def ha(s):
    return ((3 * math.sqrt(3) * (s * s)) / 2);  
if __name__ == "__main__" :
    s = int(input("Enter the side of hexagon: "))
    print("Area:","{0:.4f}" .
           format(ha(s)))
print("\n")

#2.2
w = float(input("Enter the width of the first rectangle: "))
l = float(input("Enter the length of the first rectangle: "))
a = w * l
print(f"The area of the ractangle is: {round(a, 2)}")
w = float(input("Enter the width of the second rectangle: "))
l = float(input("Enter the length of the second rectangle: "))
a = w * l
print(f"The area of the ractangle is: {round(a, 2)}")
w = float(input("Enter the width of the third rectangle: "))
l = float(input("Enter the length of the third rectangle: "))
a = w * l
print(f"The area of the ractangle is: {round(a, 2)}")
print("\n")



#3.1
print("3.")

a1 = int(input("1 side of first triangle: "))
b1 = int(input("2 side of first triangle: "))
a2 = int(input("1 side of second triangle: "))
b2 = int(input("1 side of second triangle: "))
c1 = math.sqrt(pow(a1, 2) + pow(b1, 2))
c2 = math.sqrt(pow(a2, 2) + pow(b2, 2))
if c1 < c2:
    print("Hypotenuse of the frist triangle is ", c1)
    print("Hypotenuse of the second triangle is ", c2)
    print("Hypotenuse of the second triangle is greater")
elif c1 > c2:
    print("Hypotenuse of the frist triangle is ", c1)
    print("Hypotenuse of the second triangle is ", c2)
    print("Hypotenuse of the first triangle is greater")
else:
    print("Hypotenuse of the frist triangle is ", c1)
    print("Hypotenuse of the second triangle is ", c2)
    print("Hypotenuse of these triangles are equal")
print("\n")

#3.2
string = str(input("Enter a string: "))
ar = []
l = len(string)
for i in range (0, l):
    ar.append(string[i])
 
for i in range(0,l):
    for j in range(0,l):
        if ar[i] < ar[j]:
            ar[i], ar[j] = ar[j], ar[i]
j = ""

for i in range(0, l):
    j = j + ar[i]
print(j)
print("\n")



#4.1
print("4.")
from fractions import Fraction
print ("A = 100; B = 2; C = 157; D = 9;")
print (Fraction(100, 2) / Fraction(157, 9))



#5.1
print("5.")
from fractions import Fraction
print ("A = 100; B = 2; C = 157; D = 9;")
print (Fraction(100, 2) - Fraction(157, 9))

#5.2
n = int(input('Enter an integer: '))
print("The divisors of the number are: ")
for i in range(1, n + 1):
    if(n % i == 0):
        print(i)




#6.1
print("6.")

def gcd (x, y):  
    if (y == 0):  
        return x  
    else:  
        return gcd (y, x % y)  
x = int (input ("Enter the first number: ")) 
y = int (input ("Enter the second number: "))     
print("GCD is: ", gcd(x, y))


def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
print("LCM is: ", lcm(x, y))

#6.2
def area (a , b , c , d ):
    sp = (a + b + c + d) / 2
    return math.sqrt((sp - a) * (sp - b) * (sp - c) * (sp - d))
a = int(input('Enter the first side: '))
b = int(input('Enter the second side: '))
c = int(input('Enter the third side: '))
d = int(input('Enter the fourth side: '))
x = int(input('Enter the diagonal: '))
print("%.2f"%area(a, b, c, d))



#7.2
print("7.")

def octal(n):
    on = [0] * 100
    i = 0
    while (n != 0):
        on[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(on[j], end="")
n = int(input('Enter the int: '))
octal(n)



#8.2
print("8.")
lst = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    print("Enter the ", i + 1, "element: ")
    ele = int(input())
    lst.append(ele) 
print(lst)

def swapl(list):
    first = list.pop(0)  
    last = list.pop(-1)
    list.insert(0, last) 
    list.append(first)  
    return list
print(swapl(lst))





    


























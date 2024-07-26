# 1
print("Ejercicio #1")
print("Del 1 al 7:")
for n in range(1,8):
    print(n)

print("Del 1 al 12")
for n in range(1,13):
    print(n)

# 3
print("Ejercicio #3")
print("Del 3 al 99:")
for n in range(3,100, 3):
    print(n)

# 4
print("Ejercicio 4")
print("Cuenta regresiva")
for n in range(10,0, -1):
    print(n);
print("¡Despegue!")

# 5
print("Ejercicio 5")
import turtle as t
from turtle import *
t.color("red")

for i in range(200):
    forward(i)
    left(50)


from math import sqrt


print("Me de os respequitivos dados para eu fazer a conta de bhaskara.")
a =  int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

DELTA = b**2 - 4*a*c
print("delta = ", DELTA)

if DELTA != 0 :

    fração_2a = 2*a

    X1 = (-b + sqrt(DELTA)) / fração_2a
    print("X1 = " , X1)

    X2 = (-b - sqrt(DELTA)) / fração_2a
    print("X2 = " , X2)
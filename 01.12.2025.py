""""
zime=input("ivelies :), :(, ￣へ￣, ^///^, =/")
def convert(zime):
    if zime==":)":
        print("🌫(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    elif zime==":(":
        print("😓")
    elif zime=="￣へ￣":
        print("😡")
    elif zime=="^///^":
        print("😋")
    elif zime=="=/":
        print("😓")
    else:
        print("nesaprotu")



convert(zime)
"""

"""
for k in range (10):
    print(k+1)

for i in range(20,0,-1):
    print(i)

for x in range (1,10):
    y=x**2+3*x-2
    print(f"ja x={x}, tad y={y}")

import random

x=random.randint(0,8)
y=random.randint(0,8)
print(x)
print(y)

#v1 variant
import random
m=int(input("m: "))

for i in range(m):
    sk=random.randint(0,60)
    print(i+1,". ",sk)

import random
m=int(input("m: "))

for i in range(m,0, -1):
    sk=random.randint(0,60)
    print(f'{i}.{sk}')

c = int(input("skaitļu skaits: "))
summa=0
for k in range(c):
    sk = int(input("sk: "))
    summa+=sk
    print(summa)
print("sum=" ,summa)


import math
for n in range(7,10):
    print(math.pow(n,2))

for k in range(27,17,-1):
    print(math.sqrt(k))


print(k**0.5)


for x in range(1,50):
    if x%3==0 or x%5==0:
        print(x)
    else:
        print("nedalas ne ar 3 ne ar 5")


n=int(input("n: "))
if n>1:

  for i in range(1,n):
  print(i,i**2)

else:

    for i in range(n,1):

    print(i,i**2)





for k in range(1,20):
     if k%2==0:
        continue
     else:
       print(k,"ir nepara")




n=int(input("n: "))
sum=0
for i in range(n):
    sk=int(input("sk: "))
    if sk>=0:
        sum+=sk
    else:
        break
print("pozitiva summa ir",sum)

i=int(input("i: "))

for n in range(n):
    if n % 3 == 0 or n % 5 == 0:
        print(n)
    else:
        print("nedalas ne ar 3 ne ar 5")

lats=1.42
latu_skaits=float(input("ievadi latu apjomu?: "))
def pelmenis(lats, latu_skaits):
    print(f'{lats*latu_skaits:.2f} eur.')

pelmenis(lats,latu_skaits)



fanta=50
summa=0

def automats(fanta, summa):
    while summa <= 50:
        nauda=int(input("naudas apjoms"))
        if nauda==20 or nauda==10 or nauda==5:
            summa += nauda
            print(f"iemaksats: {summa}")
            if fanta-nauda=>=0:
            print(f"vēl trukst{fanta-nauda}")
            


automats(summa, fanta)



V1=input("virkne1: ")
V2=input("virkne2: ")

V3=V1+V2
print(V3)

V1+=V2
print(V2)


s1="abapradabra"
s1=s1.replace()
print(s1)
print(s1.isalpha())


v1=input("ieavadi virknoi")
print(v1.replace("","..."))
"""
s1 = input("ieavadi virkni: ")
s2 = input("ieavadi otro virkni: ")
s2 += str(ord(s1[0]))
print(ord(s1[0]))

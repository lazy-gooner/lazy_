'''x=[1,2,3,4,5]
y=[5,6,7,8,9]
z=y+x
x+=y
print(type(z),z)
print(x*3)
for i in z: #pārskatām saraksta elementus
    print("elements",i


celasoma=[["cepure","zeķes","šalle"],["soma","krekls","ūdens"]]
print(type(celasoma))
print(celasoma[0])
for i in celasoma[0]:
    print(i)
print(celasoma[0][-1])
print(celasoma[1])
for i in celasoma[1]:
    print(i)
print(celasoma[1][0])
'''
from itertools import count

'''
saraksts=["galva",10,23.5]
saraksts.insert(len(saraksts),"vēl viens")
a=[1,2,3]
#saraksts.extend(a)#strādā ar sarakstiem
print(saraksts)

'''
'''
sar1=['a','b','c','d','e','f','g']
sar1.append('saule')
sar1.insert(3,"mākonis")
print(sar1)
for i in sar1:
    print(i)

print(sar1[::-1])
sar1.pop()
print(sar1)
#atveram write (w) modā
datne=open("uzd.txt","w",encoding="utf-8")
#datne.write(str(sar1))
for i in sar1:
    datne.write(i+"\n")
datne.close()

with open("uzd1.txt","a",encoding="utf-8") as datne:
    for i in sar1:
        datne.write(i + "\n")
    datne.close()


nedela=["pirmdiena","otrdiena","trešdiena","ceturdiena","piektdiena","Sestdiena","Svētdiena"]
f=open("nedela.txt","w",encoding="utf-8")
#f.write(str(nedela))#str pārveido sarakstu par virkni
for i in nedela:
    f.write(i+" ")
f.close()

file=open("nedela.txt","r+",encoding="utf-8")
dati=file.read() #ir virkne
#print(list(dati))
sar2=[]
info=dati.split()#no virknes izveidoju sarakstu
for i in info:
    sar2.append(i)
print(sar2)
'''
sk_sar=[]
k=6
datne=open("ievade.txt","w",encoding="utf-8")
for i in range(k):
    sk=int(input("sk= "))
    #sk=input("sk= ")
    sk_sar.append(sk)
    datne.write(str(sk)+" ")
datne.close()
#saraksta skaitļa summa
print(f"summa {sum(sk_sar)}")
print(f"min {min(sk_sar)}")
print(f"max {max(sk_sar)}")
#print(f"vid {round(sum(sk_sar)/k,4)}")
print(f"vid {(sum(sk_sar)/k):.2f}")
reizin=1
#skaitļu reizinājums
for i in sk_sar:
    reizin*=i

print(reizin)

#6uzd

import random

n=int(input("Cik skaitļus ievad? "))
m=int(input("Cik virknes ievad? "))


skaitli=[]
for i in range(n):
    skaitli.append(int(input("Ievadi skaitli: ")))

virknes=[]
for i in range(m):
    virknes.append(input("Ievadi virkni: "))

if len(skaitli) > len(virknes):
    print("Vairāk elementu ir skaitļu sarakstā")
elif len(skaitli) < len(virknes):
    print("Vairāk elementu ir virkņu sarakstā")
else:
    print("Abos sarakstos vienāds skaits")

apvienots =skaitli+virknes

print("Apvienotais saraksts:", apvienots)

with open("apvienosana.txt","w",encoding="utf-8") as f:
    for x in apvienots:
        f.write(str(x) + "\n")
"""""""""
a = 12
b = 2
def saskaitisana(a, b):
    return a+b
saskaitisana(a,b)
print(saskaitisana(a,b))
def atņemsana(a,c=13):
    print(a-c)
atņemsana(a)
def reizinamie(a,b):
    return a*b
print(reizinamie(a,b))
def dalisana(a,b):
    print(a/b)
dalisana(a,b)
izvele=input("izvele +, -, *, /")
if izvele=="+":
    print(saskaitisana(a,b))
elif izvele=="-":
   print(atņemsana(a))
elif izvele=="*":
   print(reizinamie(a,b))
elif izvele=="/":
    print(dalisana(a,b))
else:
    print("ko?")
"""""""""



"""""""""
sk=int(input("sk= "))

def para(sk):
    if sk%2==0: #vai dalijuma atlikums ir 0
        print("pāra")
    else:
        print("nēpāra")

para(sk)#izsauk funkciju
"""""""""
"""""""""
m=int(input("m= "))
c=300000000
def Einstein(m,c):
    E=m*c**2 #E m*math:pow()
    print(E, "džouli")

Einstein(m,c)
"""

"""""
maltitas_izmaksas=float(input("cik jamaksa par edienu"))
procenti=float(input("cik procentus atstasim 10, 15, cits: "))

def dzerumnauda(maltitas_izmaksas,procenti):
    return maltitas_izmaksas*procenti/100
print(dzerumnauda(maltitas_izmaksas,procenti))
"""""""



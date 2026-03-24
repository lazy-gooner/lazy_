import re

text="Mans telēfona numurs ir 20001234"
rezultāts=re.search(r"\d(8)",text)
print(rezultāts.group())
rezultāts=re.findall(r"\d(8)",text)
print(rezultāts2)
rezultāts3=re.search(r"\d(8)",text)
print(rezultāts3)
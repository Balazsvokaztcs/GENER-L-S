import random

#0
print("Osztályzatok generálása.")

#1
db=int(input("Kérem aaz osztályzatok számát: "))

osztalyzatok=[]
#mivel tudjuk a darab számot ezért - előre maghatározott lépésszámú ciklus
for i in range(db):
    oszt = random.rantint(1, 5) #az osztályzatok 1 - 5 terjednek
    osztalyzatok.append(oszt)

#2-3
print(osztalyzatok)    
print(" Ajde da vežbamo ")
# почетна вредност
Poeni=0

#уносимо одговор
Pitanje1 = int(input("Koliko je 2+2?\n"))
#питамо да ли тачно
if Pitanje1==4:
    print("Bravo! Tačno!")
    Poeni=Poeni+1
else:
    print("buuu! netačno!")

Pitanje2 = int(input("Koliko je 3*6?"))

if Pitanje2==18:
    print("Bravo! Tačno!")
    Poeni=Poeni+1
else:
    print("buuu! netačno!")
#штампамо ук поене
print("Ukupni poeni su: ",Poeni)

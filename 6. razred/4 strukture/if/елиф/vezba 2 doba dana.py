h = int(input("Koliko ima sati?: "))

if h < 12:
    doba = "Dobro jutro"
elif h <= 18:
    doba = "Dobar dan"
else:
    doba = "Dobro veče"

print(doba)

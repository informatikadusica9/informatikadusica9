ml1 = int(input("Unesi cenu mleka "))
v1 = int(input("Unesi cenu voca "))
m1 = int(input("unesi cenu mesa "))
u1 = [ml1,v1,m1]
uzina1 = sum(u1)
ml2 = int(input("Unesi novu cenu mleka "))
v2 = int(input("Unesi novu cenu voca "))
m2 = int(input("unesi novu cenu mesa "))
u2 = [ml2,v2,m2]
uzina2 = sum(u2)
if uzina1 == uzina2:
    print("Nije se promenila cena užine")
elif uzina1 > uzina2:
    print("Užina je pojeftinila za ", uzina1-uzina2)
else:
    print("Užina je poskupela za ", uzina2-uzina1, "din.")

print("Zdravo! Ovo je kratak kviz o srednjem veku. Odgovore  unosi ćiriličnim pismom! Ako to ne uradite, dobićete poruku da je odgovor netačan!")
pitanja=["Kako se naziva radna obaveza u doba Osmanlija?\n",
         "Kako se zvalo germansko pleme koje je naseljavalo Afriku\n",
         "Pravo ime Svetog Save je Rastko.",
         "Koje godine se odigravala Kosovska bitka?",
         "Nabrojnije varvarsko pleme koje tojom 7. veka dolazi na prostor rimskog carstva bili su Germani."]
odgovori=["a)kulak\nb)desetak\nc)ruteri\nd)feud\n:", " a)Vandali\nb)Ruteri\nc)Feudilin\n:", "a)tačno\nb)netačno\n:", "a)1388\nb)1389\nc)1148\nd)1398\n:", "a)tačno\nb)netačno\n:" ]
tačni_odgovori=["a","a", "a", "b", "b"]
prikaz_odgovora=["rana obaveza u doba Osmanlijskog carstva naziva se kulak\n","Severnu Afriku naseljavalo je germansko pleme Vandali\n", "Pravo ime Svetog Save je Rastko\n", "Kosovska bitka je vođena 15.juna 1389. fodine\n", "Najbrojnije varvarsko pleme koje tokom 5. veka dolazi na prostor rimskog carstva bili su Germani\n"]
rezultat =0
for i in range(len(pitanja)):
    print(pitanja[i])
    odgovor=input(odgovori[i])
    if odgovor.lower()==tačni_odgovori[i]:
        print("Odgovor je tačan!")
        rezultat +=1
    else:
        print("Odgovor je netačan, odgovor je  ")
        prikaz_odgovora[i]
procenti=(rezultat/5.0)*100
print("Tačnih odgovora je:", rezultat)
print("Imaš:", procenti, "% tačnih odgovora")

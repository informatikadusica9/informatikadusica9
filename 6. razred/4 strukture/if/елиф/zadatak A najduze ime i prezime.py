ime1= input("Unesi prvo ime i prezime:")
ime2= input("Unesi drugo ime i prezime:")
ime3= input("Unesi treće ime i prezime:")
maxime=max (len(ime1), len(ime2), len(ime3))
if (len(ime1)==maxime):
    print("Najduže ime i prezime je",ime1 )
elif (len(ime2)==maxime):
    print("Najduže ime i prezime je",ime2 )
else:   
    print("Najduže ime i prezime je",ime3 )

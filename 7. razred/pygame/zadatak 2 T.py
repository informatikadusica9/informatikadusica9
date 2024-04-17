import pygame as pg

#NAKON STO SE UKLJUCI BIBLIOTEKA PYGAME I ZADA JOJ SKRACENO IME PG, POKRECE JE
pg.init()
#POZIVA SE FJA KOJA DAJE NASLOV PROZORU
pg.display.set_caption ("Duž")
#DEFINISANJE DIMENZIJA PROZORA
(sirina, visina)=(500, 500)

#PROZOR = FJA ZA PRIKAZ PROZORA KOJI CE IMATI DEF DIMENZIJE
prozor=pg.display.set_mode ((sirina, visina))
#BOJI PROZOR U BELO 
prozor.fill(pg.Color("white"))
#KONSTANTNA DEBLJINA LINIJE
debljina=10

#CRTA VERTIKALNU CRNU LINIJU OD TACKE (200,100) DO TACKE (200,300)
pg.draw.line (prozor, pg.Color("black"), (200, 100), (200,300), debljina)

#CRTA HORIZONTALNU PO SREDINI NA Y 100
pg.draw.line (prozor, pg.Color("black"), (100, 100), (300,100), debljina)

#osvezavamo sadrzaj prozora i tako pokazujemo ono sto smo nacrtali
pg.display.update()
#CEKA DA PRITISNEMO X NA PROZORU DA BI GA UGASIO
while pg.event.wait().type!=pg.QUIT:
  pass
#GASI BIBLIOTEKU
pg.quit ()

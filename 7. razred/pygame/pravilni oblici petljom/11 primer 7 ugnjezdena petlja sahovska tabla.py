import pygame as pg, random
pg.init()
pg.display.set_caption("sahovska tabla")
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))

#bojimo pozadinu prozora u crveno
prozor.fill(pg.Color("red"))
broj_polja=6
sirinapolja=sirina//broj_polja
visinapolja=visina//broj_polja
for i in range(broj_polja):
    for j in range(broj_polja):
        if(i+j)%2!=0:
            pg.draw.rect(prozor, pg.Color("black"), (i*sirinapolja, j*visinapolja, sirinapolja,visinapolja))
        
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


import pygame as pg, random
pg.init()
pg.display.set_caption("zvezdica")
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))



# funkcija koja gradi nasumično odabranu boju
def zvezdica(x,y):
    r,d=20,2
    pg.draw.line(prozor, pg.Color("white"), (x-r,y), (x+r,y),d)
    pg.draw.line(prozor, pg.Color("white"), (x,y-r), (x,y+r),d)
    pg.draw.line(prozor, pg.Color("white"), (x-r/2,y-r/2), (x+r/2,y+r/2),d)
    pg.draw.line(prozor, pg.Color("white"), (x+r/2,y-r/2), (x-r/2,y+r/2),d)
#bojimo pozadinu prozora u plavo
prozor.fill(pg.Color("blue"))
broj_zvezdica=64
for i in range(broj_zvezdica):
    zvezdica(random.randint(0, sirina), random.randint(0, visina))

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


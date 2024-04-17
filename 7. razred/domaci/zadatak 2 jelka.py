import pygame as pg
pg.init()
pg.display.set_caption ("jelka")
(sirina, visina)=(300, 300)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))
#boje koje cemo koristiti
ZELENA = (0,100,36)
BRAON = (97,26,9)
#STABLO
pg.draw.rect (prozor, BRAON, (130,250,40,50))
#KROSNJA
pg.draw.polygon (prozor, ZELENA,[(50,250),(150,125),(250,250)])
pg.draw.polygon (prozor, ZELENA,[(75,200),(150,100),(225,200)])
pg.draw.polygon (prozor, ZELENA,[(100,150),(150,75),(200,150)])
pg.draw.polygon (prozor, ZELENA,[(125,100),(150,50),(175,100)])

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

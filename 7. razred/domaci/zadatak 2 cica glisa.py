import pygame as pg
pg.init()
pg.display.set_caption ("cica glisa")
(sirina, visina)=(300, 300)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))

def uokvireni_krug(prozor, boja, centar, poluprecnik):
  pg.draw.circle (prozor, boja, centar, poluprecnik)
  pg.draw.circle (prozor, pg.Color("black"), centar, poluprecnik, 2)
#glava
uokvireni_krug (prozor, pg.Color("yellow"), (150,150),100)
#levo oko
uokvireni_krug (prozor, pg.Color("black"), (100,120),15)
#desno oko
uokvireni_krug (prozor, pg.Color("black"), (200,120),15)
#nos
uokvireni_krug (prozor, pg.Color("black"), (150,170),15)
#usta
pg.draw.circle  (prozor, pg.Color("red"), (135,217),15)
pg.draw.circle  (prozor, pg.Color("red"), (165,217),15)
pg.draw.circle  (prozor, pg.Color("red"), (150,220),15)
pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

import pygame as pg
pg.init()
pg.display.set_caption ("E")
(sirina, visina)=(200, 200)

prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("grey"))
debljina=10

pg.draw.line (prozor, pg.Color("purple"), (50, 50), (50, 150), debljina)
pg.draw.line (prozor, pg.Color("purple"), (50, 50), (100,50), debljina)
pg.draw.line (prozor, pg.Color("purple"), (50, 100), (90,100), debljina)
pg.draw.line (prozor, pg.Color("purple"), (50, 150), (100,150), debljina)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()


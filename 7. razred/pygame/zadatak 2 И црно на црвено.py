import pygame as pg
pg.init()
pg.display.set_caption ("Duž")
(sirina, visina)=(500, 500)

prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("red"))
debljina=10

pg.draw.line (prozor, pg.Color("black"), (50, 50), (50, 150), debljina)
pg.draw.line (prozor, pg.Color("black"), (50, 150), (150,50), debljina)
pg.draw.line (prozor, pg.Color("black"), (150, 50), (150,150), debljina)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

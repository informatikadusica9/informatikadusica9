import pygame as pg
pg.init()
pg.display.set_caption ("Duž")
(sirina, visina)=(500, 500)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color(255,255,255))

pg.draw.line (prozor, pg.Color(0,0,0), (100, 250), (400,250), 5)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

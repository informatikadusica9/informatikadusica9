import pygame as pg
pg.init()
pg.display.set_caption ("Duž")
(sirina, visina)=(500, 500)

prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("yellow"))
debljina=10

pg.draw.line (prozor, pg.Color("green"), (200, 100), (200,300), debljina)
pg.draw.line (prozor, pg.Color("green"), (100, 100), (300,100), debljina)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

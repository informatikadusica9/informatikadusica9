import pygame as pg
pg.init()
pg.display.set_caption ("krug")
(sirina, visina)=(200, 200)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))

pg.draw.circle (prozor, pg.Color("red"), (100,100),50)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

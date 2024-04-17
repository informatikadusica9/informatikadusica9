import pygame as pg
pg.init()
pg.display.set_caption ("crvena kucica")
(sirina, visina)=(400, 400)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))

temena = [(50,300), (50,150),(150,50),(250,150), (250,300)]
pg.draw.polygon (prozor, pg.Color("red"), temena)
pg.draw.polygon (prozor, pg.Color("black"), temena,3)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

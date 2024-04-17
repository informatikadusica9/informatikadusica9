import pygame as pg
pg.init()
pg.display.set_caption ("zuti trougao")
(sirina, visina)=(400, 400)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))

temena = [(50,300), (200,50), (350,300)]
pg.draw.polygon (prozor, pg.Color("yellow"), temena)
pg.draw.polygon (prozor, pg.Color("grey"), temena,3)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

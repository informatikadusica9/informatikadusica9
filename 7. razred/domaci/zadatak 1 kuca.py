import pygame as pg
pg.init()
pg.display.set_caption ("kucica")
(sirina, visina)=(300, 300)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))

temena = [(50,140), (150,50), (250,140)]
pg.draw.polygon (prozor, pg.Color("red"), temena)
pg.draw.polygon (prozor, pg.Color("black"), temena,3)

pg.draw.rect (prozor, pg.Color("yellow"), (50, 140, 200, 160))
pg.draw.rect (prozor, pg.Color("black"), (50, 140, 200, 160),3)

pg.draw.rect (prozor, pg.Color("blue"), (70, 180, 40, 40))
pg.draw.rect (prozor, pg.Color("black"), (70, 180, 40, 40),3)

pg.draw.rect (prozor, pg.Color("blue"), (190, 180, 40, 40))
pg.draw.rect (prozor, pg.Color("black"), (190, 180, 40, 40),3)

pg.draw.rect (prozor, pg.Color("black"), (130, 200, 40, 100))


pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

import pygame as pg
pg.init()
pg.display.set_caption ("elipsa")
(sirina, visina)=(500, 500)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))

pg.draw.ellipse (prozor, pg.Color("blue"), (0,0,100,150),2)
pg.draw.ellipse (prozor, pg.Color("green"), (100,50,200,50))

pg.draw.rect (prozor, pg.Color("blue"), (0,0,100,150),1)
pg.draw.rect (prozor, pg.Color("green"), (100,50,200,50),1)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()

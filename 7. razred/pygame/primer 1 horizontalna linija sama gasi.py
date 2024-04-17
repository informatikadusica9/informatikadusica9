import pygame as pg
pg.init()
pg.display.set_caption ("Duž")
(sirina, visina)=(500, 500)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))

pg.draw.line (prozor, pg.Color("black"), (100, 250), (400,250), 5)

pg.display.update()
pg.time.wait(2000)
pg.quit ()

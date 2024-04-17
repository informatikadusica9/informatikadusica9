import pygame as pg
pg.init()
pg.display.set_caption("Sunce")

(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

pg.draw.circle(prozor, pg.Color("yellow"), (150,150), 50)

pg.draw.line(prozor, pg.Color("yellow"), (50, 150), (250, 150), 10)
pg.draw.line(prozor, pg.Color("yellow"), (150, 50), (150, 250), 10)

pg.draw.line(prozor, pg.Color("yellow"), (75, 75), (225, 225), 10)
pg.draw.line(prozor, pg.Color("yellow"), (75, 225), (225, 75), 10)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

import pygame as pg
pg.init()
pg.display.set_caption("Cica Glisa")

(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

pg.draw.circle(prozor, pg.Color("yellow"), (140,80), 25,2)
pg.draw.polygon (prozor, pg.Color("green"), [(120,20), (160,20), (160,60), (120,60)])

pg.draw.line(prozor, pg.Color("green"), (100,60),(180,60),2)

pg.draw.circle (prozor, pg.Color("black"), (132,75), 2, 2)
pg.draw.circle (prozor, pg.Color("black"), (150,75), 2, 2)
pg.draw.line(prozor, pg.Color("red"), (132,88),(150,88),2)


pg.draw.line(prozor, pg.Color("black"), (140,105),(140,200),2)
pg.draw.line(prozor, pg.Color("black"), (60,120),(80,140),2)
pg.draw.line(prozor, pg.Color("black"), (80,140),(140,120),2)
pg.draw.line(prozor, pg.Color("black"), (140,120),(180,160),2)
pg.draw.line(prozor, pg.Color("black"), (180,160),(200,200),2)
pg.draw.line(prozor, pg.Color("black"), (140,200),(160,220),2)
pg.draw.line(prozor, pg.Color("black"), (160,220),(160,280),2)

pg.draw.line(prozor, pg.Color("black"), (140,200),(120,220),2)
pg.draw.line(prozor, pg.Color("black"), (120,220),(120,280),2)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

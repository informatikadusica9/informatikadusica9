import pygame as pg
pg.init()
pg.display.set_caption("meta")

(sirina, visina) = (350, 350)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

#centar kruga je u centru prozora
centar =(sirina//2, visina //2) 

#poluprečnik se menja od 10 do 160, sa korakom 30
for r in range (10, 161, 30):
    pg.draw.circle (prozor, pg.Color("black"), centar, r, 5)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

import pygame as pg
pg.init()
pg.display.set_caption("dijagonala")
(sirina, visina) = (400, 300)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("black"))

n = 5
dx = sirina / n
dy = visina / n
# crtamo n linija iznad dijagonale i nju
for i in range(n+1):
    pg.draw.line(prozor, pg.Color("green"), (i*dx,0), (0, i*dy), 2)

# dodaj n-1 linija ispod dijagonale, bez nje
for i in range(1,n):
    pg.draw.line(prozor, pg.Color("green"), (i*dx, visina), (sirina, i*dy), 2)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


import pygame as pg
pg.init()
pg.display.set_caption("pravougaona mreza")
(sirina, visina) = (400, 300)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

brojPodeoka = 5
dx = sirina / brojPodeoka
dy = visina / brojPodeoka

# crtamo horizontalne crvene linije
for i in range(1,brojPodeoka):
    pg.draw.line(prozor, pg.Color("red"), (0, i*dy), (sirina, i*dy), 3)

# dodaj kod koji crta vertikalne linije crvnom bojom
for i in range(1,brojPodeoka):
    pg.draw.line(prozor, pg.Color("black"), (i*dx, 0), (i*dx, visina), 3)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


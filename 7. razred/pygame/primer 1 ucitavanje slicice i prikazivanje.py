import pygame as pg
pg.init()
pg.display.set_caption("ucitavanje slicica")

(sirina, visina) = (500, 200)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

#ucitavamo slicicu iz datoteke PyGame.png
slika = pg.image.load("PyGame.png")

#prikazujemo slicicu na sredini ekrana
(x,y) = ((sirina - slika.get_width())/2,(visina - slika.get_height())/2)
prozor.blit(slika,(x,y))

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

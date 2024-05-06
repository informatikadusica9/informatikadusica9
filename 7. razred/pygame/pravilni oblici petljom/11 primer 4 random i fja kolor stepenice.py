import pygame as pg, random
pg.init()
pg.display.set_caption("Histogram")
(sirina, visina) = (400, 300)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))


# funkcija koja gradi nasumično odabranu boju
def nasumicna_boja():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# broj histograma
broj_histograma = 15
# dimenzija histograma
a = sirina / broj_histograma
b = visina / broj_histograma
# prolazimo kroz sva polja
for i in range(broj_histograma):
    pg.draw.rect(prozor, nasumicna_boja(), (i*a, visina-i*b, a, i*b))

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


import pygame as pg, random
pg.init()

pg.display.set_caption("promena boja")
(sirina, visina) = (300, 300)
prozor=pg.display.set_mode((sirina, visina))

boje = ["red", "black", "yellow", "green"]
broj͟boje = 0

kraj = False
sat = pg.time.Clock()

while not kraj:
  prozor.fill(pg.Color(boje[broj͟boje]))
  broj͟boje = (broj͟boje + 1) % len(boje)
  pg.display.update()

  for dogadjaj in pg.event.get():
    if dogadjaj.type == pg.QUIT:
      kraj = True
  
  sat.tick(2)

pg.quit()

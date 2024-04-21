import pygame as pg, random
pg.init()

pg.display.set_caption("promena boja")
(sirina, visina) = (400, 400)
prozor=pg.display.set_mode((sirina, visina))

x=0
def crtaj():
  #crtamo lopticu
  prozor.fill(pg.Color("black"))
  pg.draw.circle(prozor, pg.Color("yellow"), (x, visina//2), 30)

def novi_frejm():
  global x
  x+=1
  
kraj = False
sat = pg.time.Clock()


while not kraj:
  crtaj()
  pg.display.update()

  for dogadjaj in pg.event.get():
    if dogadjaj.type == pg.QUIT:
      kraj = True
  
  sat.tick(50)
  novi_frejm()

pg.quit()

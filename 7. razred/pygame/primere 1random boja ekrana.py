import pygame as pg, random
pg.init()

pg.display.set_caption("promena boja")
(sirina, visina) = (300, 300)
prozor=pg.display.set_mode((sirina, visina))



kraj = False
sat = pg.time.Clock()#sat koji odredjuje broj frejmova u sekundi

while not kraj:
  #nasumicno odredjujemo boju pozadine
  boje = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
  #bojimo pozadinu prozora
  prozor.fill(boje)
  #azuriramo sadrzaj prozora
  pg.display.update()
  #proveravamo da li je korisnik iskljucio prozor
  for dogadjaj in pg.event.get():
    if dogadjaj.type == pg.QUIT:
      kraj = True
  #pauziramo do slededjeg frejma  
  sat.tick(2)



pg.quit()

import pygame as pg
import random
pg.init()
pg.display.set_caption ("sareni veretikalni krugovi ")
(sirina, visina)=(600, 600)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))


# krugovi 15px po sredini
r = 15  # poluprečnik krugova
y = r   # y koordinata centra tekućeg kruga
while y<visina:# crta sve dok y koordinata ne dodje do kraja visine
  #bira random boju svakog kruga
    boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  # crtamo krug
    pg.draw.circle(prozor, boja, (sirina // 2, y), r)
  # centar narednog kruga je udaljen za 2r od centra tekućeg kruga
    y += 2*r  



        
pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()


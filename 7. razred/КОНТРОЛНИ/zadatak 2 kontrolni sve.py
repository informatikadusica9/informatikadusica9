import pygame as pg
import random
pg.init()
pg.display.set_caption ("Pera Peric VII")
(sirina, visina)=(600, 600)
prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))




#prvi zadatak oblici
# crna linija    
pg.draw.line(prozor, pg.Color("black"), (100, 50), (450, 50), 5)
# crvena linija u g   
pg.draw.line(prozor, pg.Color("red"), (50, 75), (350, 75), 5)
pg.draw.line(prozor, pg.Color("red"), (50, 75), (50, 200), 5)
#kvadrat
pg.draw.rect (prozor, pg.Color("blue"), (100, 100, 100,100))
#kruznica
pg.draw.circle(prozor, pg.Color("green"), (400, 200), 50, 3)
#elipsa
pg.draw.ellipse (prozor, pg.Color("grey"), (50,300,250,100),10)
#trougao
pg.draw.polygon (prozor, pg.Color("yellow"), [(300,550), (425,400), (550,550)])

# drugi zadatak dijagonale
n = 10
dx = sirina / n #razmak izmedju dijagonala
dy = visina / n
# crtamo n linija iznad dijagonale i nju
for i in range(n+1):
    pg.draw.line(prozor, pg.Color("grey"), (i*dx,0), (0, i*dy), 1)
# dodaj n-1 linija ispod dijagonale, bez nje
for i in range(1,n):
    pg.draw.line(prozor, pg.Color("green"), (i*dx, visina), (sirina, i*dy), 2)

# trece zadatak krugovi 
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


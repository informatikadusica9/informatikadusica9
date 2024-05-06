import pygame as pg, random
pg.init()
pg.display.set_caption("zvezdica ugnjezdeno")
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))



# funkcija 
def zvezdica(x,y):
    r,d=10,2
    pg.draw.line(prozor, pg.Color("white"), (x-r,y), (x+r,y),d)
    pg.draw.line(prozor, pg.Color("white"), (x,y-r), (x,y+r),d)
    pg.draw.line(prozor, pg.Color("white"), (x-r/2,y-r/2), (x+r/2,y+r/2),d)
    pg.draw.line(prozor, pg.Color("white"), (x+r/2,y-r/2), (x-r/2,y+r/2),d)
#bojimo pozadinu prozora u plavo
prozor.fill(pg.Color("blue"))
broj_zvezdica=8
razmakx=sirina//(broj_zvezdica+1)
razmaky=visina//(broj_zvezdica+1)
for i in range(broj_zvezdica):
    for j in range(broj_zvezdica):
        x=(i+1)*razmakx
        y=(j+1)*razmaky
        zvezdica(x,y)
        
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


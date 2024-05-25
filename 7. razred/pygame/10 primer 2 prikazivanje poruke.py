import pygame as pg
pg.init()
pg.display.set_caption("poruka")

(sirina, visina) = (500, 200)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

#font kojim će biti prikazan tekst font
font=pg.font.SysFont("Arial", 40)

#poruka koja će se ispisivati
poruka ="Ovo je PyGame!!!" 

#gradimo sličicu koja predstavlja tu poruku ispisanu crnom bojom
tekst = font.render(poruka, True, pg.Color("black")) 

#odredujemo veličinu tog teksta (da bismo mogli da ga centriramo).
(sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())

#položaj (координате левог угла) odredujemo tako da tekst bude centriran
#(половина разлике између димензија екрана и димензија слике која се приказује)
(x, y)=((sirina - sirina_teksta) /2,(visina - visina_teksta) / 2)

# prikazujemo sličicu na odgovarajućem mestu na ekranu
prozor.blit (tekst, (x, y))

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

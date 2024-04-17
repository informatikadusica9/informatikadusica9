import pygame as pg
pg.init()
pg.display.set_caption ("plavi robot")
(sirina, visina)=(400, 400)

prozor=pg.display.set_mode ((sirina, visina))
prozor.fill(pg.Color("white"))
# crtamo plavi kvadrat i pravougaonik
pg.draw.rect (prozor, pg.Color("blue"), (150, 50, 100, 100))
pg.draw.rect (prozor, pg.Color("blue"), (125, 155, 150, 200))
# crtamo ruke
pg.draw.line (prozor, pg.Color("black"), (125, 160), (50, 260),5)
pg.draw.line (prozor, pg.Color("black"), (275, 160), (350, 260),5)
# crtamo levu nogu
pg.draw.line (prozor, pg.Color("black"), (160, 360), (160, 380),10)
pg.draw.line (prozor, pg.Color("black"), (160, 380), (140, 380),10)
# crtamo desnu nogu
pg.draw.line (prozor, pg.Color("black"), (240, 360), (240, 380),10)
pg.draw.line (prozor, pg.Color("black"), (240, 380), (260, 380),10)

pg.display.update()
while pg.event.wait().type!=pg.QUIT:
  pass
pg.quit ()


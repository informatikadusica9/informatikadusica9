 
import pygame as pg
import random
pg.init()
s = 500
v = 50
prozor = pg.display.set_mode((s, v))
pg.display.set_caption("Niz raznobojnih duži sa razmakom")
prozor.fill(pg.Color("white"))


praznine = 30
sredina = v // 2
x = 0
while x < s:
        boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pg.draw.line(prozor, boja, (x, sredina), (x + praznine, sredina), 5)
        x = x + 2 * praznine




pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

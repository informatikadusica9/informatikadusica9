#Na sajtu Vulkan znanja (https://vulkanznanje.rs/) ćeš
#u gornjem levom uglu uočiti logotip u vidu olovke u bojama
#zastave Republike Srbije.
#Pokušaj da ga nacrtaš u Pygame-u.

import pygame as pg
pg.init()
prozor = pg.display.set_mode((600,600))
pg.display.set_caption("Vulkan znanje za najbolje obrazovanje!")
prozor.fill(pg.Color("white"))
temenaSivo = ((300,200),(250,250),(225,250),(300,100),(375,250))
pg.draw.polygon(prozor,pg.Color("grey"),temenaSivo)
pg.draw.polygon(prozor,pg.Color("black"),temenaSivo,3)
temenaCrveno = ((233,500),(100,500),(225,250),(250,250))
pg.draw.polygon(prozor,pg.Color("red"),temenaCrveno)
pg.draw.polygon(prozor,pg.Color("black"),temenaCrveno,3)
temenaPlavo = ((233,500),(250,250),(300,200),(366,500))
pg.draw.polygon(prozor,pg.Color("blue"),temenaPlavo)
pg.draw.polygon(prozor,pg.Color("black"),temenaPlavo,3)
temenaBelo = ((366,500),(300,200),(375,250),(500,500))
pg.draw.polygon(prozor,pg.Color("white"),temenaBelo)
pg.draw.polygon(prozor,pg.Color("black"),temenaBelo,3)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()




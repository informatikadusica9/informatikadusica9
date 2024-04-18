def pretvaranjekm(metar):
    kilometar=metar//1000
    return kilometar
def pretvaranjem(metar):
    m=metar%1000
    return m
metar = int(input("Unesi metre: "))
print( pretvaranjekm(metar), "km")
print( pretvaranjem(metar), "m")

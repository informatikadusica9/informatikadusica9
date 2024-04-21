def draw_circle (x,y,color,rad):
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.circle(rad)
    t.fillcolor(color)
    t.end_fill()
    t.up()
    t.home()

import turtle
t=turtle.Turtle()
t.up
draw_circle(0,-50,"green", 50)
draw_circle(0,300,"green", 25)
draw_circle(200,200,"orange", 50)
draw_circle(0,-300,"orange", 20)
draw_circle(-200,200,"blue", 50)
draw_circle(300,0,"blue", 50)
draw_circle(-200,-200,"red", -50)
draw_circle(-300,0,"red", 50)
draw_circle(200,-200,"yellow", 50)

import turtle

def drawSquare(someTurtle):
    i=90
    j=0
    while(i<110):
        while(j<4):
            someTurtle.forward(100)
            someTurtle.right(i)
            j=j+1
        i=i+5
    #abc=turtle.Turtle()
    #abc.circle(100)
    
def drawArt():
    window=turtle.Screen() #window which pops up when prog starts running
    window.bgcolor("yellow")
    xyz=turtle.Turtle() #turtle->lib Turtle->class so 'xyz' is obj of Class 
    xyz.shape("turtle")
    xyz.color("green")
    xyz.speed(6)
    for i in range(1,30):
        drawSquare(xyz)
        xyz.right(10)
    window.exitonclick()
drawArt()

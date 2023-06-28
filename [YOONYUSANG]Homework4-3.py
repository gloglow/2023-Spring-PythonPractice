import turtle

t=turtle.Turtle()
global file

def moveto(x, y):
    t.goto(x,y)
    with open('coordinate.txt', 'a') as file:
        file.write((str(x))+' '+str(y)+'\n')

with open('coordinate.txt', 'a+') as file:
    file.seek(0)
    for line in file:
        print(line)
        a,b=map(float, line.split())
        t.goto(a,b)

turtle.onscreenclick(moveto)

turtle.done()
file.close()
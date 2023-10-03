import turtle

screen = turtle.Screen()
screen.title("Python Square")
screen.bgcolor("light green")
lion = turtle.Turtle()
againeSize = int(input("repeat : "))
size = int(input("size : "))

def ShinkingSquare(size):
    for keke in range(4):
        lion.forward(size)
        lion.left(90)
        size -= 10

for kele in range(againeSize):

    ShinkingSquare(size)
    size -= 30

turtle.done()

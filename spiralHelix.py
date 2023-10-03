import turtle

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("blue")
turtleScreen.title("Python  Spiral")

lion = turtle.Turtle()
lion.speed(5)
lion.color("red")
circleColor = ["red", "orange", "yellow", "black"]
for i in range(15):
    lion.color(circleColor[i % 4])
    lion.circle(i * 10)
    lion.circle(-i * 10)
    lion.left(i * 3)




turtle.done()
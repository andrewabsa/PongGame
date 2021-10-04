import turtle

class Startup():
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong by Andrew Absalan")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

#Paddle A
class Paddle_a():
    def __init__(self):
        self.paddle_a = turtle.Turtle()
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.penup()
        self.paddle_a.goto(-350, 0)

class Main():
    def __init__(self):
        self.wn = turtle.Screen()
        while True:
            self.wn.update()
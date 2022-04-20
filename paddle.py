from turtle import Turtle

MOVEMENT_SPEED = 20


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

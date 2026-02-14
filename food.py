from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-300,300),random.randint(-300,300))
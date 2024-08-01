from turtle import  Turtle
import random

#Making food class of child class of turtle

class Food(Turtle):
    """Calling super class method
    with super init"""

    def __init__(self):
        super().__init__()
        """Modifying turtle"""
        self.shape("circle")
        self.penup()
        self.color("blue")
        """Making size of circle"""
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        """Speed"""
        self.speed("fastest")
        """Calling refresh function"""
        self.refresh()


    """Making new function called refresh"""

    def refresh(self):
        """Making random x and y with help of randint"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        """Putting circle in random position in screen"""
        self.goto(random_x, random_y)
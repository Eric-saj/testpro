from turtle import Turtle


starting_position = [(0, 0), (-20, 0), (-40, 0)]
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.new_segment = Turtle("square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(position)
            self.segments.append(self.new_segment)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_cordy = self.segments[seg-1].ycor()
            new_cordx = self.segments[seg-1].xcor()
            self.segments[seg].goto(new_cordx,new_cordy)
        self.head.forward(20)




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)



    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

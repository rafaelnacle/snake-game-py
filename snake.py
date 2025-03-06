from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_2_x = self.segments[seg_num - 1].xcor()
            seg_2_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(seg_2_x, seg_2_y)
        self.segments[0].forward(MOVE_DISTANCE)
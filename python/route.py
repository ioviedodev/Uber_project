from tracemalloc import start
from turtle import end_fill


class Route:
    id      = int
    start   = []
    end     = []

    def __init__(self,id, start, end):
        self.id = id
        self.start = start
        self.end = end

    def print_object(self):
        print("id           : "+ str(self.id));
        print("start        : "+ self.start);
        print("end          : "+ self.end);
        
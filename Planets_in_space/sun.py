import turtle

class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp:float, x:float=0.0, y:float=0.0):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.x = x
        self.y = y
        # these are the graphic stuff
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.color("yellow")
        #initial position of the sun
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

    def get_radius(self)->float:
        return self.radius

    def get_mass(self) -> float:
        return self.mass

    def get_temp(self)->float:
        return self.temp

    def get_x_pos(self) -> float:
        return self.x

    def get_y_pos(self) -> float:
        return self.y

    def __str__(self):
        return f"Sun (name = {self.name}, radius = {self.radius}, mass = {self.mass}, temp = {self.temp}, x = {self.x}, y = {self.y}"
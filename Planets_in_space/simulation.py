import turtle
from solar_system import SolarSystem
from sun import Sun
from planets import Planet


class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods:int):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        # these are the graphic stuff
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width, height=self.height)
        self.t.clear()

    def run(self):
        self.solar_system.show_planets()
        for _ in range(self.num_periods):
            self.solar_system.move_planets()
            self.solar_system.show_planets()
        self.screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 10000000, 5800)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 5.0, 200.0, 25, color="green")
    solar_system.add_planets(earth)

    mars = Planet("MARS", .1, 10.0, 125.0, 62, color="red")
    solar_system.add_planets(mars)

    simulation = Simulation(solar_system, 500, 500, 2000)
    simulation.run()
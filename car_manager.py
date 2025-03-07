from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Randomly create a car
        random_chance = random.randint(1, 6)  # Adjust frequency here
        if random_chance == 1:
            new_car = Turtle("turtle")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_y = random.randint(-250, 250)
            new_car.goto(-300, new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
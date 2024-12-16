from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Initialize game components
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen to keyboard input
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.display_game_over()

    # Check if player has reached the top
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
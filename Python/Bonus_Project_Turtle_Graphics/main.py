import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# You can import sound and music as well

view_screen = Screen()
view_screen.setup(width=600, height=600)
view_screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

view_screen.listen()
view_screen.onkey(player.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    view_screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.crossed_finish_line():
        player.reset_turtle_position()
        scoreboard.increase_level()
        car_manager.increase_speed()
        # Make the speed increase at random

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.scoreboard_game_over()

view_screen.exitonclick()
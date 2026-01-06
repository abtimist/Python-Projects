import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
traffic = CarManager()
screen.listen()
screen.onkey(player.move_player,"Up")
level = Scoreboard()
level.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    screen.update()
    traffic.create_car()
    traffic.move_cars()

    if player.ycor()>280:
        level.add_point()
        traffic.increase_speed()
        player.reset_position()


    for cars in traffic.cars:
        if player.distance(cars)<20:
            level.game_over()
            game_is_on = False



screen.exitonclick()





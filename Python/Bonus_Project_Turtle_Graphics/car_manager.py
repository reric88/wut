from turtle import Turtle
import random
import time

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
CAR_MOVE_DISTANCE = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        # self.speed = CAR_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 20)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))

            # y_positions = [car.ycor() for car in self.all_cars]


            # if len(y_positions) > 0:
            #     max_y_position = max(y_positions)
            #     min_y_position = min(y_positions)
            #     start_y_position = min_y_position - (min_y_position % 20) + 20
            #     end_y_position = max_y_position + 20
            # else:
            #     start_y_position = -240
            #     end_y_position = 260

            random_position = (random.randrange(-4, 4) * 60)

            if random_position == last_random_position:
                rando

            if random_position % 2 == 0:
                car_speed = 1
            else:
                car_speed = 2

            # random_y_position = random.randrange(start_y_position, end_y_position)

            # random_y_position = random.randint(-240, 280)
            new_car.goto(240, random_position)
            
            # car_speed = random.randint(1, 2)
            new_car.speed = car_speed

            last_random_position = random_position
            self.all_cars.append(new_car)




    def move_cars(self):
        for car in self.all_cars:
            car.backward(car.speed)

    def stop_cars(self):
        for car in self.all_cars:
            car.backward(0)

    def increase_speed(self):
        for car in self.all_cars:
            car.speed *= 2














# from turtle import Turtle
# import random

# COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# CAR_MOVE_DISTANCE = 5

# class CarManager():
#     def __init__(self):
#         self.all_cars = []
#         self.speed = CAR_MOVE_DISTANCE

#     def create_car(self):
#         random_chance = random.randint(1, 6)
#         if (random_chance == 1):
#             new_car = Turtle('square')
#             new_car.penup()
#             new_car.shapesize(stretch_wid=1, stretch_len=2)
#             new_car.color(random.choice(COLORS))

#             random_y_position = random.randint(-240, 280)
#             new_car.goto(300, random_y_position)
#             self.all_cars.append(new_car)

#     def move_cars(self):
#         for car in self.all_cars:
#             car.backward(self.speed)

#     def stop_cars(self):
#         for car in self.all_cars:
#             car.backward(0)

#     def increase_speed(self):
#         self.speed += 5
import random
from re import S
import arcade

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.DARK_GREEN
        self.width = 16
        self.height = 16
        self.center_x = 250
        self.center_y = 250
        self.speed = 10
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
    def eat(self):
        self.score += 1
        self.width += 20

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.RED
        self.radians = 8
        self.width = 20
        self.height = 20
        self.center_x = random.randint(0, 500)
        self.center_y = random.randint(0, 400)
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radians, self.color)

    

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=400, title="Snake_Game")
        self.background_color = arcade.color.KHAKI
        self.food = Apple()
        self.plyer = Snake()

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.plyer.draw()

    def on_update(self, delta_time):
        if arcade.check_for_collision(self.plyer, self.food):
            self.plyer.eat()
            self.food = Apple()
        
    
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            #print("UP")
            self.plyer.center_y += self.plyer.speed
        elif symbol == arcade.key.DOWN:
            #print("Down")
            self.plyer.center_y -= self.plyer.speed
        elif symbol == arcade.key.LEFT:
            #print("Left")
            self.plyer.center_x -= self.plyer.speed
        elif symbol == arcade.key.RIGHT:
            #print("Right")
            self.plyer.center_x += self.plyer.speed


g = Game()
arcade.run()

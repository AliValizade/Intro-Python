import random
import arcade

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.DARK_GREEN
        self.width = 16
        self.height = 16
        self.center_x = 250
        self.center_y = 250
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)


class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.RED
        self.radians = 8
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


g = Game()
arcade.run()

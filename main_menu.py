import arcade


WIDTH = 1920
HEIGHT = 1080


class MainMenu(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.DARK_BLUE)
        arcade.set_viewport(0, WIDTH - 1, 0, HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Главное меню', WIDTH / 2, HEIGHT / 2, arcade.color.RED, font_size=100, anchor_x='center')

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        view = GameView()


class GameView(arcade.View):
    def __init__(self):
        super(GameView, self).__init__()
        self.player = None
        self.score = 0
        self.background = 0
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.background = arcade.Sprite("resources:")

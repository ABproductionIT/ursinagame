from ursina import *
from xo3x3x3 import level


class Game(Ursina):
    def __init__(self):
        super().__init__()
        window.fullscreen = True
        Entity(model='quad', scale=60, texture='white_cube', texture_scale=(60, 60), rotation_x=90, y=-5,
               color=color.light_gray)  # plane
        Entity(model='sphere', scale=100, texture='textures/sky0', double_sided=True)  # sky
        # Entity(model='models/xyz', texture='textures/xyz', scale=0.8)
        EditorCamera()
        camera.world_position = (0, 0, -15)
        self.model, self.texture = 'models/custom_cube', 'textures/cube_texture'
        self.load_game()

    def cubes_maker(self, x, y, z):
        if x == 0:
            Entity(name=(x, y, z),
                   model=self.model,
                   color=color.gray,
                   texture=self.texture,
                   position=(0, y, z))
        if x == 1:
            Entity(name=(x, y, z),
                   model=self.model,
                   color=color.gray,
                   texture=self.texture,
                   position=(2, y, z))
        if x == 2:
            Entity(name=(x, y, z),
                   model=self.model,
                   color=color.gray,
                   texture=self.texture,
                   position=(4, y, z))

    def load_game(self):
        combos = []
        for x in range(level):
            for y in range(level):
                for z in range(level):
                    if x == 0:
                       interval = 0
                       Cube_button(position=(0, y, z))
                    if x == 1:
                       interval = 2
                       Cube_button(position=(2, y, z))
                    if x == 2:
                       interval = 4
                       Cube_button(position=(4, y, z))

    def input(self, key):
        super().input(key)


class Cube_button(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
                   parent=scene,
                   model='cube',
                   color=color.gray,
                   highlight_color = color.lime,
                   texture='white_cube',
                   position=position)



if __name__ == '__main__':
    game = Game()
    game.run()

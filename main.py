from ursina import *


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

    def load_game(self):
        # kubikna sarqum u positiony x y z
        Entity(model=self.model, texture=self.texture, position=(0,0,1))
        Entity(model=self.model, texture=self.texture, position=(0,0,3))
        Entity(model=self.model, texture=self.texture, position=(0,0,5))


    def input(self, key):
        super().input(key)


if __name__ == '__main__':
    game = Game()
    game.run()

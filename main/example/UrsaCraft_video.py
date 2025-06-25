from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from sys import exit
import subprocess


print(f"\n\n\n\ninfo by the system<UrsaCraft_video.py<window>>\nfile path:{__file__}\n\n\n\n")
app = Ursina()
print(f"\n\n\n\ninfo by the system<UrsaCraft_video.py>\n\tfile path:{__file__}\n\n\n\n")
window.title = "3d" # window title

window.always_on_top = True

# Block textures and sound
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
block_pick = 1

# Window settings
window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
	global block_pick

	# Hand movement
	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	# Block pick and exit game
	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['escape']:
		print(f"\n\n\n\ninfo by the system<UrsaCraft_video.py>\n\tfile path:{__file__}\n\t<exit form game program>\n\n\n\n")
		exit()

class Voxel(Button):
	"""the class for the blocks in the game"""

	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		"""placing and breaking blocks"""
		if self.hovered:
			if key == 'left mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)

			if key == 'right mouse down':
				punch_sound.play()
				destroy(self)

class Sky(Entity):
	"""the class for the sky"""

	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	"""the class for the player hand"""
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

# Genarating the world
for z in range(20):
	for x in range(20):
		voxel = Voxel(position = (x,0,z))

player = FirstPersonController() # For the game play
sky = Sky() # Placing the sky 
hand = Hand() # Placing the player's hand

app.run()
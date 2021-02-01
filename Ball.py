# Ball
#
# A number of moving ball LED effects

import colorsys
from kivy.clock import Clock


class Ball:
	def __init__(self, strip):
		duration = 1.0
		self.strip = strip
		self.position = 0
		self.hue = 2/3
		framerate = 15
		self.velocity = duration*len(strip)/framerate

		Clock.schedule_interval(self.move, 1/framerate)

		return

	def move(self, dt):
		# clear strip
		for LED in self.strip:
			LED.setColor(0.0, 0.0, 0.0, 1.0)

		LEDBall = int(self.position)
		if LEDBall >= 0 and LEDBall < len(self.strip):
			rgb = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0)
			self.strip[LEDBall].setColor(rgb[0], rgb[1], rgb[2], 1.0)

		self.position += self.velocity

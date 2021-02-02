# Ball
#
# A number of moving ball LED effects

import colorsys
from kivy.clock import Clock


class Ball:
	def __init__(self, strip, duration=4.0, hue=0.0, reflect=False):
		self.strip = strip
		self.position = 0
		self.hue = hue
		self.reflect = reflect
		framerate = 15
		self.velocity = 1.0/framerate/duration

		Clock.schedule_interval(self.move, 1/framerate)

		return

	def move(self, dt):
		# clear strip
		for LED in self.strip:
			LED.setColor(0.0, 0.0, 0.0, 1.0)

		LEDPosition = int(self.position*len(self.strip))
		if LEDPosition >= 0 and LEDPosition < len(self.strip):
			rgb = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0)
			self.strip[LEDPosition].setColor(rgb[0], rgb[1], rgb[2], 1.0)

		self.position += self.velocity
		if self.reflect:
			if self.position >= 1.0:
				self.velocity = -self.velocity
				self.position += 2*self.velocity
			if self.position < 0.0:
				self.velocity = -self.velocity
				self.position += 2*self.velocity

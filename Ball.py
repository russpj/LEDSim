# Ball
#
# A number of moving ball LED effects

import colorsys
from kivy.clock import Clock


class Ball:
	def __init__(self, strip, duration=4.0, hue=0.0, reflect=False, fade=1.0):
		self.strip = strip
		self.numLEDs = len(strip)
		self.position = 0
		self.hue = hue
		self.reflect = reflect
		self.fade=fade
		framerate = self.numLEDs/duration
		self.velocity = 1

		Clock.schedule_interval(self.move, 1/framerate)

		return

	def move(self, dt):
		# clear strip
		for LED in self.strip:
			LED.reduceValue(self.fade)

		LEDPosition = self.position
		if LEDPosition >= 0 and LEDPosition < self.numLEDs:
			rgb = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0)
			self.strip[LEDPosition].setColor(rgb[0], rgb[1], rgb[2])

		self.position += self.velocity
		if self.reflect:
			if self.position >= self.numLEDs:
				self.velocity = -self.velocity
				self.position = self.numLEDs
			if self.position < 0:
				self.velocity = -self.velocity
				self.position = 0

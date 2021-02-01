# Breathe
#
# Breathe is an LED effect that pulses the brightness of the LEDs

import colorsys
from kivy.clock import Clock

class Breathe:
	def __init__(self, strip):
		self.strip = strip
		self.hue = 0.67
		self.saturation = 1.0
		self.brightness = 0.0
		self.brightenAmount = 0.1
		Clock.schedule_interval(self.brighten, 1/10.0)
		return

	def brighten(self, dt):
		for LED in self.strip:
			rgb = colorsys.hsv_to_rgb(self.hue, self.saturation, self.brightness)
			LED.setColor(rgb[0], rgb[1], rgb[2], 1.0)	

		self.brightness += self.brightenAmount
		if (self.brightness > 1.0):
			self.brightness = 1.0
			self.brightenAmount = -self.brightenAmount
		if (self.brightness <= 0.0):
			self.brightness = 0.0
			self.brightenAmount = -self.brightenAmount


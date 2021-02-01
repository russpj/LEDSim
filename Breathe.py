# Breathe
#
# Breathe is an LED effect that pulses the brightness of the LEDs

import colorsys
from kivy.clock import Clock

class Breathe:
	def __init__(self, strip, hue=0.0, saturation = 1.0, duration = 4.0):
		self.strip = strip
		self.hue = hue
		self.saturation = saturation
		self.brightness = 0.0
		framerate = 15
		self.brightenAmount = 2/(framerate*duration)
		Clock.schedule_interval(self.brighten, 1/framerate)
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


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from ColorFill import ColorFill


class Sample(App):
	def build(self):
		self.root = layout = FloatLayout()

		self.numStrips = 3
		self.lengthStrips = 20
		
		self.grid = GridLayout(rows = self.numStrips, pos_hint = {'center_x': .5, 'center_y': 0.5})
		layout.add_widget(self.grid)

		self.effects = []
		hue = 1/6
		for stripNum in range(self.numStrips):
			strip = []
			for LEDLocation in range(self.lengthStrips):
				LED = ColorFill()
				LED.setColor(0.0, 0.0, 0.0, 1.0)
				self.grid.add_widget(LED)
				strip.append(LED)
			self.effects.append(Breathe(strip, hue=hue, duration=3.0*(1/3+hue)))
			hue += 1/self.numStrips

		layout.bind(size=self.update_layout)

		return layout

	def update_layout(self, instance, value):
		squareSide = min(instance.size[0]/self.lengthStrips, instance.size[1]/self.numStrips)
		gridWidth = squareSide*self.lengthStrips
		gridHeight = squareSide*self.numStrips
		self.grid.size_hint_max = (gridWidth, gridHeight)
		return

if __name__ == '__main__':
	Sample().run()


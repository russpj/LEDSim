# ColorFill
#
# ColorFill is a Kivy Widget that supports a solid fill color

import colorsys
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class ColorFill(Widget):
	def __init__(self, **kwargs):
		super(ColorFill, self).__init__(**kwargs)
		self.bind(pos=self.redraw, size=self.redraw)
		return

	def redraw(self, instance, value):
		self.bg_rect.size = self.size
		self.bg_rect.pos = self.pos
		return

	def setColor(self, red, green, blue, alpha=1.0):
		self.red = red
		self.green = green
		self.blue = blue
		self.alpha = alpha
		self.canvas.clear()
		with self.canvas:
			Color(red, green, blue, alpha)
			self.bg_rect = Rectangle(pos = self.pos, size = self.size)
		return

	def setHSVColor(self, hue, saturation, value):
		rgb = colorsys.hsv_to_rgb(hue, saturation, value)
		self.setColor(rgb[0], rgb[1], rgb[2])
		return

	def reduceValue(self, reduction):
		hsv = colorsys.rgb_to_hsv(self.red, self.green, self.blue)
		value = max(0.0, hsv[2]-reduction)
		self.setHSVColor(hsv[0], hsv[1], value)

import colorsys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

class Sample(App):
	def build(self):
		self.root = layout = FloatLayout()

		self.numStrips = 3
		self.lengthStrips = 20
		
		self.grid = GridLayout(rows = self.numStrips, pos_hint = {'center_x': .5, 'center_y': 0.5})
		layout.add_widget(self.grid)
		self.LEDs = []
		hue = 0.0
		for stripNum in range(self.numStrips):
			strip = []
			for LEDLocation in range(self.lengthStrips):
				LED = ColorFill()
				brightness = LEDLocation / self.lengthStrips
				rgb = colorsys.hsv_to_rgb(hue, 1.0, brightness)
				LED.setColor(rgb[0], rgb[1], rgb[2], 1.0)
				self.grid.add_widget(LED)
				strip.append(LED)
			self.LEDs.append(strip)
			hue += 1/3

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

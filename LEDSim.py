import colorsys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.clock import Clock
from ColorFill import ColorFill


class Breathe:
	def __init__(self, strip):
		self.strip = strip
		self.hue = 0.67
		self.saturation = 1.0
		self.brightness = 0.0
		self.brightenAmount = 0.1
		Clock.schedule_interval(self.Brighten, 1/10.0)
		return

	def Brighten(self, dt):
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



class LEDSim(App):
	def build(self):
		self.root = layout = FloatLayout()

		self.numStrips = 1
		self.lengthStrips = 20
		
		self.grid = GridLayout(rows = self.numStrips, pos_hint = {'center_x': .5, 'center_y': 0.5})
		layout.add_widget(self.grid)
		self.LEDs = []
		for stripNum in range(self.numStrips):
			strip = []
			for LEDLocation in range(self.lengthStrips):
				LED = ColorFill()
				brightness = LEDLocation / self.lengthStrips
				LED.setColor(brightness, brightness, 1.0, 1.0)
				self.grid.add_widget(LED)
				strip.append(LED)
			self.LEDs.append(strip)

		layout.bind(size=self.update_layout)

		self.breathe = Breathe(self.LEDs[0])
			
		return layout

	def update_layout(self, instance, value):
		squareSide = min(instance.size[0]/self.lengthStrips, instance.size[1]/self.numStrips)
		gridWidth = squareSide*self.lengthStrips
		gridHeight = squareSide*self.numStrips
		self.grid.size_hint_max = (gridWidth, gridHeight)
		return

if __name__ == '__main__':
	LEDSim().run()

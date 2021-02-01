import colorsys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.clock import Clock
from ColorFill import ColorFill
from Breathe import Breathe

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

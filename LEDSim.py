from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.clock import Clock
from ColorFill import ColorFill

numStrips = 1
lengthStrips = 20

class LEDSim(App):
	def build(self):
		self.root = layout = FloatLayout()
		
		self.grid = GridLayout(rows = numStrips)
		layout.add_widget(self.grid)
		self.LEDs = []
		for stripNum in range(numStrips):
			strip = []
			for LEDLocation in range(lengthStrips):
				LED = ColorFill()
				brightness = LEDLocation / lengthStrips
				LED.setColor(brightness, brightness, 1.0, 1.0)
				self.grid.add_widget(LED)
				strip.append(LED)
			self.LEDs.append(strip)
			
		return layout

	
if __name__ == '__main__':
	LEDSim().run()

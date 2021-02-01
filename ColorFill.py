# ColorFill
#
# ColorFill is a Kivy Widget that supports a solid fill color

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
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

	def setColor(self, red, green, blue, alpha):
		self.canvas.clear()
		with self.canvas.before:
			Color(red, green, blue, alpha)
			self.bg_rect = Rectangle(pos = self.pos, size = self.size)
		return


class Sample(App):
	def build(self):
		self.root = layout = FloatLayout()

		self.numStrips = 3
		self.lengthStrips = 20
		
		self.grid = GridLayout(rows = self.numStrips, pos_hint = {'center_x': .5, 'center_y': 0.5})
		layout.add_widget(self.grid)
		self.LEDs = []
		for stripNum in range(self.numStrips):
			strip = []
			for LEDLocation in range(self.lengthStrips):
				LED = ColorFill()
				brightness = LEDLocation / self.lengthStrips
				if stripNum == 0:
					LED.setColor(1.0, brightness, brightness, 1.0)
				if stripNum == 1:
					LED.setColor(brightness, 1.0, brightness, 1.0)
				if stripNum == 2:
					LED.setColor(brightness, brightness, 1.0, 1.0)
				self.grid.add_widget(LED)
				strip.append(LED)
			self.LEDs.append(strip)

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

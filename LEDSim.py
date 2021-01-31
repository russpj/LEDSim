from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.clock import Clock

class ColorFill(Widget):
	def __init__(self, **kwargs):
		super(Widget, self).__init__(**kwargs)

		with self.canvas:
			Color(0.4, 0.4, 1.0, 1.0)
			self.bg_rect = Rectangle(pos = self.pos, size = self.size)
		return

	def redraw(self):
		self.bg_rect.size = self.size
		self.bg_rect.pos = self.pos
		return

class LEDSim(App):
	def build(self):
		self.root = layout = GridLayout()
		layout.bind(size=self._update_rect, pos=self._update_rect)

		with layout.canvas.before:
			Color(0.1, .9, 0.1, 1)  # green; colors range from 0-1 not 0-255
			self.rect = Rectangle(size=layout.size, pos=layout.pos)
			
		return layout

	def _update_rect(self, instance, value):
		self.root.canvas.clear()
		self.rect.pos = instance.pos
		self.rect.size = instance.size

	
if __name__ == '__main__':
	LEDSim().run()

# ColorFill
#
# ColorFill is a Kivy Widget that supports a solid fill color

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
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
		self.root = layout = GridLayout(cols=1)
		LED = ColorFill()
		LED.setColor(0.4, 0.4, 1.0, 1.0)
		layout.add_widget(LED)
			
		return layout

	
if __name__ == '__main__':
	Sample().run()

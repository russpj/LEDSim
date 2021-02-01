# ColorFill
#
# ColorFill is a Kivy Widget that supports a solid fill color

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


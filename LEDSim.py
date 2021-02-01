from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.clock import Clock
from ColorFill import ColorFill

class LEDSim(App):
	def build(self):
		self.root = layout = GridLayout(cols=1)
#		layout.bind(size=self._update_rect, pos=self._update_rect)
		LED = ColorFill()
		LED.setColor(0.4, 0.4, 1.0, 1.0)
		layout.add_widget(LED)

#		with layout.canvas.before:
#			Color(0.1, .9, 0.1, 1)  # green; colors range from 0-1 not 0-255
#			self.rect = Rectangle(size=layout.size, pos=layout.pos)
			
		return layout

#	def _update_rect(self, instance, value):
#		self.root.canvas.clear()
#		self.rect.pos = [instance.pos[0], instance.size[1]/2]
#		size = [instance.size[0], instance.size[1]/2]
#		self.rect.size = size

	
if __name__ == '__main__':
	LEDSim().run()

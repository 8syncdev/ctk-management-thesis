import customtkinter as ctk
from random import choice
from typing import Literal

class SlideControl(ctk.CTkFrame):
	def __init__(self, parent, start_pos, end_pos, options = {
		'rely': 0.05,
		'relheight': 0.5,
	}, time_duration = 0.05, direction: Literal['x', '-x', 'y', '-y'] = 'x'):
		super().__init__(master = parent)

		self.options = {
			'rely': options.get('rely'),
			'relheight': options.get('relheight'),
		}

		self.time_duration = time_duration # Time duration for each animation

		self.direction = direction

		# general attributes 
		self.start_pos = start_pos
		self.end_pos = end_pos
		self.width = abs(start_pos - end_pos)

		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# layout
		self.place(relx = self.start_pos, relwidth = self.width, **self.options)

	def animate(self):
		if self.in_start_pos:
			self.animate_forward() 
		else:
			self.animate_backwards()

	def animate_forward(self):
		self.forward()

	def animate_backwards(self):
		self.backward()

	def forward(self):
		if ((self.pos < self.end_pos) if self.direction in ['x', 'y'] else (self.pos > self.end_pos)):
			self.pos += self.time_duration if self.direction in ['x', 'y'] else -self.time_duration
			self.place(relx = self.pos, relwidth = self.width, **self.options)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False
	
	def backward(self):
		if ((self.pos > self.start_pos) if self.direction in ['x', 'y'] else (self.pos < self.start_pos)):
			self.pos += -self.time_duration if self.direction in ['x', 'y'] else self.time_duration
			self.place(relx = self.pos, relwidth = self.width, **self.options)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True
import customtkinter as ctk
from random import choice

class SlideControl(ctk.CTkFrame):
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent)

		self.options = {
			'rely': 0.05,
			'relheight': 0.5,
		}

		self.time_duration = 0.05 # Time duration for each animation

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
		if self.pos < self.end_pos:
			self.pos += self.time_duration
			self.place(relx = self.pos, relwidth = self.width, **self.options)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos > self.start_pos:
			self.pos -= self.time_duration
			self.place(relx = self.pos, relwidth = self.width, **self.options)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True
# Michael Chan 18562 
# Graficas por Computadora 
# SR1Point

import struct 

def char(input):
	return struct.pack('=c', input.encode('ascii'))

def word(input):
	return struct.pack('=h', input)

def dword(input):
	return struct.pack('=l', input)

def glColor(r, g, b):
	return bytes([b, g, r])

BLACK = glColor(0, 0, 0)

class Render(object):
	def glInit(self):
		self.width = 640
		self.height = 480
		self.xViewport = 0
		self.yViewport = 0
		self.viewportWidth = 0
		self.viewportHeight = 0
		self.color = glColor(255, 255, 255)
		self.clearColor = glColor(0, 0, 0)
		self.glClear()

	def glColorPoint(self, r, g, b):
		self.color = glColor(round(r * 255), round(g * 255), round(b * 255))

	def glCreateWindow(self, width = 640, height = 480):
		self.width = width
		self.height = height

	def glViewport(self, x, y, width, height):
		self.xViewport = x
		self.yViewport = y
		self.viewportWidth = width
		self.viewportHeight = height

	def glClear(self):
		print(self.width)
		print(self.height)
		self.framebuffer = [
			[BLACK for i in range(self.width)]
			for j in range(self.height)
		]
		print(self.framebuffer)


	def glClearColor(self, r, g, b):
		self.clearColor = glColor(round(r * 255), round(g * 255), round(b * 255))
		self.framebuffer = [
            [clearColor for x in range(self.width)] for y in range(self.height)
        ]

	def pixel(self, x, y):
		print(x)
		print(y)

		self.framebuffer[y][x] = self.color

	def glVertex(self, x, y):
		xPoint = round((x+1) * (self.viewportWidth / 2) + self.xViewport)
		yPoint = round((y+1) * (self.viewportHeight / 2) + self.yViewport)
		self.pixel(xPoint, yPoint)

	def glFinish(self, filename):
		f = open(filename, 'bw')

		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(54 + self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(54))

		f.write(dword(40))
		f.write(dword(self.width))
		f.write(dword(self.height))
		f.write(word(1))
		f.write(word(24))
		f.write(dword(0))
		f.write(dword(self.width * self.height * 3))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))

		for x in range(self.height):
			for y in range(self.width):
				f.write(self.framebuffer[x][y])

		f.close()
	
bmp = Render()

bmp.glInit()
bmp.glCreateWindow(640, 480)
bmp.glColorPoint(0.53, 0.48, 0.90)
bmp.glViewport(10, 10, 400, 300)
bmp.glVertex(0, 0)
bmp.glFinish('out.bmp')



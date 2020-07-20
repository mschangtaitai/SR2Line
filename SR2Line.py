from SR1Point import Render, glColor

r = Render()
r.glInit()
r.glCreateWindow(640, 480)
r.glViewport(10, 10, 400, 300)

def glLine(x1input, y1input, x2input, y2input):
	x1 = round((x1input+1) * (r.viewportWidth / 2) + r.xViewport)
	x2 = round((x2input+1) * (r.viewportWidth / 2) + r.xViewport)
	y1 = round((y1input+1) * (r.viewportHeight / 2) + r.yViewport)
	y2 = round((y2input+1) * (r.viewportHeight / 2) + r.yViewport)
	dy = y2 - y1
	dx = x2 - x1

	steep = dy > dx

	if steep:
		x1, y1 = y1, x1
		x2, y2 = y2, x2

	if x1 > x2:
		x1, x2 = x2, x1
		y1, y2 = y2, y1

	dy = abs(y2 - y1)
	dx = abs(x2 - x1)

	offset = 0
	threshold = dx

	y = y1
	for x in range(round(x1), round(x2)):
		print(x, y)
		if steep:
			r.pixel(y, x)
		else:
			r.pixel(x, y)

		offset += dy * 2
		if offset >= threshold:
			y += 1 if y1 < y2 else - 1
			threshold += 2 * dx

glLine(-0.2, -0.2, 0.5, 1)

r.glFinish("out2.bmp")


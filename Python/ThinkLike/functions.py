import turtle

def draw_multicolor_square(t,sz):
	for i in ['red', 'purple', 'hotpink', 'blue']:
		t.color(i)
		t.forward(sz)
		t.left(90)

wn= turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range (15):
	draw_multicolor_square(tess, size)
	size += 11
	tess.forward(100)
	tess.right(18)
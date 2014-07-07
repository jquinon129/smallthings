import turtle
tess = turtle.Turtle()
tess.shape('turtle')
tess.color('red')
#print type(tess)
for i in range(12):
	tess.penup()
	tess.forward(80)
	tess.pendown()
	tess.forward(20)
	tess.penup()
	tess.stamp()
	tess.backward(100)
	tess.left(30)


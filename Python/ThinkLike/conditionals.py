import turtle

def draw_bar(t, height):
	t.pendown()
	t.begin_fill()
	t.left(90)
	t.forward(height)
	t.write(' ' + str(height))
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.left(90)
	t.end_fill()
	t.penup()
	t.forward(10)

def make_turtle(color1, color2, size):
	t = turtle.Turtle()
	t.color(color1,color2)
	t.pensize(size)
	return t

def make_window(color, title):
	w = turtle.Screen()
	w.bgcolor(color)
	w.title(title)
	return w


# wn = make_window('lightgreen', 'Get Got')
# alex = make_turtle('blue', 'red', 3)

# xs = [48, 117, 200, 240, 160, 260, 220]

# for i in xs:
# 	draw_bar(alex, i)

#name of day ranging from 0 to 7
def numdays(num):
	dayname = ['Sunday','Monday', 'Tuesday', 'Wednesday', "Thor's day", 'Friday', 'Sat']
	return dayname[num]

#name of day when you leave at start day and return on end day
def retday(start, end):
	dayname = ['Sunday','Monday', 'Tuesday', 'Wednesday', "Thor's day", 'Friday', 'Sat']
	dayret= dayname[(end + start) % 7]
	return dayret

def grade(num):
	if num >= 75
		return 'First'
	elif num 
	elif num 
	else
		return 'F3'
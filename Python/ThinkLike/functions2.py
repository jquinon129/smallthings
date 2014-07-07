import turtle

def draw_square(t, sz):
	for i in range(4):
		t.forward(sz)
		t.left(90)
	return t

def draw_poly(t, n, sz):
	for i in range(n):
		t.forward(sz)
		t.left(360/n)



def make_window(color, title):
	w = turtle.Screen()
	w.bgcolor(color)
	w.title(title)
	return w

def make_turtle(color, size):
	t = turtle.Turtle()
	t.color(color)
	t.pensize(size)
	return t

def draw_square(t, size):
	for i in range (4):
		t.forward(size)
		t.left(90)


w = make_window('lightgreen', 'heh')
alex = make_turtle('hotpink', 3)

#five squares
# for i in range(5):
# 	draw_square(alex, 20)
# 	alex.penup()
# 	alex.forward(40)
# 	alex.pendown()

#inner squares
# size = 20
# for i in range(5):
# 	draw_square(alex, size)
# 	size += 20
# 	alex.penup()
# 	alex.backward(10)
# 	alex.right(90)
# 	alex.forward(10)
# 	alex.left(90)
# 	alex.pendown()

#draw_poly test
#draw_poly(alex, 8, 50)

#for i in range (20):
#not sure...


# #draw spiral
# size = 5
# right = 90
# alex.right(180)
# for i in range(20):
# 	alex.forward(size)
# 	size +=5
# 	alex.right(right)
# 	right -= .3

# equilateral trianlge
# def draw_equitrianlge(t, sz):
# 	draw_poly(t, 3, sz)

# draw_equitrianlge(alex, 100)

#sum to n
# def sum_to(n):
# 	tot = 0
# 	for i in range(n+1):
# 		tot +=i
# 	return tot

# print sum_to(10)

#area of circle
# def area_of_circle(r):
# 	area = (r **2) * 3.14
# 	return area

# def draw_star(t, sz):
# 	for i in range(5):
# 		t.right(144)
# 		t.forward(sz)

def draw_superstar(t,sz):
	for i in range(5):
#		t.penup()
		t.right(144)
		t.forward(300)
#		t.pendown()
		for i in range(5):
			t.right(144)
			t.forward(sz)

draw_superstar(alex, 100)
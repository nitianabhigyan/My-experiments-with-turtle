import turtle 

pen = turtle.Turtle()
pen.clear()
pen.color("#d2d2d2")
turtle.setup(.95,.8)

print("CLick to kill")


def sword(x = 200):
	def rod(t = x):
		pen.fd(t)
		pen.circle(int(x/6),180)
		pen.fd(t)
	
	def sides(y = x):
		pen.fd(y/3)
		pen.circle(y/15,180)
		pen.fd(y/3)

	turtle.bgcolor("#b4b4b4")
	pen.fillcolor("#12d112")
	pen.begin_fill()
	pen.lt(90)
	rod()  # Shaft
	pen.end_fill()
	pen.begin_fill()
	pen.fillcolor("#121212")
	pen.rt(90)
	sides() # First on left side
	pen.rt(90)
	rod(x/3) # Then bottom side
	pen.rt(90)
	sides() # first on left side
	pen.fd(x/3)
	pen.end_fill()
	pen.home()
	
	

pen.reset()
sword()

turtle.exitonclick()
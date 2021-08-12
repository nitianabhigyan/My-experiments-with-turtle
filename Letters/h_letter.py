import turtle 

pen = turtle.Turtle()
pen.clear()
pen.color("#d2d2d2")
turtle.setup(.95,.8)
print("CLick to kill")


"""
Goal: Exploit the symmetry.
1. Vertical symettry in "H"
"""
def draw_half(base=200,side = 90):
	pen.forward(base)
	pen.right(side)
	pen.forward(int(base/10))
	pen.right(side)
	pen.forward(int(base/2) - int(base/10))  # Stop a little before midpoint
	pen.left(side)
	pen.forward(int((base/2)/2))
	pen.right(side)  # Face down again.
	# Lift the pen and bridge the gap
	pen.up()
	pen.forward(int(base/10))
	pen.down()
	# Start again.
	pen.right(side)
	pen.forward(int((base/2)/2))
	pen.left(side)
	pen.forward(int(base/2))  # base/10 not needed as ALREADY moved by that length.
	pen.right(side)
	pen.forward(int(base/10))


pen.reset()
pen.left(90)  # face up.
draw_half()
pen.home()

turtle.exitonclick()
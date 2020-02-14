import turtle
import tkinter as tk

#function to lift the pen, moves the turtle cursor to the top left corner, and sets the pen back down
def corner(borderSize):
	turtle.seth(0)
	turtle.pu()
	turtle.goto(-round(borderSize/2), round(borderSize/2))
	turtle.pd()
#

#function to move the turtle cursor to the top left grid square
def start(squareSize):
	turtle.pu()
	turtle.fd(squareSize/2)
	turtle.rt(90)
	turtle.fd(squareSize/2)
	turtle.lt(90)
#

#function to draw the board
def drawBoard(board, size):
	root = tk.Tk()
	screenHeight = root.winfo_screenheight()		#create a tk object to grab the screen height
	
	
	turtle.title("Board")			#sets the title of the turtle window
	turtle.setup(screenHeight,screenHeight,0,0)		#sets the initial size of the turtle window
	turtle.ht()
	
	root.destroy()				#destroy the tk window now that we don't need it anymore
	
	
	
	square = round((screenHeight-(screenHeight/10))/size)		#length of each square, including width of one border
	border = square*size+1			#the length of the entire border, including the width of each border
	
	
	
	turtle.tracer(0,0)
	
	corner(border)
	
	#draws the borders for the box
	i = 0
	while i < 4:
		turtle.fd(border)
		turtle.rt(90)
		
		i += 1
	#
	
	#draws the vertical lines for the grid
	i = 0
	while i < size-1:
		turtle.fd(square)
		turtle.rt(90)
		turtle.fd(border)
		turtle.bk(border)
		turtle.lt(90)
		
		i += 1
	#
	
	#draws the horizontal lines for the grid
	corner(border)
	turtle.rt(90)
	i = 0
	while i < size-1:
		turtle.fd(square)
		turtle.lt(90)
		turtle.fd(border)
		turtle.bk(border)
		turtle.rt(90)
		
		i += 1
	#
	
	corner(border)
	start(square)
	
	style = ('Courier', 30)
	
	i = 0
	j = 0
	while i < size:
		while j < size:
			boardNumber = board[i][j]
			turtle.write(boardNumber, font=style, align = 'center')
			
			turtle.fd(square)
			j += 1
		#
		
		#returns to the beginning of the row and goes down to the next row
		turtle.bk(square*size)
		turtle.rt(90)
		turtle.fd(square)
		turtle.lt(90)
		
		j = 0
		i += 1
	
	corner(border)
	turtle.update()
	

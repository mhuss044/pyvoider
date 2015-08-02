'''
game

3D projected,
   screens;
	main view
		radar
		vehicle orientation
		ammo/weapon status

'''
'''
var = "put"
v = 'red'
n = 4

print "ff:",n,",",var,"are there",v
print "gg:%d, %s, %s" % (n+2, v, var)
'''

from math import sin
from math import cos
from math import radians
import curses	# curses lib
from curses import wrapper

engineRad = [0, 10, 20, 30, 40]
winDivide = 0;
mainWindef = { 'xTop' : 0, 'yTop' : 0, 'height' : 1, 'width' : 1, 'mainWin' : 0 }  

class gameWindow(object):
	def __init__(self, xT, yT, h, w):
		self.xTop = xT
		self.yTop = yT
		self.height = h
		self.width = w
	def makeWin(self, wObj):
		self.winObj = wObj
	def changeDim(self, xT, yT, h, w):
		self.xTop = xT
		self.yTop = yT
		self.height = h
		self.width = w
#		return true
	
print "Voider Game"
def main(stdscr):

	stdscr = curses.initscr()	# init curses, return a window obj
	stdscr.clearok(1)		# makes next call to refresh clear the window as well
	winDivide = curses.COLS - 40	# x pos of HUDs to draw

	# setup main window where stuff coming at player is drawn, fire into mid of screen
	mainWin = gameWindow( 0, 0, curses.LINES, winDivide)
	mainWin.makeWin( curses.newwin( mainWin.height, mainWin.width, mainWin.yTop, mainWin.xTop))

	# set HUD windows
	radarWin = gameWindow( winDivide, 0, int(curses.LINES/3), 40)
	radarWin.makeWin( curses.newwin( radarWin.height, radarWin.width, radarWin.yTop, radarWin.xTop))

	oriWin = gameWindow( winDivide, int(curses.LINES/3), int(curses.LINES/3), 40)
	oriWin.makeWin( curses.newwin( oriWin.height, oriWin.width, oriWin.yTop, oriWin.xTop))

	ammoStatusWin = gameWindow( winDivide, int(curses.LINES/3)*2, int(curses.LINES/3), 40)
	ammoStatusWin.makeWin( curses.newwin( ammoStatusWin.height, ammoStatusWin.width, ammoStatusWin.yTop, ammoStatusWin.xTop))

	# Set some properties
	curses.noecho()			# do not output inputted char to screen
	curses.cbreak()			# dont wait for 'enter' pressed to respond to input
	curses.curs_set(False)		# no blinking cursor
	stdscr.keypad(True)		# allows recog of LEY_LEFT, PAGE_UP
	stdscr.nodelay(True)		# make getch(), and getKey non block


	# This raises ZeroDivisionError when i == 10.
	'''
	for i in range(0, 11):
	    v = i-10
		    stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
		    '''
	if curses.can_change_color():
		print "Can use colour"
	elif curses.can_change_color():
	 	print "c"
	else:
	 	print "cc"

	mainWin.winObj.border('x','x','x','x','*','*','*','*')	# ls, rs, ts, bs, tl, tr, bl, br	
#	mainWin.winObj.box(1, 160)
	radarWin.winObj.border('x','x','x','x','*','*','*','*')	# ls, rs, ts, bs, tl, tr, bl, br	
	oriWin.winObj.border('x','x','x','x','*','*','*','*')	# ls, rs, ts, bs, tl, tr, bl, br	
	ammoStatusWin.winObj.border('x','x','x','x','*','*','*','*')	# ls, rs, ts, bs, tl, tr, bl, br	

	while( (stdscr.getch() != ord('q')) and (stdscr.getch != curses.KEY_EXIT) ):
		for i in range(0, 5):
			for ang in range(0, 360):
				x = int(mainWin.height/2 + engineRad[i]*sin(radians(ang)))
				y = int(mainWin.width/2 + engineRad[i]*cos(radians(ang)))
				if x > 0 and x < mainWin.width:
					if y > 0 and y < mainWin.height:
						mainWin.winObj.addch(y, x, ord('*'))
			if engineRad[i] < 40:
				engineRad[i] += 5
			else:
				engineRad[i] = 0

#		mainWin.winObj.addch(10, 10, ord('*'))

		mainWin.winObj.refresh()
		radarWin.winObj.refresh()
		oriWin.winObj.refresh()
		ammoStatusWin.winObj.refresh()
		stdscr.refresh()

	curses.endwin()			# deinit curses,& return terminal to previous state;echo,cbreak,keypad

wrapper(main)			# wrapper ensures that terminal is returned to its org state, incase main fails to restore state


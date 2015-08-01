'''
game

'''
'''
'''

import curses	# curses lib
from curses import wrapper
var = "put"
v = 'red'
n = 4

print "hello"

print "ff:",n,",",var,"are there",v
print "gg:%d, %s, %s" % (n+2, v, var)


stdscr = curses.initscr()	# init curses, return a window obj
def main(stdscr):

	begin_x = 20; begin_y = 7
	height = 5; width = 40
	win = curses.newwin(height, width, begin_y, begin_x)

	curses.noecho()			# do not output inputted char to screen
	curses.cbreak()			# dont wait for 'enter' pressed to respond to input
	stdscr.keypad(True)		# allows recog of LEY_LEFT, PAGE_UP


	# Clear screen
	stdscr.clear()

	# This raises ZeroDivisionError when i == 10.
	'''
	for i in range(0, 11):
	    v = i-10
		    stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
		    '''
	yMax = curses.LINES - 1
	xMax = curses.COLS - 1

	if(curses.can_change_color())

	stdscr.refresh()
#	stdscr.getkey()

	curses.endwin()			# deinit curses,& return terminal to previous state;echo,cbreak,keypad

wrapper(main)			# wrapper ensures that terminal is returned to its org state, incase main fails to restore state


import curses
import time

def animate(stdscr):
    curses.curs_set(0)  # Cursor verstecken
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # 100ms timeout
    
    x, y = 0, 5
    direction = 1
    
    while True:
        stdscr.clear()
        stdscr.addstr(y, x, "🚀")
        stdscr.refresh()
        
        x += direction
        if x >= 70 or x <= 0:
            direction *= -1
            
        if stdscr.getch() == ord('q'):
            break

curses.wrapper(animate)

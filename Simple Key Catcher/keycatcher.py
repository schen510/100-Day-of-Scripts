import sys
import threading
import tty
import termios

"""Simple asynchronous key capturer that is used to detect certain keys being pressed down"""

breakNow = False

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def waitForKeyPress():
    global breakNow

    while True:
        ch = getch()

        if ch == "q": # Or skip this check and just break
            breakNow = True
            break
        elif ch == "d":
            print "Sending Disturbance"
        elif ch == "b":
            print "Sending Fault"

def main():
    threads = []
    t = threading.Thread(target=waitForKeyPress, args=())
    threads.append(t)
    t.start()

    while breakNow == False:
        pass

if __name__ == '__main__':
    main()



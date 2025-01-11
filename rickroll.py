import time
import webbrowser

timer = 0
while timer < 3:
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    timer = timer + 1

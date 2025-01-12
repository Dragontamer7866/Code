import time
import webbrowser

version = input("Would you like the Normal, Meow Meow, or Villager covers? ")
if version == "Normal":
    timer = 0
    while timer < 3:
        time.sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        timer = timer + 1

elif version == "Meow Meow":
    timer = 0
    while timer < 3:
        time.sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=dmA6_0ZwWb4")
        timer = timer + 1

elif version == "Villager":
    timer = 0
    while timer < 3:
        time.sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=2GXlAJPa-KM")
        timer = timer + 1

else:
    timer = 0
    while timer < 3:
        time.sleep(1)
        webbrowser.open("https://youtu.be/2U4E-RXHshc?si=VMqvKCvt3M4fQ-OO")
        timer = timer + 1

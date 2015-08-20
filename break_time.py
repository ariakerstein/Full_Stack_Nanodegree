import webbrowser
import time

time.sleep(3)
webbrowser.open("http:www.ariakerstein.com")

i=1
cycles = []

print("This Program started on " +time.ctime())
while i < 3:
	webbrowser.open("http:www.ariakerstein.com")
	cycles.append(i)
	i = i + 1
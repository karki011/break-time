import webbrowser
import time

time.sleep(10)
total_break = 3
break_count = 0

print("Break start on " + time.ctime())
while(break_count < total_break):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=EXmoX2DVSbM")
    break_count = break_count + 1
from tkinter import*
from datetime import datetime
import datetime
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import random
import time

root = Tk()
root.title("Budík")
root.geometry("400x200")


def set():
	global set_alarm_time
	user = int(hour.get())*3600+ int(min.get())*60 + int(sec.get())
	cas = datetime.datetime.now()
	curr = int(cas.hour)*3600 + int(cas.minute)*60 + int(cas.second)
	if (user - curr) < 0:
		set_alarm_time = (86400 - abs(user - curr))
	else :
		set_alarm_time = abs(user - curr)
	seznam()
waiting = []
run_once = 0
def seznam():
	global waiting
	global run_once
	waiting.append(set_alarm_time)
	if run_once == 0:
		run_once = run_once + 1
		alarm()
	else:
			pass


def alarm():
	if waiting:
		for i in range(len(waiting)):
			waiting[i] = waiting[i] - 1
			print (waiting)
		root.after(1000, alarm)
		if 0 in waiting:
			waiting.remove(0)
			print("Budíček")
			zvuk()
			
	else:
		print("Budíček")
		zvuk()
		exit()
			
def zvuk():
	zvuk1 = AudioSegment.from_mp3("C:/Users/42060/Desktop/pgs/a.mp3")
	zvuk2 = AudioSegment.from_mp3("C:/Users/42060/Desktop/pgs/b.mp3")
	zvuk3 = AudioSegment.from_mp3("C:/Users/42060/Desktop/pgs/c.mp3")
	zvuk4 = AudioSegment.from_mp3("C:/Users/42060/Desktop/pgs/d.mp3")
	zvuk5 = AudioSegment.from_mp3("C:/Users/42060/Desktop/pgs/e.mp3")
	zvuky = [zvuk1, zvuk2, zvuk3, zvuk4, zvuk5]
	pogzvuk = random.choice(zvuky)
	x = _play_with_simpleaudio(pogzvuk)
	time.sleep(15)
	x.stop()
	if not waiting:
		exit()

Label(root,text="Budík",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Zadejte čas",font=("Helvetica 15 bold")).pack(pady=15)

frame = Frame(root)
frame.pack()

hour = IntVar()
min = IntVar()
sec = IntVar()

hourTime= Entry(root,textvariable = hour,bg = "pink",width = 15).place(x=110,y=45)
minTime= Entry(root,textvariable = min,bg = "pink",width = 15).place(x=150,y=45)
secTime = Entry(root,textvariable = sec,bg = "pink",width = 15).place(x=200,y=45)

tlacitko = Button(root,text="Zapnout budík",font=("Helvetica 15"), command=set)
tlacitko.pack(pady=5)

root.mainloop()

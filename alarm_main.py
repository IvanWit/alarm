from sqlite3 import Time
from tkinter import*
from datetime import datetime
import datetime
from tokenize import String
from turtle import numinput
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import random
import time

root = Tk()
root.title("Budík")
root.geometry("400x250")

waiting = []
run_once = 0
prnt = StringVar()
display = []
def set():
	global set_alarm_time
	global nhour
	global nmin
	global nsec
	nhour = int(str(hour.get())[:2])
	nmin = int(str(min.get())[:2])
	nsec = int(str(sec.get())[:2])
	if nhour >= 24:
		warning()
	elif nmin >= 60:
		warning()
	elif nsec >= 60:
		warning()
	else:
		user = int(nhour)*3600 + int(nmin)*60 + int(nsec)
		cas = datetime.datetime.now()
		curr = int(cas.hour)*3600 + int(cas.minute)*60 + int(cas.second)
		if (user - curr) < 0:
			set_alarm_time = (86400 - abs(user - curr))
		else :
			set_alarm_time = abs(user - curr)
		seznam()

def warning():
	war = Toplevel(root)
	war.geometry("600x75")
	war.title("POZOR!")
	Label(war, text="Chybné zadání času!", font=("helvetica 40 bold"), fg="red", anchor=CENTER).pack()
def seznam():
	global waiting
	global run_once
	set_u = "{:02d}:{:02d}:{:02d}".format(nhour, nmin, nsec)
	display.append(set_u)
	prnt.set(", ".join(display))
	waiting.append(set_alarm_time)
	if run_once == 0:
		run_once = run_once + 1
		alarm()
	else:
			pass


def alarm():	

	if waiting:
		for i in range(len(waiting)):
			if i >= len(waiting):
				i = 0
			elif i < 0:
				i = 0
			waiting[i] = waiting[i] - 1
			print (waiting, i)
			if waiting[i] <= 0:
				waiting.remove(waiting[i])
				print("Budíček")
				sound()
		root.after(1000, alarm)
	else:
		print("Budíček")
		sound()
		exit()
			
def sound():
	sound1 = AudioSegment.from_mp3("a.mp3")
	sound2 = AudioSegment.from_mp3("b.mp3")
	sound3 = AudioSegment.from_mp3("c.mp3")
	sound4 = AudioSegment.from_mp3("d.mp3")
	sound5 = AudioSegment.from_mp3("e.mp3")
	sounds = [sound1, sound2, sound3, sound4, sound5]
	pogsound = random.choice(sounds)
	x = _play_with_simpleaudio(pogsound)
	for z in range(len(waiting)):
		waiting[z] = waiting[z] - 15
	time.sleep(15)
	x.stop()
	if not waiting:
		exit()

Label(root, text="Budík", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Zadejte čas", font=("Helvetica 15 bold")).pack(pady=10)
Label(root, textvariable=prnt, font=("Helvetice 10"), wraplengt=300).pack(pady=5)

frame = Frame(root)
frame.pack()

hour = IntVar()
min = IntVar()
sec = IntVar()


hourTime= Entry(root, textvariable=hour, bg="pink", width=15).place(x=110,y=45)
minTime= Entry(root, textvariable=min, bg="pink", width=15).place(x=150,y=45)
secTime = Entry(root, textvariable=sec, bg="pink", width=15).place(x=200,y=45)

tlacitko = Button(root,text="Zapnout budík",font=("Helvetica 15"), command=set)
tlacitko.pack(pady=5)

root.mainloop()

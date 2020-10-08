import os
import time
import random
import datetime
#import pygame # if you don't have pygame: sudo apt-get install python-pygame
#also that line is commented out as we import the mixer specifically a bit further down.

startdelay = 0
musicdir = '/home/pi/music'
maxvolume = 0.6
volumefadespeed = 0.02
restart = True
startsong = ""

d = datetime.date.today()
if d.month == 12:
	musicdir = '/home/pi/music/winter'

bgm = [mp3 for mp3 in os.listdir(musicdir) if mp3[-4:] == ".mp3" or mp3[-4:] == ".ogg"]

lastsong = -1
currentsong = -1
from pygame import mixer
mixer.init()
random.seed()
volume = maxvolume

#TODO: Fill in all of the current RetroPie Emulator process names in this list.
emulatornames = ["retroarch","ags","uae4all2","uae4arm","capricerpi","linapple","hatari","stella","atari800","xroar","vice","daphne","reicast","pifba","osmose","gpsp","jzintv","basiliskll","mame","advmame","dgen","openmsx","mupen64plus","gngeo","dosbox","ppsspp","simcoupe","scummvm","snes9x","pisnes","frotz","fbzx","fuse","gemrb","cgenesis","zdoom","eduke32","lincity","love","kodi","alephone","micropolis","openbor","openttd","opentyrian","cannonball","tyrquake","ioquake3","residualvm","xrick","sdlpop","uqm","stratagus","wolf4sdl","solarus","drastic","nds","moonlight","steamlink.sh","streaming_clien","wolf4sdl.sh"]

def esRunning():
	running = False
	pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
	for pid in pids:
		try:
			procname = open(os.path.join('/proc',pid,'comm'),'rb').read()
			#if procname[:-1] == "emulationstatio":
			if "emulationstatio" in str(procname[:-1]):
				running = True
		except IOError:	
			continue
	return running

esStarted = False
while not esStarted:
	time.sleep(1)
	esStarted = esRunning()

if startdelay > 0:
	time.sleep(startdelay)
	
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
for pid in pids:
	try:
		procname = open(os.path.join('/proc',pid,'comm'),'rb').read()
		if procname[:-1] == "omxplayer" or procname[:-1] == "omxplayer.bin":
			while os.path.exists('/proc/'+pid):
				time.sleep(1)
	except IOError:	
		continue
		
if not startsong == "":
	try:
		currentsong = bgm.index(startsong)
	except:
		currentsong = -1

while True:
	while not esStarted:
		if mixer.music.get_busy():
			mixer.music.stop();
		time.sleep(10)
		esStarted = esRunning()
				
	if os.path.exists('/home/pi/DisableMusic'):
		print("DisableMusic found!")
		if mixer.music.get_busy():
			mixer.music.stop();
		while (os.path.exists('/home/pi/DisableMusic')):
			time.sleep(15)
		print("DisableMusic gone!")

	if not mixer.music.get_busy():
		while currentsong == lastsong and len(bgm) > 1:
			currentsong = random.randint(0,len(bgm)-1)
		song = os.path.join(musicdir,bgm[currentsong])
		mixer.music.load(song)
		lastsong=currentsong
		mixer.music.set_volume(maxvolume)
		mixer.music.play()
		print("BGM Now Playing: " + song)
	 
	emulator = -1;
	esStarted = esRunning()
	pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
	for pid in pids:
		try:
			procname = open(os.path.join('/proc',pid,'comm'),'rb').read()
			#if procname[:-1] in emulatornames:
			if "retroarch" in str(procname[:-1]):
				emulator = pid;
				print("Emulator found! " + str(procname[:-1]) + " Muting the music...")
				while volume > 0:
					volume = volume - volumefadespeed
					if volume < 0:
						volume=0
					mixer.music.set_volume(volume);
					time.sleep(0.05)			
				if restart:
					mixer.music.stop()
				else:
					mixer.music.pause()
				print("Muted.  Monitoring emulator.")
				while os.path.exists("/proc/" + pid):
					time.sleep(1);
				print("Emulator finished, resuming audio...")
				if not restart:
					mixer.music.unpause()
					while volume < maxvolume: 
						volume = volume + volumefadespeed;
						if volume > maxvolume:
							volume=maxvolume
						mixer.music.set_volume(volume);
						time.sleep(0.05)
				print("Restored.")
				volume=maxvolume

		except IOError:
			continue

	time.sleep(1);
	
print("An error has occurred that has stopped Test1.py from executing.") #theoretically you should never get this far.

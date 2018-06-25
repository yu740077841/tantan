import os
import time
import threading as thd
import random
huifu = "在吗，仙女"
huifu2 = "怎么不说话"
huifu3 = "加我v：nicaiyahehe，我怕把仙女弄丢了"
t = 2094

def notouch():
	cmd = 'adb shell input tap 419 1859'
	print(cmd)
	os.system(cmd)
	tie = random.randint(1,3)
	time.sleep(tie)
	
	
def touch():
	cmd = 'adb shell input tap 654 1856'
	print(cmd)
	os.system(cmd)
	
def suijitouch():
	for i in range(6,11):
		touch()
		tim = random.randint(1,6)
		time.sleep(tim)
		print(tim)

def start():
	suijitouch()
	notouch()
	

def dingshi():
	for e in range(500,800):
		start()
	tee = random.randint(300,1800)
	time.sleep(tee)
	

def zhaohuanwindows(y):
	print (y)
	cmd = "adb shell input tap 431 " + str(y)
	os.system(cmd)

def zhantie():
	cmd = 'adb shell input swipe 369 1294 369 1294 2000'
	print(cmd)
	os.system(cmd)
	cmd = "adb shell input tap 171 1155 "
	os.system(cmd)

def fuzhi():
	cmd = 'adb shell am broadcast -a clipper.set -e text '+ str(huifu)
	os.system(cmd)

def fuzhi2():
	cmd = 'adb shell am broadcast -a clipper.set -e text ' + str (huifu2)
	os.system(cmd)

def fuzhi3():
	cmd = 'adb shell am broadcast -a clipper.set -e text ' + str(huifu3)
	os.system(cmd)

def send():
	cmd = "adb shell input tap 980 2072 "
	os.system(cmd)


def backtohua():
	cmd = "adb shell input tap 78 194 "
	os.system(cmd)	

def backchat():
	cmd = "adb shell input tap 993 133 "
	os.system(cmd)

def shangfanye():
	cmd = "adb shell input swipe 386 577 386 1492 "
	os.system(cmd)

def ladaodi():
	for c in range(10,20):
		cmd = "adb shell input swipe 989 2016 31 605  "
		os.system(cmd)

def dianjikuangkuang():
	cmd = "adb shell input tap 431 2093 "
	os.system(cmd)	

def tuichu():
	cmd = "adb shell input tap 65 144 "
	os.system(cmd)




def liaotian():
	dianjikuangkuang()
	fuzhi()
	zhantie()
	send()
	fuzhi2()
	zhantie()
	send()
	fuzhi3()
	zhantie()
	send()
	
def chat():
	ladaodi()
	# zhaohuanwindows(t)
	
	# liaotian()
	# tuichu()
	for f in range(2,5):
		zhaohuanwindows(t)
		liaotian()
		tuichu()
		tiee = random.randint(1,6)
		time.sleep(tiee)


def final():
	dingshi()
	backchat()
	chat()
	backtohua()
	final()


final()
import time
print "Commands loaded!"
buildversion = 1.0
def help():
	print "Help    --> Shows this message."
	print "Version --> Shows the current version."
	print "Exit    --> Exits."
	print "Timer   --> Starts a timer dialogue."
def version():
	print "Version: ", buildversion
def timer(secs):
	secspassed = 0
	while(secspassed < secs):
		secspassed += 1
		time.sleep(1)
		print secspassed
		if (secspassed == secs):
			print secs, " seconds passed!"

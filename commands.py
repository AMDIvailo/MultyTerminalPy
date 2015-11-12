import time
buildversion = 1.1
codename = "Math adventures."
def help():
	print "Help    --> Shows this message."
	print "Version --> Shows the current version."
	print "Exit    --> Exits."
	print "Timer   --> Starts a timer dialogue."
def version():
	print "Version: ", buildversion, " - ", codename
def timer(secs):
	secspassed = 0
	while(secspassed < secs):
		secspassed += 1
		time.sleep(1)
		print secspassed
		if (secspassed == secs):
			print secs, " seconds passed!"
def calculator():
	calcmode = True
	print "Calculator mode enabled!"
	print "Use +, -, *, / to do arythmetic operations. Type exitcalc to disable the calculator mode. Type help to see this message again. "
	while(calcmode == True):
		calccommand = raw_input("Calculator command: ")
		if(calccommand == "exitcalc"):
			print "Calculator mode disabled!"
			calcmode = False
		elif(calccommand == "help"):
			print "Use +, -, *, / to do arythmetic operations. Type exitcalc to disable the calculator mode. Type help to see this message again. "
		elif(calccommand == "+"):
			value1 = input("First value: ")
			value2 = input("Second value: ")
			print "Result: ", value1 + value2
		elif(calccommand == "-"):
                        value1 = input("First value: ")
                        value2 = input("Second value: ")
                        print "Result: ", value1 - value2
                elif(calccommand == "*"):
                        value1 = input("First value: ")
                        value2 = input("Second value: ")
                        print "Result: ", value1 * value2
                elif(calccommand == "/"):
                        value1 = input("First value: ")
                        value2 = input("Second value: ")
                        print "Result: ", value1 / value2

		else:
			print "Type help to see how to use the calculator. "
print "Commands loaded!"

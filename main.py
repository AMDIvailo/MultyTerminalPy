import commands
import time
def main():
	while (1 == 1):
		command = raw_input('Command: ')
		if(command == "help"):
			commands.help()
		elif(command == "exit"):
			print "Exited!"
			exit()
		elif(command == "version"):
			commands.version();
		elif(command == "timer"):
			timertime = input('Enter time: ')
			commands.timer(timertime)
		elif(command == "calculator" or command == "calc"):
			commands.calculator()
		else:
			print "There is no such command!"

main()

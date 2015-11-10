import commands
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
		else:
			print "There is no such command!"

main()

def main():
	while (1 == 1):
		command = raw_input('Command: ')
		if(command == "help"):
			print "This is help!";
		elif(command == "exit"):
			print "Exited!"
			exit()

main()

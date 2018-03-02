import os

print """
	  _____  ____  ____     ___  _____  ____   ____  __ __  ______    ___  ____    _____
         |     ||    ||    \   /  _]|     ||    | /    ||  |  ||      |  /  _]|    \  / ___/
         |   __| |  | |  D  ) /  [_ |   __| |  | |   __||  |  ||      | /  [_ |  D  )(   \_ 
         |  |_   |  | |    / |    _]|  |_   |  | |  |  ||  _  ||_|  |_||    _]|    /  \__  |
         |   _]  |  | |    \ |   [_ |   _]  |  | |  |_ ||  |  |  |  |  |   [_ |    \  /  \ |
         |  |    |  | |  .  \|     ||  |    |  | |     ||  |  |  |  |  |     ||  .  \ \    |
         |__|   |____||__|\_||_____||__|   |____||___,_||__|__|  |__|  |_____||__|\_|  \___| """

print "                                   by fir3wa1k3r                                     "
while(True):
	flag = 0
	print "\nEnter the choice:"
	print "1.Create a ACL"
	print "2.Display ACL"
	print "3.Delete ACL"
	print "4.Exit"
	choice = int(raw_input())
	if choice == 1:
		sip = raw_input("\nEnter the source IP address:")
		destch = raw_input("\nDo you want to enter the destination IP address also, if yes press y else press n:")
		if destch == "y":
			flag = 1
		action = raw_input("\nChoose the action to be performed in the ACL, ACCEPT or DENY:")
		if flag == 1:
			dip = raw_input("\nEnter the destination IP address:")
			os.system("sudo iptables -I INPUT -s "+ sip +" -d "+dip+" -j "+action)
		else:
			os.system("sudo iptables -I INPUT -s "+ sip +" -j "+action)
	elif choice == 2:
		os.system("sudo iptables -L --line-numbers")
	elif choice == 3:
		ch = raw_input("\nEnter the ACL number to delete:")
		os.system("sudo iptables -D INPUT "+ch)
	else:
		print "\nThank you!!!"
		break

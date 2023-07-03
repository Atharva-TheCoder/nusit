#!/bin/bash
#NuSIT Installation

#main function - OS selection and user input

main() 
{
	clear #clearing screen
	echo
	echo -e '\e[96m <--- NuSIT Installation --->\e[0m' 
	echo
	sleep 1.0

	#OS selection
	echo "Where do you want to install?"
	echo '1) Linux (Deb, Ubuntu, ArchOS, etc)'
	echo '2) Termux'
	echo

	#user input
	read -p 'Select option [1/2]: ' INPUT
	action
}

#action based on the input
action() 
{
	if [[ $INPUT == 1 ]]; then
		echo 
		echo -e '\e[93mInstalling NuSIT...\e[0m'
		sleep 2.0
		linux
	elif [[ $INPUT == 2 ]]; then
		echo 
		echo -e '\e[93mInstalling NuSIT...\e[0m'
		sleep 2.0
		tmux
	else
		echo -e '\e[31mInvalid input!\e[0m'
		sleep 1.0
		main
	fi
}

#for linux os
linux() {
	#echo 'linux'
	sleep 3.0 
	mkdir /etc/nusit > /dev/null 2>&1
	mv core/linux/index.py /etc/nusit/ > /dev/null 2>&1
	mv core/linux/nusit /bin/ > /dev/null 2>&1
	chmod +x /bin/nusit > /dev/null 2>&1
	chmod +x /etc/nusit/index.py > /dev/null 2>&1
	install_success
	destruct
}

#for termux
tmux() {
	#echo 'tmux'
	sleep 3.0 
	mkdir /data/data/com.termux/files/usr/etc/nusit > /dev/null 2>&1
	mv core/tmux/index.py /data/data/com.termux/files/usr/etc/nusit/ > /dev/null 2>&1 
	mv core/tmux/nusit /data/data/com.termux/files/usr/bin/ > /dev/null 2>&1
	chmod +x /data/data/com.termux/files/usr/bin/nusit > /dev/null 2>&1
	chmod +x /data/data/com.termux/files/usr/etc/nusit/index.py > /dev/null 2>&1
	install_success
	destruct
}

#Installation success
install_success() {
	clear
	echo
	echo -e '\e[92m[ NuSIT Installed Successfully ]\e[0m'
	echo
	sleep 1.0
	echo -e 'Type \e[92m"nusit"\e[0m and hit Enter to start'
	echo
	echo 'Do you want to run a program?'
	echo '[1] Yes'
	echo '[2] No'
	echo
	read -p "Select option [1/2]: " RUN
	start
}

start(){
	if [[ $RUN == 1 ]]; then
		clear
		nusit
	elif [[ $RUN == 2 ]]; then
		echo
		destruct
		exit 
	else
		echo -e '\e[31mInvalid input!\e[0m'
		sleep 1.0
		install_success
	fi
}	

#Self destruction - remove all files
destruct() {
	rm -rf ../nusit > /dev/null 2>&1
}

#run program
main
exit

#Created by - Atharva Tilewale
#starting of the code

# import only system from os
from os import system, name
import time
import colorama
colorama.init()

#colors
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"


# define our clear function
def clear():
        
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

time.sleep(0.5) #screen pause 0.5sec

#NuSIT Banner

print LIGHT_GREEN
print """
ooooo      ooo              .oooooo..o ooooo ooooooooooooo 
`888b.     `8'             d8P'    `Y8 `888' 8'   888   `8 
 8 `88b.    8  oooo  oooo  Y88bo.       888       888      
 8   `88b.  8  `888  `888   `"Y8888o.   888       888      
 8     `88b.8   888   888       `"Y88b  888       888      
 8       `888   888   888  oo     .d8P  888       888      
o8o        `8   `V88V"V8P' 8""88888P'  o888o     o888o """

time.sleep(1)
print YELLOW
print """
O       o O       o O       o O       o O       o O       o
| O   o | | O   o | | O   o | | O   o | | O   o | | O   o |
| | O | | | | O | | | | O | | | | O | | | | O | | | | O | |
| o   O | | o   O | | o   O | | o   O | | o   O | | o   O |
o       O o       O o       O o       O o       O o       O 
"""
time.sleep(1)

print "" +END+"      <<---["+GREEN+BOLD+"Nu"+END+"cleotide "+GREEN+BOLD+ "S"+END+"equence "+GREEN+BOLD+"I"+END+"dentifier "+GREEN+BOLD+"T"+END+"ool]--->>"
print END
time.sleep(2)

#set key as true
key = True

#loop - will run till key = true
while (key == True):
    clear()
    #Enter main DNA sequence
    mainseq = (raw_input("Enter DNA sequence: "))
    
    #Enter target sequence
    targetseq = raw_input("Enter the target sequence: ")

    ### TESTS ###

    #length of main seq
    mlen = len(mainseq)
    #length of target seq
    tlen = len(targetseq)
    #no.of time sequence repeated
    repeat = mainseq.count(targetseq)

    #G count
    if("G" in mainseq):
        gcount = mainseq.count("G")
    else: 
        gcount = mainseq.count("g")

    #C count
    if("C" in mainseq):
        ccount = mainseq.count("C")
    else:
        ccount = mainseq.count("c")

    #GC count
    gccount = gcount + ccount

    #GC content
    gccontent = (str(gccount) + "/" + str(mlen))
    gccontentpercent = (float(gccount)/mlen)*100
    
    ### RESULTS ###
    
    print(" ")
    print(YELLOW + "<=== RESULTS ===>" + END)
    print(" ")

    #Length of main sequence
    print(LIGHT_WHITE + ">> Length of DNA sequence: " + LIGHT_CYAN + str(mlen) + " bases" + END) 

    #Length of identifying sequence
    print(LIGHT_WHITE + ">> Length of target sequence: " + LIGHT_CYAN + str(tlen) + " bases" + END)

    #check whether target sequence is present in main sequence
    if(targetseq in mainseq):
        print(LIGHT_WHITE + ">> Target sequence in DNA sequence: " + LIGHT_GREEN + "Present" + END)

        #No. of times sequence repeated
        print(LIGHT_WHITE + ">> No. of times sequence repeated: " + LIGHT_CYAN + str(repeat) + " times" + END)
    else:
        print(LIGHT_WHITE + ">> Target sequence in DNA sequence: " + LIGHT_RED + "Absent" + END)
        
    # show gcratio
    print(LIGHT_WHITE + ">> GC content: " + LIGHT_CYAN + gccontent + " = " + (str("{:.4f}".format(gccontentpercent)) + "%" + END))

    entry = True
    while (entry == True):
        print(LIGHT_WHITE)
        rerun = raw_input("Do you want to start a new task? (y/n): ")
        print(END)
        if(rerun == "y" or rerun == "Y"):
            key = True
            entry = False
        elif(rerun == "n" or rerun == "N"):
            key = False
            entry = False
        else:
            print(LIGHT_RED + "Invalid input!" + END)

    

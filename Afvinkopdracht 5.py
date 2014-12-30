##########################################################################
###Python Application to recall a certain DNA sequence in a large file####
###and eventually calculate its GC percentage, By: Richard Jansen#########
###HAN University of applied sciences, 12-11-2014#########################
##########################################################################

print ("Thank you for using this application, below you will be prompted for your intentions ")
####################################################################
###opening the file with an added notification in case of failure###
####################################################################
try:
	file = open("sequences.fa")
	sequence = file.readlines()
except IOError:
   print("bla")
##########################################################
###List of functions, execution depending on user input###
##########################################################
def main():  
    z = str(input("GCperc or SEQ? "))
    if z == "GCperc":
        GCperc()
    if z == "SEQ":
      	SEQ()
#################################################################
###Function to find the sequence in the file, using user input###
#################################################################
def SEQ():
    y = False
    try:
        x = str(input("welke sequentie?"))
        for line in sequence:
            if ">" in line and x in line:
                print (line)
                y = True
        if y == False:
            print ("░█▀▀ ░█▀█ ░█ ░█▀▀ ░░█▀▀ ░█▀█ ░█ ░█")
            print ("░█▀▀ ░█▀▀ ░█ ░█ ░░░░█▀▀ ░█▀█ ░█ ░█")
            print ("░▀▀▀ ░▀ ░░░▀ ░▀▀▀ ░░▀ ░░░▀░▀ ░▀ ░▀▀▀")
    except KeyboardInterrupt:
       print("You have Cancelled the operation ")
    except:
        print ("FATAL ERROR ")
##################################
###Still work in progress#########
##################################
def GCperc():
    print ("work in progress")
main()

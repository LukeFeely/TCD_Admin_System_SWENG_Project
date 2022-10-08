from config import  markingScheme
import sys
import pprint
import subprocess
import os



if(sys.argv[0]==None):
    print("You must specify the year as a command line argument")

else:
    markingScheme["year"] = int(sys.argv[1])
    outFile = open("config.py","w")
    outputString = "markingScheme = " + (str(markingScheme))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(outputString)
    outputString = outputString.replace(",",",\n")
    
    outFile.write(outputString)
    outFile.close()

    os.system("sh autoIndent.sh")
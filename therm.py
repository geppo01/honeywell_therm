#!/usr/bin/python

# By Brad Goodman
# http://www.bradgoodman.com/
# brad@bradgoodman.com

from therm_lib import *
import os
from os.path import expanduser
home=expanduser("~")
####################### Fill in settings below #######################


home_cfg = home + "/.thermrc"
if os.path.isfile(home_cfg) :
  # Read settings from file
  cfg_filename = home_cfg
elif os.path.isfile('./.thermrc') :
  # Read settings from file
  cfg_filename = "./.thermrc"

print "cfg_filename = " + cfg_filename
if (cfg_filename == "") :
  USERNAME="your@emailaddress.com"
  PASSWORD="your_total_comfort_password"
  DEVICE_IDS=[012345]
else :
  (USERNAME, PASSWORD, DEVICE_IDS) = read_settings_from_file(cfg_filename)

print "USERNAME: " + USERNAME
print "DEVICE_IDS: " + str(DEVICE_IDS)
DEVICE_ID = DEVICE_IDS[2]
############################ End settings ############################

def printUsage():
    print
    print "Cooling: -c temperature -t hold_time"
    print "Heating: -h temperature -t hold_time"
    print "Status: -s"
    print "Cancel: -x"
    print "Fan: -f [0=auto|1=on]"
    print
    print "Example: Set temperature to cool to 80f for 1 hour: \n\t therm.py -c 80 -t 1"
    print
    print "If no -t hold_time is provided, it will default to one hour from command time."
    print
    
    
def main():

  if (len(sys.argv) < 2) :
    printUsage()
    sys.exit()
  
  if sys.argv[1] == "-s":
    get_login("status", USERNAME, PASSWORD, DEVICE_ID)
    sys.exit()

  if sys.argv[1] == "-x":
    get_login("cancel", USERNAME, PASSWORD, DEVICE_ID)
    sys.exit()        
    
  if (len(sys.argv) < 3) or (sys.argv[1] == "-help"):
    printUsage()
    sys.exit()

  if sys.argv[1] == "-c":
    get_login("cool", USERNAME, PASSWORD, DEVICE_ID, sys.argv[2])
    sys.exit()

  if sys.argv[1] == "-h":
    get_login("heat", USERNAME, PASSWORD, DEVICE_ID, sys.argv[2])
    sys.exit()

  if sys.argv[1] == "-f":
    get_login("fan", USERNAME, PASSWORD, DEVICE_ID, sys.argv[2])
    sys.exit()        
        
if __name__ == "__main__":
    main()

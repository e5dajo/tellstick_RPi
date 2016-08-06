from subprocess import call
from astro import dusk 
from astro import dawn 
import re 
import config
from get_utc_from_local_time import get_utc


def checkdifftime(starttime,endtime):
   #return true if time diff is larger then config.min_light_time
   a= starttime.split(":")
   b= endtime.split(":")
   et=int(b[0])*60+int(b[1])
   st=int(a[0])*60+int(a[1])
   if (et-st<config.min_light_time):
      return False
   else:
      return True


#get morning and evning turn on/off times in UTC:
utc_evning_off_time = get_utc(config.evning_turnoff_time)
utc_morning_on_time = get_utc(config.morning_turnon_time)

#get dusk and dawn from astro.py
dusk_time =  dusk()
dawn_time =  dawn()
print "dusk:",dusk_time,"dawn:",dawn_time
#Handle evning timers (numbers specified in config.py)
if checkdifftime(dawn_time,utc_evning_off_time):
   for i in config.evning_timers:
      call(["/home/pi/tellstick/tdtool_on.sh",dawn_time,str(i)])
      call(["/home/pi/tellstick/tdtool_off.sh",utc_evning_off_time,str(i)])

#Handle morning timers (numbers specified in config.py)
if checkdifftime(utc_morning_on_time,dusk_time):
   for i in config.morning_timers:
      call(["/home/pi/tellstick/tdtool_on.sh",utc_morning_on_time,str(i)])
      call(["/home/pi/tellstick/tdtool_off.sh",dusk_time,str(i)])

#Handle lighs that are on during when dark:
for j in config.night_timers:
   call(["/home/pi/tellstick/tdtool_on.sh",dawn_time,str(j)])
   call(["/home/pi/tellstick/tdtool_off.sh",dusk_time,str(j)])


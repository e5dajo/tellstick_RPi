import ephem
from datetime import datetime



#Make an observer
kungsbacka      = ephem.Observer()

#PyEphem takes and returns only UTC times. 15:00 is noon in Fredericton
#kungsbacka.date = "2016-12-24 15:00:00"
kungsbacka.date = datetime.utcnow()
#print datetime.utcnow()

#Location of Kungsbacka, sweden
kungsbacka.lon  = str(12.076) #Note that lon should be in string format
kungsbacka.lat  = str(57.487)      #Note that lat should be in string format

#Elevation of Fredericton, Canada, in metres
kungsbacka.elev = 20

#To get U.S. Naval Astronomical Almanac values, use these settings
kungsbacka.pressure= 0
#fred.horizon = '-0:34'

sunrise=kungsbacka.previous_rising(ephem.Sun()) #Sunrise
noon   =kungsbacka.next_transit   (ephem.Sun(), start=sunrise) #Solar noon
sunset =kungsbacka.next_setting   (ephem.Sun()) #Sunset

#We relocate the horizon to get twilight times
kungsbacka.horizon = '-3' #-6=civil twilight, -12=nautical, -18=astronomical
beg_twilight=kungsbacka.previous_rising(ephem.Sun(), use_center=True) #Begin civil twilight
end_twilight=kungsbacka.next_setting   (ephem.Sun(), use_center=True) #End civil twilight

#print beg_twilight
#print end_twilight
#print sunset
#print datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S %Z')


def dusk():
   #fix time format to "hh:mm"
   a=str(beg_twilight)
   tmp=a.split(" ")[1].split(":")
   beg_twilight_short=tmp[0]+":"+tmp[1]
   return beg_twilight_short

def dawn():
   #fix time format to "hh:mm"
   a=str(end_twilight)
   tmp=a.split(" ")[1].split(":")
   end_twilight_short=tmp[0]+":"+tmp[1]
   return end_twilight_short


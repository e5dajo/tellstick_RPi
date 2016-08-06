import pytz
import datetime
local = pytz.timezone ("Europe/Stockholm")
def get_utc(local_time):
   date=datetime.datetime.utcnow().strftime('%Y-%m-%d')
   localtimestr = date + " " + local_time + ":00"
   naive = datetime.datetime.strptime (localtimestr, "%Y-%m-%d %H:%M:%S")
   local_dt = local.localize(naive, is_dst=None)
   utc_dt = local_dt.astimezone (pytz.utc) 
   return utc_dt.strftime('%H:%M')

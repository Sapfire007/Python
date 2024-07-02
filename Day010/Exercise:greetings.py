#in Shell : pip install pytz
from pytz import timezone
from datetime import date, datetime
ind_time_initial = datetime.now(timezone("Asia/Kolkata")).strftime('%d/%m/%Y %H:%M:%S.%f')
# ind_time_Hours = datetime.now(timezone("Asia/Kolkata")).strftime('%H')
if (datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') < "12:00:01" and datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S')>="00:00:00"):
  print("Good Morning!")
elif (datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') < "17:00:02" and datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') > "12:00:01"):
  print("Good Afternoon!")
elif (datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S') <= "23:59:59" and datetime.now(timezone("Asia/Kolkata")).strftime('%H') > "17:00:02"):
  print("Good Evening!")
print("Today's Date and Time is : ",ind_time_initial)
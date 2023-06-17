# CHAPTER 8 - IMPORTING LIBRARIES 
# TELLING TIME- Page 106/107

# import the datetime module 
from datetime import datetime

# create a Datetime object with attributes assigned current date and time values then display its contents
today = datetime.today()
print('Today is :' , today)

# create a loop to catch each attribute value individually
for atr in \
['year','month','day','hour','minute','second','microsecond']: print(atr , ':\t', getattr(today,atr))

# display time using dot notation
print('Time:', today.hour, ':' , today.minute , sep='')

# assign formatted day and month names to variables
day = today.strftime('%A')
month = today.strftime('%B')

#display the formatted date
print('Date:', day,month, today.day)

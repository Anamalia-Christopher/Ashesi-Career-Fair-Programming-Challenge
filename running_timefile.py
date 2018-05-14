import datetime
import draft2
start = datetime.datetime.now()

draft2.highest_cases()

stop = datetime.datetime.now()

time = stop-start
print ("it takes",time,"seconds to execute question d")

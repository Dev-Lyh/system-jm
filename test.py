from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.now().strftime("%Y_%m_%dT%H-%M-%S")

print("Date and time is:", dt)
print("Timestamp is:", str(ts))
print('./' + str(ts) + '.json')
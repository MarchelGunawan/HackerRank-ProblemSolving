# This question want to convert the time format 12 hour to 24 hour
# so 07:05:45PM become 19:05:45

def timeConvertion(time: str):
    # To take either AM or PM
    diff = time[8:10]
    """
        Need to take 2 digit of hour from time
        and convert it into integer.
        So later we can add 12 if it's PM 
        and substract it if it's AM 
    """
    hour = int(time[:2])
    minandsec = time[2:8]
    if diff == "PM":
        hour += 12
        """
            For the AM it will be a special case when hour is 12 since 12AM means 00 and 1 AM mean 01
            so we need substract if the hour is 12.
        """
    elif diff == "AM" and hour == 12:
        hour -= 12
    # we need to changeback the hour from integer to string.
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    return hour+minandsec

print("12:01:00AM =", timeConvertion("12:01:00AM"))
print("07:01:00PM =", timeConvertion("07:01:00PM"))
print("09:01:00AM =", timeConvertion("09:01:00AM"))
